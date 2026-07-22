"""add assigned_to column

Revision ID: 8a167f40e271
Revises: fc3bd3b74739
Create Date: 2026-07-22 16:57:17.627108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a167f40e271'
down_revision: Union[str, Sequence[str], None] = 'fc3bd3b74739'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column(
        'tickets',
        sa.Column('assigned_to', sa.String(length=100), nullable=True)
    )

    op.add_column(
        'tickets',
        sa.Column('assigned_to_email', sa.String(length=255), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('tickets', 'assigned_to_email')
    op.drop_column('tickets', 'assigned_to')
