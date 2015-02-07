"""empty message

Revision ID: 2b759ff46b1c
Revises: 560afa165e58
Create Date: 2015-02-07 14:35:03.711000

"""

# revision identifiers, used by Alembic.
revision = '2b759ff46b1c'
down_revision = '560afa165e58'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('type_project', 'category')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('type_project', sa.Column('category', mysql.ENUM(u'READING', u'DISPLAYING'), nullable=True))
    ### end Alembic commands ###
