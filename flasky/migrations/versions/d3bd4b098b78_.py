"""empty message

Revision ID: d3bd4b098b78
Revises: 21e84b27015e
Create Date: 2021-05-14 11:04:34.955349

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3bd4b098b78'
down_revision = '21e84b27015e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trade_records', 'activity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trade_records', sa.Column('activity', mysql.VARCHAR(length=10), nullable=False))
    # ### end Alembic commands ###