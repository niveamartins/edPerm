"""kill coluna aluno id complemento

Revision ID: 7d8137a0079c
Revises: 914d4e1406b3
Create Date: 2020-06-19 23:56:12.229193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d8137a0079c'
down_revision = '914d4e1406b3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('SET FOREIGN_KEY_CHECKS = 0;')
    op.execute('ALTER TABLE aluno DROP FOREIGN KEY aluno_ibfk_1 ; ')
    op.execute('ALTER TABLE aluno DROP FOREIGN KEY aluno_ibfk_2 ; ')
    op.drop_column('aluno','alunos_id_complemento')
    op.execute('SET FOREIGN_KEY_CHECKS = 1;')

def downgrade():
    op.add_column('aluno',sa.Column('alunos_id_complemento',sa.Integer, sa.ForeignKey('userComplemento.id_complemento'), nullable=False,))
