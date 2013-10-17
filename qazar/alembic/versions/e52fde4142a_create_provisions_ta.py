"""create provisions table

Revision ID: e52fde4142a
Revises: None
Create Date: 2013-10-16 17:47:26.035911

"""

# revision identifiers, used by Alembic.
revision = 'e52fde4142a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'provisions',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True)
        sa.Column('user_id', sa.Integer())
        sa.Column('ip_address', sa.VARCHAR(15))
        sa.Column('status', sa.Integer())
    )


def downgrade():
     op.drop_table('provisions')
