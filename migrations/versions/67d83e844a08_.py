"""empty message

Revision ID: 67d83e844a08
Revises: 
Create Date: 2021-02-11 22:23:51.994958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d83e844a08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cardapio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('petiscos', sa.String(length=50), nullable=False),
    sa.Column('doces', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha_hash', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('sucos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('abacaxi_hortela', sa.String(length=50), nullable=False),
    sa.Column('batata_doce', sa.String(length=50), nullable=False),
    sa.Column('detox', sa.String(length=50), nullable=False),
    sa.Column('laranja', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bebidas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('refrigerantes', sa.String(length=20), nullable=False),
    sa.Column('agua', sa.String(length=20), nullable=False),
    sa.Column('alcool', sa.String(length=20), nullable=False),
    sa.Column('cardapio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cardapio_id'], ['cardapio.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('bebidas', sa.Integer(), nullable=True),
    sa.Column('sucos', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bebidas'], ['bebidas.id'], ),
    sa.ForeignKeyConstraint(['sucos'], ['sucos.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('bebidas')
    op.drop_table('sucos')
    op.drop_table('login')
    op.drop_table('cardapio')
    # ### end Alembic commands ###
