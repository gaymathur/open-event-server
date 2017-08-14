"""empty message
Revision ID: 8a548c2338e6
Revises: a1c17effff1d
Create Date: 2017-05-21 22:35:28.931669
"""

# revision identifiers, used by Alembic.
revision = '8a548c2338e6'
down_revision = 'a1c17effff1d'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'end_time', new_column_name='ends_at')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'ends_at', new_column_name='end_time')
    ### end Alembic commands ###