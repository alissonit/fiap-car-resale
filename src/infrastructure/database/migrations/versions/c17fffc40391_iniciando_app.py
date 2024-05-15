"""iniciando app

Revision ID: c17fffc40391
Revises: 
Create Date: 2024-05-15 00:36:29.775679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c17fffc40391'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('car_user_id', sa.Integer(), nullable=True),
    sa.Column('car_brand', sa.String(), nullable=True),
    sa.Column('car_model', sa.String(), nullable=True),
    sa.Column('car_year', sa.Integer(), nullable=True),
    sa.Column('car_color', sa.String(), nullable=True),
    sa.Column('car_price', sa.Float(), nullable=True),
    sa.Column('car_type', sa.String(), nullable=True),
    sa.Column('car_condition', sa.String(), nullable=True),
    sa.Column('car_transmission', sa.String(), nullable=True),
    sa.Column('car_mileage', sa.Float(), nullable=True),
    sa.Column('car_engine', sa.Float(), nullable=True),
    sa.Column('car_fuel', sa.String(), nullable=True),
    sa.Column('car_description', sa.String(), nullable=True),
    sa.Column('car_armored', sa.Boolean(), nullable=True),
    sa.Column('car_sold', sa.Boolean(), nullable=True),
    sa.Column('car_created_at', sa.DateTime(), nullable=True),
    sa.Column('car_updated_at', sa.DateTime(), nullable=True),
    sa.Column('car_deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('car_id')
    )
    op.create_index(op.f('ix_cars_car_id'), 'cars', ['car_id'], unique=False)
    op.create_table('sales',
    sa.Column('sale_id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('buyer_cpf', sa.String(), nullable=True),
    sa.Column('sale_state', sa.String(), nullable=True),
    sa.Column('sale_date', sa.DateTime(), nullable=True),
    sa.Column('sale_created_at', sa.DateTime(), nullable=True),
    sa.Column('sale_updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('sale_id')
    )
    op.create_index(op.f('ix_sales_sale_id'), 'sales', ['sale_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sales_sale_id'), table_name='sales')
    op.drop_table('sales')
    op.drop_index(op.f('ix_cars_car_id'), table_name='cars')
    op.drop_table('cars')
    # ### end Alembic commands ###
