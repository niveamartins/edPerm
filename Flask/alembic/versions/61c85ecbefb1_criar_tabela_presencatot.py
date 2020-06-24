"""criar tabela presencatot

Revision ID: 61c85ecbefb1
Revises: f42afa6ec295
Create Date: 2020-06-17 18:01:36.654045

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '61c85ecbefb1'
down_revision = 'f42afa6ec295'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'presencatot',
        sa.Column('id_presencatot', sa.Integer, primary_key=True),
        sa.Column('presencatot_id_aluno',sa.Integer,sa.ForeignKey('aluno.id_aluno'),nullable=False),
        sa.Column('presencatot_id_turma',sa.Integer,sa.ForeignKey('turma.id_turma'),nullable=False),
        sa.Column('presenca_total',sa.Interval,nullable=False,default=datetime.timedelta(seconds=0))
    )


def downgrade():
    op.drop_table('presencatot')
