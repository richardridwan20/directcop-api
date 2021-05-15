"""create_providers_table

Revision ID: fb20365823ac
Revises: 016712d9f3f4
Create Date: 2021-05-12 16:15:59.112086

"""
from alembic import op
import sqlalchemy as sa
from app.utils.uuid import generate_uuid

# revision identifiers, used by Alembic.
revision = 'fb20365823ac'
down_revision = '016712d9f3f4'
branch_labels = None
depends_on = None


def upgrade():
    providers = op.create_table(
        'providers',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('name', sa.String(100)),
        sa.Column('slug', sa.String(100),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('url', sa.String(200)),
        sa.Column('is_active', sa.Boolean(), default=True),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    uuid = generate_uuid()

    op.bulk_insert(providers,
                   [
                        {'id': uuid,
                         'name': 'Nike',
                         'slug': 'nike',
                         'url': 'https://nike.com/sg'
                        }
                    ])
    pass


def downgrade():
    op.drop_table('providers')
    pass
