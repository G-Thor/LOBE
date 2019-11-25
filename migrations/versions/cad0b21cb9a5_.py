"""empty message

Revision ID: cad0b21cb9a5
Revises: 396445290990
Create Date: 2019-11-21 15:46:54.320746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cad0b21cb9a5'
down_revision = '396445290990'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Recording', 'plot_fname')
    op.drop_column('Recording', 'plot_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recording', sa.Column('plot_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Recording', sa.Column('plot_fname', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
