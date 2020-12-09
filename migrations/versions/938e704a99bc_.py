"""empty message

Revision ID: 938e704a99bc
Revises: 4e0962d591ac
Create Date: 2020-12-09 22:03:07.163647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '938e704a99bc'
down_revision = '4e0962d591ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('ordinal', sa.Integer(), nullable=True))
    op.drop_column('books', 'cardinal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('cardinal', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('books', 'ordinal')
    # ### end Alembic commands ###
