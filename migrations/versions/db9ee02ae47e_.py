"""empty message

Revision ID: db9ee02ae47e
Revises: 5ab9d2d0c181
Create Date: 2020-06-15 19:55:40.528791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9ee02ae47e'
down_revision = '5ab9d2d0c181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('verification', sa.Column('recording_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'verification', 'Recording', ['recording_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'verification', type_='foreignkey')
    op.drop_column('verification', 'recording_id')
    # ### end Alembic commands ###
