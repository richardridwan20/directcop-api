"""create_user_profiles_table

Revision ID: f85f09161a1d
Revises: fb20365823ac
Create Date: 2021-05-12 16:16:19.122510

"""
from alembic import op
import sqlalchemy as sa
from app.utils.uuid import generate_uuid


# revision identifiers, used by Alembic.
revision = 'f85f09161a1d'
down_revision = 'fb20365823ac'
branch_labels = None
depends_on = None


def upgrade():
    user_profiles = op.create_table(
        'user_profiles',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('user_id', sa.String(100)),
        sa.Column('provider_id', sa.String(100)),
        sa.Column('first_name', sa.String(100)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('address', sa.String(200)),
        sa.Column('postal_code', sa.String(100)),
        sa.Column('city', sa.String(100)),
        sa.Column('phone_number', sa.String(100)),
        sa.Column('email', sa.String(100)),
        sa.Column('is_active', sa.Boolean(), default=True),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )
    
    uuid = generate_uuid()
    
    # use existing relationship data
    conn = op.get_bind()
    res = conn.execute("select id from users WHERE full_name='Administrator'")
    results = res.fetchall()
    
    conn_provider = op.get_bind()
    res_provider = conn_provider.execute("select id from providers WHERE slug='nike'")
    results_provider = res_provider.fetchall()
    
    op.bulk_insert(user_profiles,
                   [
                        {'id': uuid,
                         'user_id': results[0][0],
                         'provider_id': results_provider[0][0],
                         'first_name': 'Sean',
                         'last_name': 'Wiryadi',
                         'address': 'Jalan Kemang no 12, Jakarta Selatan',
                         'postal_code': '11890',
                         'city': 'Jakarta',
                         'phone_number': '+6281297499300',
                         'email': 'sean@directcop.id',
                         'is_active': True,
                        }
                    ])
    
    pass


def downgrade():
    op.drop_table('user_profiles')
    pass
