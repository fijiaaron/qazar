"""Add a row

Revision ID: 1770ee90a63
Revises: e52fde4142a
Create Date: 2013-10-17 20:45:24.442121

"""

# revision identifiers, used by Alembic.
revision = '1770ee90a63'
down_revision = 'e52fde4142a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.bulk_insert('provisions',
            [{'id':1, 'user_id':1, 'ip_address':'123.456.789', 'status':''}])


def downgrade():
    pass
