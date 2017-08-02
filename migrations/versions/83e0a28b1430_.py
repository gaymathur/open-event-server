"""empty message

Revision ID: 83e0a28b1430
Revises: b79853132e71
Create Date: 2016-08-22 20:58:04.341000

"""

# revision identifiers, used by Alembic.
revision = '83e0a28b1430'
down_revision = 'b79853132e71'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket_holders', sa.Column('checked_in', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket_holders', 'checked_in')
    ### end Alembic commands ###