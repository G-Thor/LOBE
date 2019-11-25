"""empty message

Revision ID: b873b44b3709
Revises: 9bcbe67560e7
Create Date: 2019-11-07 23:36:54.101890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b873b44b3709'
down_revision = '9bcbe67560e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Session', sa.Column('collection_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Session', 'Collection', ['collection_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Session', type_='foreignkey')
    op.drop_column('Session', 'collection_id')
    # ### end Alembic commands ###