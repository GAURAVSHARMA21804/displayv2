"""little changes

Revision ID: 79351d7e1d45
Revises: 687f7439dd82
Create Date: 2024-03-26 15:28:47.797489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '79351d7e1d45'
down_revision = '687f7439dd82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parts_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('part_name', sa.String(length=64), nullable=False))
        batch_op.drop_column('parn_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parts_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parn_name', mysql.VARCHAR(length=64), nullable=False))
        batch_op.drop_column('part_name')

    # ### end Alembic commands ###
