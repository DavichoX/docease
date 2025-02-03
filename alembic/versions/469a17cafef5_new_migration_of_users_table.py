"""new migration of users table

Revision ID: 469a17cafef5
Revises: bb1032586d0a
Create Date: 2025-01-24 18:31:40.978810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '469a17cafef5'
down_revision: Union[str, None] = 'bb1032586d0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
