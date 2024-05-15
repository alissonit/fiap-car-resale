"""iniciando app

Revision ID: 0b6d13f68a51
Revises: c17fffc40391
Create Date: 2024-05-15 02:44:22.923996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b6d13f68a51'
down_revision: Union[str, None] = 'c17fffc40391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('sale_status', sa.String(), nullable=True))
    op.drop_column('sales', 'sale_state')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('sale_state', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('sales', 'sale_status')
    # ### end Alembic commands ###