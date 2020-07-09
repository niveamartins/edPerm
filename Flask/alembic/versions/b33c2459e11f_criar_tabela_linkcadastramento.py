"""Criar tabela LinkCadastramento

Revision ID: b33c2459e11f
Revises: 7d8137a0079c
Create Date: 2020-07-06 13:21:46.577064

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime, timedelta
import uuid

# revision identifiers, used by Alembic.
revision = 'b33c2459e11f'
down_revision = '7d8137a0079c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'link',
            sa.Column('token', sa.String(36), primary_key=True,
                default=str(uuid.uuid4())),
            sa.Column('link_id_turma', sa.Integer,
                sa.ForeignKey('turma.id_turma'), nullable=False),
            sa.Column('validade', sa.DateTime, nullable=False,
                default=datetime.now()+timedelta(minutes=3))
            )

def downgrade():
    op.drop_table('link')
