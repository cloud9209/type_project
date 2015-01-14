"""empty message

Revision ID: 248bbfcf5f79
Revises: None
Create Date: 2015-01-14 19:26:07.853000

"""

# revision identifiers, used by Alembic.
revision = '248bbfcf5f79'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('profile_image', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Enum('READING', 'DISPLAYING'), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_project_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['type_project.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_work',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('cretion_time', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['type_project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_work_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.Column('work_id', sa.Integer(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_id'], ['type_work.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('type_work_comment')
    op.drop_table('type_work')
    op.drop_table('type_project_comment')
    op.drop_table('type_project')
    op.drop_table('author')
    ### end Alembic commands ###