"""empty message

Revision ID: d45a8fe327c6
Revises: 60d60eb59f58
Create Date: 2020-07-14 09:08:58.454705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd45a8fe327c6'
down_revision = '60d60eb59f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('verifier_progression', sa.Column('equipped_font', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('verifier_progression', 'equipped_font')
    op.create_table('mos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('collection_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_samples', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['Collection.id'], name='mos_collection_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='mos_pkey')
    )
    # ### end Alembic commands ###
