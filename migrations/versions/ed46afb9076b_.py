"""empty message

Revision ID: ed46afb9076b
Revises: 5bf1deecbf3b
Create Date: 2020-10-16 05:39:17.818542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed46afb9076b'
down_revision = '5bf1deecbf3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Posting', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('Posting', sa.Column('dev', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Posting', 'dev')
    op.drop_column('Posting', 'active')
    # ### end Alembic commands ###
