"""Añade campo imagen a Comida

Revision ID: 9f9703f0898d
Revises: bfe035d00a6e
Create Date: 2022-01-30 16:38:32.012042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f9703f0898d'
down_revision = 'bfe035d00a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comida', sa.Column('imagen', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comida', 'imagen')
    # ### end Alembic commands ###
