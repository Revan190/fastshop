"""init

Revision ID: 799909f2b79d
Revises: 
Create Date: 2023-12-17 14:06:36.467099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlmodel.sql.sqltypes import AutoString  # Добавлено

# revision identifiers, used by Alembic.
revision: str = '799909f2b79d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', AutoString(), nullable=False),
        sa.Column('description', AutoString(), nullable=True),
        sa.Column('image', AutoString(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['parent_id'], ['categories.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', AutoString(), nullable=False),
        sa.Column('email', AutoString(), nullable=False),
        sa.Column('phone_number', AutoString(), nullable=False),
        sa.Column('hashed_password', AutoString(), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.Column('is_staff', sa.Boolean(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('first_name', AutoString(), nullable=False),
        sa.Column('last_name', AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', AutoString(), nullable=False),
        sa.Column('description', AutoString(), nullable=True),
        sa.Column('short_description', AutoString(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', AutoString(), nullable=False),
        sa.Column('phone_number', AutoString(), nullable=False),
        sa.Column('hashed_password', AutoString(), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.Column('is_staff', sa.Boolean(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('first_name', AutoString(), nullable=True),
        sa.Column('last_name', AutoString(), nullable=True),
        sa.Column('date_joined', sa.DateTime(), nullable=False),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.Column('is_temporary', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id']),
        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_discounts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('discount_percent', sa.Integer(), nullable=True),
        sa.Column('discount_amount', sa.Float(), nullable=True),
        sa.Column('valid_from', sa.DateTime(), nullable=False),
        sa.Column('valid_to', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('original', AutoString(), nullable=False),
        sa.Column('thumbnail', AutoString(), nullable=True),
        sa.Column('caption', AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock_records',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(), nullable=False),
        sa.Column('additional_info', AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_addresses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', AutoString(), nullable=True),
        sa.Column('city', AutoString(), nullable=False),
        sa.Column('street', AutoString(), nullable=False),
        sa.Column('house', AutoString(), nullable=False),
        sa.Column('apartment', AutoString(), nullable=True),
        sa.Column('post_code', AutoString(), nullable=True),
        sa.Column('floor', AutoString(), nullable=True),
        sa.Column('additional_info', AutoString(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_addresses')
    op.drop_table('stock_records')
    op.drop_table('product_images')
    op.drop_table('product_discounts')
    op.drop_table('product_categories')
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('company')
    op.drop_table('categories')
    # ### end Alembic commands ###
