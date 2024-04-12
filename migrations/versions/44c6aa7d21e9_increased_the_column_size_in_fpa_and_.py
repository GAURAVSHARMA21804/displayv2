"""Increased the column size in fpa_and_set_up_approved_records table

Revision ID: 44c6aa7d21e9
Revises: 7b56dc444025
Create Date: 2024-03-14 16:49:40.420345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44c6aa7d21e9'
down_revision = '7b56dc444025'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fpa_and_set_up_approved_records', schema=None) as batch_op:
        batch_op.alter_column('start_shift_1_parameters_values',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=1500),
               existing_nullable=True)
        batch_op.alter_column('start_shift_2_parameters_values',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=1500),
               existing_nullable=True)
        batch_op.alter_column('end_shift_1_parameters_values',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=1500),
               existing_nullable=True)
        batch_op.alter_column('end_shift_2_parameters_values',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=1500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fpa_and_set_up_approved_records', schema=None) as batch_op:
        batch_op.alter_column('end_shift_2_parameters_values',
               existing_type=sa.String(length=1500),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('end_shift_1_parameters_values',
               existing_type=sa.String(length=1500),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('start_shift_2_parameters_values',
               existing_type=sa.String(length=1500),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('start_shift_1_parameters_values',
               existing_type=sa.String(length=1500),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###