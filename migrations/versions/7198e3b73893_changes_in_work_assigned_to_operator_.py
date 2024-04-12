"""changes in work_assigned_to_operator table again

Revision ID: 7198e3b73893
Revises: 7786c470bb64
Create Date: 2024-03-12 17:35:58.500992

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7198e3b73893'
down_revision = '7786c470bb64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_assigned_to_operator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('shift', sa.String(length=2), nullable=False))
        batch_op.add_column(sa.Column('total_assigned_task', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('left_for_rework', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('passed', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('filled', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('failed', sa.Integer(), nullable=True))
        batch_op.drop_column('employee_id_id')

    with op.batch_alter_table('work_assigned_to_operator_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('shift', sa.String(length=2), nullable=False))
        batch_op.add_column(sa.Column('total_assigned_task', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('left_for_rework', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('passed', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('filled', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('failed', sa.Integer(), nullable=True))
        batch_op.drop_column('employee_id_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_assigned_to_operator_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id_id', mysql.VARCHAR(length=20), nullable=False))
        batch_op.drop_column('failed')
        batch_op.drop_column('filled')
        batch_op.drop_column('passed')
        batch_op.drop_column('left_for_rework')
        batch_op.drop_column('total_assigned_task')
        batch_op.drop_column('shift')
        batch_op.drop_column('employee_id')

    with op.batch_alter_table('work_assigned_to_operator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id_id', mysql.VARCHAR(length=20), nullable=False))
        batch_op.drop_column('failed')
        batch_op.drop_column('filled')
        batch_op.drop_column('passed')
        batch_op.drop_column('left_for_rework')
        batch_op.drop_column('total_assigned_task')
        batch_op.drop_column('shift')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###