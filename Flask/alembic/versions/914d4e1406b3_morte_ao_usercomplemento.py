"""Morte ao usercomplemento

Revision ID: 914d4e1406b3
Revises: 61c85ecbefb1
Create Date: 2020-06-19 20:43:58.162211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '914d4e1406b3'
down_revision = '61c85ecbefb1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('SET FOREIGN_KEY_CHECKS = 0;')
    op.drop_table('userComplemento')
    op.drop_table('user')
    op.create_table(
        'user' ,
        sa.Column('Id', sa.Integer, primary_key = True),
        sa.Column('usuario',sa.Text, nullable=False),
        sa.Column('email',sa.Text, nullable=False),
        sa.Column('senha',sa.Text,nullable=False),
        sa.Column('cpf',sa.String(11), nullable=False),
        sa.Column('telefone',sa.String(9),nullable=False),
        sa.Column('Tipo',sa.Enum('adm','gestor','coordenador', 'propositor','cursista','apoiador'), nullable=False),
        sa.Column('funcao',sa.String(20),nullable=True),
        sa.Column('profissao',sa.String(30),nullable=True),
        sa.Column('UnidadeBasicaDeSaude',sa.String(30), nullable=True),
        sa.Column('CAP',sa.String(4),nullable=True)
)
    op.execute('SET FOREIGN_KEY_CHECKS = 1;')

def downgrade():
    op.drop_table('user')    
    op.create_table(
        'user',
        sa.Column('Id', sa.Integer, primary_key = True),
        sa.Column('usuario',sa.Text, nullable=False),
        sa.Column('email',sa.Text, nullable=False),
        sa.Column('senha',sa.Text,nullable=False),
        sa.Column('cpf',sa.String(11), nullable=False),
        sa.Column('telefone',sa.String(9),nullable=False),
        sa.Column('Tipo',sa.Enum('adm','gestor','coordenador', 'propositor','cursista','apoiador'), nullable=False)
        )
    op.create_table(
        'userComplemento',
        sa.Column('id_usercomplemento', sa.Integer, primary_key=True),
        sa.Column('user_id_usercomplemento', sa.Integer, sa.ForeignKey('user.Id'),primary_key=True),
        sa.Column('funcao',sa.String(20),nullable=True),
        sa.Column('profissao',sa.String(30),nullable=True),
        sa.Column('UnidadeBasicaDeSaude',sa.String(30), nullable=True),
        sa.Column('CAP',sa.String(4),nullable=True)
    )
    