"""add_payment_to_user_profiles_table

Revision ID: 5e29acb83dbb
Revises: d508d7813b45
Create Date: 2021-06-03 19:03:43.481535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e29acb83dbb'
down_revision = 'd508d7813b45'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user_profiles', sa.Column('card_name', sa.String(200), nullable=True))
    op.add_column('user_profiles', sa.Column('card_number', sa.String(200), nullable=True))
    op.add_column('user_profiles', sa.Column('card_expiry_date', sa.String(50), nullable=True))
    op.add_column('user_profiles', sa.Column('card_cvv', sa.String(50), nullable=True))
    op.add_column('user_profiles', sa.Column('address_2', sa.String(300), nullable=True))
    op.add_column('user_profiles', sa.Column('address_3', sa.String(300), nullable=True))
    pass


def downgrade():
    op.drop_column('user_profiles', 'card_name')
    op.drop_column('user_profiles', 'card_number')
    op.drop_column('user_profiles', 'card_expiry_date')
    op.drop_column('user_profiles', 'card_cvv')
    op.drop_column('user_profiles', 'address_2')
    op.drop_column('user_profiles', 'address_3')
    pass
