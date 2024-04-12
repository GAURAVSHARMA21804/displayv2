"""Increased the size of process_name in processes_info

Revision ID: 7ab17214a5e4
Revises: 7198e3b73893
Create Date: 2024-03-13 11:28:37.684326

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7ab17214a5e4'
down_revision = '7198e3b73893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.alter_column('parameter_name',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.String(length=220),
               existing_nullable=False)

    with op.batch_alter_table('processes_info', schema=None) as batch_op:
        batch_op.alter_column('process_name',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.String(length=220),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('processes_info', schema=None) as batch_op:
        batch_op.alter_column('process_name',
               existing_type=sa.String(length=220),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=False)

    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.alter_column('parameter_name',
               existing_type=sa.String(length=220),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###