"""Changed Blog and User models

Revision ID: 077d1a989464
Revises: 74b08d161343
Create Date: 2020-07-22 15:25:53.807330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077d1a989464'
down_revision = '74b08d161343'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'picture')
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('date', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'posted')
    op.add_column('blogs', sa.Column('picture', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
