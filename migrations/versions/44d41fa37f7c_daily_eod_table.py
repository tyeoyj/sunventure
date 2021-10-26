"""Daily EOD table

Revision ID: 44d41fa37f7c
Revises: 
Create Date: 2021-10-24 22:28:47.737354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d41fa37f7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dailyEOD',
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('close', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dailyEOD')
    # ### end Alembic commands ###
