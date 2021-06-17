"""add_province_country_user_profile

Revision ID: 255ec46426b7
Revises: 7b6fc5e2332f
Create Date: 2021-06-17 16:38:17.958291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '255ec46426b7'
down_revision = '7b6fc5e2332f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user_profiles', sa.Column('province', sa.String(200), nullable=True))
    op.add_column('user_profiles', sa.Column('country', sa.String(200), nullable=True))
    pass


def downgrade():
    op.drop_column('user_profiles', 'province')
    op.drop_column('user_profiles', 'country')
    pass
