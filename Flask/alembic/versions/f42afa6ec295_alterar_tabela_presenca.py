"""alterar tabela presenca

Revision ID: f42afa6ec295
Revises: 
Create Date: 2020-06-17 17:28:18.193381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f42afa6ec295'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('presenca','ultimoCheckIn')
    op.drop_column('presenca','presencaTotal')
    op.drop_column('presenca','presencaAtualizada')
    op.add_column('presenca', sa.Column('checkIn', sa.DateTime, nullable=False))
    op.add_column('presenca', sa.Column('presencaValidade', sa.Boolean, nullable=False, default=False))


def downgrade():
    op.drop_column('presenca','presencaValidade')
    op.drop_column('presenca','checkIn')
    op.add_column('presenca',sa.Column('ultimoCheckIn',sa.DateTime,nullable=True)) 
    op.add_column('presenca',sa.Column('presencaTotal',sa.DateTime,nullable=False))
    op.add_column('presenca',sa.Column('presencaAtualizada',sa.Boolean,nullable=True))
    
