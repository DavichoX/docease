"""new new migration

Revision ID: 809318f314c1
Revises: 469a17cafef5
Create Date: 2025-01-27 18:16:18.491184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '809318f314c1'
down_revision: Union[str, None] = '469a17cafef5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
