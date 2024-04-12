from flask import request, session, jsonify, current_app
from collections import Counter
from Database.models import Operator_creds, fpa_and_set_up_approved_records, reading_params, stations, work_assigned_to_operator, processes_info, parameters_info, check_sheet, notify_to_incharge, check_sheet_data ,floor_incharge_creds
from Database.init_and_conf import db
from datetime import datetime
from Config.token_handler import TokenRequirements
import pytz

def operator_login(data):
    try:
        employee_id = data.get('employee_code')
        password = data.get('password')
        # date = datetime.now().date()
        # time = datetime.now().time()
        
        user = Operator_creds.query.filter_by(employee_id=employee_id).first()
        
        if user is not None:
            if user.password == password:
                session['logged_in'] = True
                token = TokenRequirements.create_token(employee_id=employee_id, mobile_no = user.mobile, secret_key=current_app.config['SECRET_KEY'])
                return jsonify({'Response': 'Operator login successfull!', 'token': f'{token}', 'employee_id':f'{user.employee_id}', 'fName': f'{user.fName}', 'lName': f'{user.lName}', 'skill':f'{user.skill_level}','dob':f'{user.dob}','mobile':f'{user.mobile}','email':f'{user.email}','password':f'{user.password}'}), 200
            else:
                return jsonify({'Response:': 'Authentication Failed!'}), 401
        else:
            return jsonify({'Response:': 'User Not Found!'}), 404
    except Exception as e:
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422

def get_task(data):
    try:
        station_id = data.get('station_id')
        current_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        date = datetime.now(pytz.timezone('Asia/Kolkata')).date()
        get_task_data = work_assigned_to_operator.query.filter_by(station_id=station_id).first()
        if  get_task_data:
            if get_task_data.date==date:
                if get_task_data.end_shift_time>=current_time:
                    # work_data = []
                    task_data = {
                        'station_id': get_task_data.station_id,
                        'part_no': get_task_data.part_no,
                        'process_no':get_task_data.process_no,
                        'start_shift_time':get_task_data.start_shift_time.strftime('%H:%M:%S'),
                        'end_shift_time':get_task_data.end_shift_time.strftime('%H:%M:%S'),
                        'assigned_by_owner':get_task_data.assigned_by_owner,
                        'operator_login_status':get_task_data.operator_login_status,
                        'employee_id':get_task_data.employee_id,
                        'shift':get_task_data.shift,
                        'total_assigned_task':get_task_data.total_assigned_task,
                        'left_for_rework':get_task_data.left_for_rework,
                        'passed':get_task_data.passed,
                        'filled':get_task_data.filled,
                        'failed':get_task_data.failed
                        # Add other relevant fields here
                    }
                    # work_data.append(task_data)
                    assigned_process = get_task_data.process_no
                    print(assigned_process)
                    get_process_data = processes_info.query.filter_by(process_no=assigned_process).first()
                    images_urls = get_process_data.images_urls
                    
                    get_parameters = parameters_info.query.filter_by(process_no=assigned_process).all()
                    process_params_info = []
                    for process_param in get_parameters:
                        # parameter_no = process_param.parameter_no
                        one_param_data = {"parameter_no": process_param.parameter_no, "parameter_name": process_param.parameter_name, "process_no": process_param.process_no, "belongs_to_part": process_param.belongs_to_part, "min": process_param.min,"max": process_param.max, "unit": process_param.unit, "FPA_status": process_param.FPA_status, "readings_is_available": process_param.readings_is_available}
                        # parameter_name = process_param.parameter_name
                        # process_no = process_param.process_no
                        # belongs_to_part = process_param.belongs_to_part
                        # min = process_param.min
                        # max = process_param.max
                        # unit = process_param.unit
                        # FPA_status = process_param.FPA_status
                        # readings_is_available = process_param.readings_is_available
                        # if parameter_no not in process_params_info:
                        #     process_params_info[parameter_no] = []
                        # process_params_info[parameter_no].extend(one_param_data)
                        process_params_info.append(one_param_data)
                    
                    check_sheet_entity_datas = db.session.query(check_sheet.csp_id, check_sheet.csp_name, check_sheet.csp_name_hindi, check_sheet.specification, check_sheet.control_method, check_sheet.frequency).all()
                    check_sheet_datas = [{'csp_id': csp_id, 'csp_name': csp_name, 'csp_name_hindi': csp_name_hindi, 'specification': specification, 'control_method': control_method, 'frequency': frequency} for csp_id, csp_name, csp_name_hindi, specification, control_method, frequency in check_sheet_entity_datas]
                    
                    check_sheet_status_for_operator = check_sheet_data.query.filter_by(station_id=station_id).first()
                    if check_sheet_status_for_operator:
                        check_sheet_fill_status = True
                    else:
                        check_sheet_fill_status = False
                    
                    # get_station_data=stations.query.filter_by(station_id=station_id).first()
                    # floor_no = get_station_data.floor_no
                    # get_floor_incharge_creds = floor_incharge_creds.query.filter_by(floor_no=floor_no).first()
                    # employee_id_floor_incharg= get_floor_incharge_creds.employee_id
                    emoloyee_id_floor_incharge=get_task_data.assigned_by_owner
                    

                    
                    return jsonify({"work_operator_data":task_data,"urls":images_urls, "check_sheet_datas":check_sheet_datas, "total_check_sheet_params": len(check_sheet_datas), "process_params_info":process_params_info, "check_sheet_fill_status":check_sheet_fill_status, "emoloyee_id_floor_incharge":emoloyee_id_floor_incharge}), 200
                else:
                    return jsonify({"Message":"no task assigned to this station at current shift..."}), 404
            else:
                return jsonify({"Message":"no task assigned to this station today..."}), 404
        else:
            return jsonify({"Message":"This station never assigned any task or doesn't exist..."}), 404
    except Exception as e:
        # db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422





def add_work(data):
    try:
        operator_employee_id = data.get('operator_employee_id')
        date = datetime.now().date()

        existing_operator_today = fpa_and_set_up_approved_records.query.filter_by(
            operator_employee_id=operator_employee_id, date=date
        ).first()

        if existing_operator_today:
            updated = False  # Flag to check if update is needed

            for shift in ['start_shift_1', 'start_shift_2', 'end_shift_1', 'end_shift_2']:
                parameters_values_key = f"{shift}_parameters_values"
                time_key = f"{shift}_time"

                if data.get(parameters_values_key) and not getattr(existing_operator_today, parameters_values_key):
                    setattr(existing_operator_today, parameters_values_key, data.get(parameters_values_key))
                    setattr(existing_operator_today, time_key, datetime.now().time())
                    updated = True

            if updated:
                db.session.commit()
                return jsonify({"Message": "Your work updates have been saved successfully"}), 200
            else:
                return jsonify({"Message": "No updates were necessary"}), 200
        else:
            new_work = fpa_and_set_up_approved_records(
                operator_employee_id=operator_employee_id,
                start_shift_1_parameters_values=data.get('start_shift_1_parameters_values', ''),
                start_shift_1_time=datetime.now().time() if data.get('start_shift_1_parameters_values') else None,
                date=date
            )
            db.session.add(new_work)
            db.session.commit()
            return jsonify({"Message": "Your new work record has been added successfully"}), 200

        
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422

def add_reading(data):
    try:
        operator_employee_id = data.get('operator_employee_id')
        parameter_no = data.get('parameter_no')
        # operator_employee_id = data.get['operator_employee_id']
        date = datetime.now().date()

        existing_parameter = reading_params.query.filter_by(
            parameter_no=parameter_no, date=date
        ).first()

        if existing_parameter:
            updated = False  # Flag to check if update is needed

            for no in [1,2,3,4,5]:
                reading_values_key = f"reading_{no}"
                time_key = f"reading_{no}_time"

                if data.get(reading_values_key) and not getattr(existing_parameter, reading_values_key):
                    setattr(existing_parameter, reading_values_key, data.get(reading_values_key))
                    setattr(existing_parameter, time_key, datetime.now().time())
                    updated = True

            if updated:
                db.session.commit()
                return jsonify({"Message": "Your reading updates have been saved successfully"}), 200
            else:
                return jsonify({"Message": "No reading were necessary to update"}), 200
        else:
            new_reading = reading_params(
                operator_employee_id=operator_employee_id,
                parameter_no=parameter_no,
                reading_1=data.get('reading_1', ''),
                reading_1_time=datetime.now().time() if data.get('reading_1') else None,
                # reading_2=data.get('reading_2', ''),
                # reading_2_time=datetime.now().time() if data.get('reading_2') else None,
                
                # reading_3=data.get('reading_3', ''),
                # reading_3_time=datetime.now().time() if data.get('reading_3') else None,
                
                # reading_4=data.get('reading_4', ''),
                # reading_4_time=datetime.now().time() if data.get('reading_4') else None,
                # reading_5=data.get('reading_5', ''),
                # reading_5_time=datetime.now().time() if data.get('reading_5') else None,
                                
                date=date
            )
            db.session.add(new_reading)
            db.session.commit()
            return jsonify({"Message": "Your new reading record has been added successfully"}), 200

        
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422


def update_work_status(data):
    try:
        station_id = data.get('station_id')
        get_station_data = work_assigned_to_operator.query.filter_by(station_id=station_id).first()
        if get_station_data:
            get_station_data.passed = data.get('passed') or get_station_data.passed
            get_station_data.filled = data.get('filled') or get_station_data.filled
            get_station_data.failed = data.get('failed') or get_station_data.failed
            
            db.session.commit()
            return jsonify({"Message":"Part has been updated Successfully"}),200
        else:
            return jsonify({"Message":"No part is available"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422


def notify_to_incharge_func(data):
    try:
        station_id = data.get("station_id")
        csp_id = data.get("csp_id")
        floor_no = data.get("floor_no")
        date_and_time = datetime.now()
        
        add_notification = notify_to_incharge(station_id=station_id, csp_id=csp_id, floor_no=floor_no, created_at=date_and_time)
        db.session.add(add_notification)
        db.session.commit()
        return jsonify({"Message":f"Notification sent to in-charge for Station ID :{station_id}"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422

def checksheet_add_logs(data):
    try:
        # csp_id = data.get('csp_id')
        
        oprtr_employee_id = data.get('oprtr_employee_id')
        flrInchr_employee_id = data.get('flrInchr_employee_id')
        status_datas = data.get('status_datas')
        station_id=data.get('station_id')
        
        add_checksheet_data = check_sheet_data(oprtr_employee_id=oprtr_employee_id, flrInchr_employee_id=flrInchr_employee_id, status_datas=status_datas,station_id=station_id)
        db.session.add(add_checksheet_data)
        db.session.commit()
        return jsonify({"Message": "Check sheet data submited successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422
    

# def work_operator_get_data(data):
    try:
        station_id = data.get('station_id')
        current_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        date = datetime.now(pytz.timezone('Asia/Kolkata')).date()
        
        get_task_data = work_assigned_to_operator.query.filter_by(station_id=station_id).first()
        if  get_task_data:
            if get_task_data.date==date:
                # start_shift_time = datetime.strptime(get_task_data.start_shift_time, '%H:%M:%S').time()
                # end_shift_time = datetime.strptime(get_task_data.end_shift_time, '%H:%M:%S').time()
                if get_task_data.end_shift_time >= current_time:
                # if get_task_data.end_shift_time>=current_time:
                    task_data = {
                        'station_id': get_task_data.station_id,
                        'part_no': get_task_data.part_no,
                        'process_no':get_task_data.process_no,
                        'start_shift_time':get_task_data.start_shift_time.strftime('%H:%M:%S'),
                        'end_shift_time':get_task_data.end_shift_time.strftime('%H:%M:%S'),
                        'assigned_by_owner':get_task_data.assigned_by_owner,
                        'operator_login_status':get_task_data.operator_login_status,
                        'employee_id':get_task_data.employee_id,
                        'shift':get_task_data.shift,
                        'total_assigned_task':get_task_data.total_assigned_task,
                        'left_for_rework':get_task_data.left_for_rework,
                        'passed':get_task_data.passed,
                        'filled':get_task_data.filled,
                        'failed':get_task_data.failed
                        # Add other relevant fields here
                    }
                    return  jsonify({"work_operator_data":task_data}), 200
                else:
                    return jsonify("No task asssigned in this station or  your shift has been completed"),503
            else:
                return jsonify("No task assigned today"),404
        else:
            return jsonify("NO station found"),404
    except Exception as e:
        # db.session.rollback()
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422



##################### fpa data ################ api
# def get_fpa_data(data):
#     try:
#         line_no=data.get('line_no')
#         # Fetch all station_ids for the given floor_no
#         is_not_approved = False
#         current_lines_data = stations.query.filter_by(line_no=line_no).all()
#         if current_lines_data:
#             all_stations = [entity.station_id for entity in current_lines_data]
#             print(all_stations)
#             for station_id in all_stations:
#                 operator_data = work_assigned_to_operator.query.filter_by(station_id=station_id).all()
#                 print(operator_data)
#                 if operator_data:
#                     for operator in operator_data:
#                         if operator.passed < 2 and operator.failed > 0:
#                             is_not_approved = True
#                             break
#                     if is_not_approved:
#                         break  # Exit the outer loop if the condition is met   
#             return jsonify({" For this line_no is_approved value is":is_not_approved}),200
#         else:
#             return jsonify({"Message": "No stations found for the given line_no."}), 404
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'Error': f'Failed to fetch data: {e}'}), 500

# def get_fpa_data(data):
#     try:
#         # station_id = data.get('station_id')
    
#         line_no=data.get('line_no')
#         current_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
#         date = datetime.now(pytz.timezone('Asia/Kolkata')).date()
#         # all_lines_stations=[]
#         # Fetch all station_ids for the given floor_no
#         # is_not_approved = False
#         current_lines_data = stations.query.filter_by(line_no=line_no).all()
#         if current_lines_data:
#             # for entity in range(0, len(current_lines_data)):
#             #     all_lines_stations.append(current_lines_data[entity].station_id)
#             # # all_duplicates = dict(Counter(all_stations))
#             # all_lines_stations.sort()
#             all_stations = [entity.station_id for entity in current_lines_data]
#             print(all_stations)
#             # print(all_lines_stations)
#             result = {}
#             for station_id in all_stations:
#                 operator_data = work_assigned_to_operator.query.filter_by(station_id=station_id).all()
#                 print(operator_data)
#                 if operator_data:
#                     station_result = []
#                     for operator in operator_data:
#                         if operator.date == date and operator.end_shift_time >= current_time:
#                             station_result.append({
#                             'station_id':operator_data.station_id,
#                             'part_no': operator_data.part_no,
#                             'process_no':operator_data.process_no,
#                             'start_shift_time':operator_data.start_shift_time.strftime('%H:%M:%S'),
#                             'end_shift_time':operator_data.end_shift_time.strftime('%H:%M:%S'),
#                             'total_assigned_task':operator_data.total_assigned_task,
#                             'passed':operator_data.passed,
#                             'failed':operator_data.failed
#                         # Add other relevant fields here
#                              })
#                     result[station_id] = station_result
#                             # return jsonify({"work_operator_data":task_data}), 200

#                 else:
#                     result[station_id]=[]
#             return jsonify({"work_operator_data": result}), 200
#         else:
#             return jsonify({"error":"No such Line Number Found!"}),  404
#     except Exception as e:
#         # db.session.rollback()
#         return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422

def get_fpa_data(data):
    try:
        line_no = data.get('line_no')
        current_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        date = datetime.now(pytz.timezone('Asia/Kolkata')).date()
        current_lines_data = stations.query.filter_by(line_no=line_no).all()
        if current_lines_data:
            all_stations = [entity.station_id for entity in current_lines_data]
            result = []
            for station_id in all_stations:
                operator_data = work_assigned_to_operator.query.filter_by(station_id=station_id).all()
                if operator_data:
            
                    for operator in operator_data:
                        if operator.date == date and operator.end_shift_time >= current_time:
                            result.append({
                                'station': {
                                    'station_id': operator.station_id,
                                    'part_no': operator.part_no,
                                    'process_no': operator.process_no,
                                    'start_shift_time': operator.start_shift_time.strftime('%H:%M:%S'),
                                    'end_shift_time': operator.end_shift_time.strftime('%H:%M:%S'),
                                    'total_assigned_task': operator.total_assigned_task,
                                    'passed': operator.passed,
                                    'failed': operator.failed
                                    # Add other relevant fields here
                                }
                            })
                    
            return jsonify({"work_operator_data": result}), 200
        else:
            return jsonify({"error": "No such Line Number Found!"}), 404
    except Exception as e:
        return jsonify({'Error': f'Block is not able to execute successfully {e}'}), 422