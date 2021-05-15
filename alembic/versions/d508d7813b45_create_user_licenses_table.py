"""create_user_licenses_table

Revision ID: d508d7813b45
Revises: f85f09161a1d
Create Date: 2021-05-12 16:36:35.403444

"""
from alembic import op
import sqlalchemy as sa
from app.utils.uuid import generate_uuid


# revision identifiers, used by Alembic.
revision = 'd508d7813b45'
down_revision = 'f85f09161a1d'
branch_labels = None
depends_on = None


def upgrade():
    user_licenses = op.create_table(
        'user_licenses',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('user_id', sa.String(100)),
        sa.Column('license_type', sa.String(100)),
        sa.Column('start_date', sa.String(100)),
        sa.Column('end_date', sa.String(100)),
        sa.Column('status', sa.String(100)),
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
    
    op.bulk_insert(user_licenses,
                   [
                        {'id': uuid,
                         'user_id': results[0][0],
                         'license_type': 'permanent',
                         'start_date': '2021-05-12',
                         'end_date': '2099-05-12',
                         'status': 'active'
                        }
                    ])
    
    pass


def downgrade():
    op.drop_table('user_licenses')
    pass
