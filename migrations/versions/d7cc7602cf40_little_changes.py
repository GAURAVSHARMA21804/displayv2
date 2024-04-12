"""little changes

Revision ID: d7cc7602cf40
Revises: 7f2a1db8f5e1
Create Date: 2024-03-19 17:14:48.353307

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd7cc7602cf40'
down_revision = '7f2a1db8f5e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('check_sheet', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('check_sheet_data', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('check_sheet_data_logs', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('params_ucl_lcl', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('parts_info', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('processes_info', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('stations', schema=None) as batch_op:
        batch_op.alter_column('added_time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('added_date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('work_assigned_to_operator', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    with op.batch_alter_table('work_assigned_to_operator_logs', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_assigned_to_operator_logs', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('work_assigned_to_operator', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('stations', schema=None) as batch_op:
        batch_op.alter_column('added_date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('added_time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('processes_info', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('parts_info', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('params_ucl_lcl', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('check_sheet_data_logs', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('check_sheet_data', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('check_sheet', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('time',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###