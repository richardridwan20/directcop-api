"""add_profile_name_to_user_profiles

Revision ID: 7b6fc5e2332f
Revises: 5e29acb83dbb
Create Date: 2021-06-11 20:46:03.192213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b6fc5e2332f'
down_revision = '5e29acb83dbb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user_profiles', sa.Column('profile_name', sa.String(200), nullable=True))
    pass


def downgrade():
    op.drop_column('user_profiles', 'profile_name')
    pass
