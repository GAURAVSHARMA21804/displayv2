"""Created and update some tables

Revision ID: 7b56dc444025
Revises: 9435ca98da0e
Create Date: 2024-03-14 16:16:26.932592

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b56dc444025'
down_revision = '9435ca98da0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('floor_incharge_creds', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('min', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('max', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('unit', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('FPA_status', sa.Boolean(), nullable=True))

    with op.batch_alter_table('station_info', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('station_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('parameters_info', schema=None) as batch_op:
        batch_op.drop_column('FPA_status')
        batch_op.drop_column('unit')
        batch_op.drop_column('max')
        batch_op.drop_column('min')

    with op.batch_alter_table('floor_incharge_creds', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
