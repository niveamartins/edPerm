CREATE TABLE IF NOT EXISTS user (	
id INTEGER PRIMARY KEY auto_increment,
usuario TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL,
cpf VARCHAR(11) NOT NULL,
telefone VARCHAR(9) NOT NULL,
tipo ENUM('adm','gestor','coordenador','propositor','cursista','apoiador')
);


CREATE TABLE IF NOT EXISTS turma(
id_turma INTEGER PRIMARY KEY auto_increment,
id_responsavel INTEGER NOT NULL,
nome_do_curso VARCHAR(50) NOT NULL,
dia VARCHAR(50) NOT NULL,
hora VARCHAR(50) NOT NULL,
carga_horaria_total VARCHAR(50) NOT NULL,
tolerancia VARCHAR(50) NOT NULL,
modalidade VARCHAR(50) NOT NULL,
turma_tag VARCHAR(50) NOT NULL,
FOREIGN KEY (id_responsavel) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS horario(
id_horario INTEGER PRIMARY KEY auto_increment,
horario_id_turma INTEGER NOT NULL,
dia_da_semana VARCHAR(20) NOT NULL,
horario_inicio TIME NOT NULL,
horario_termino TIME NOT NULL,
FOREIGN KEY (horario_id_turma) REFERENCES turma(id_turma)
);

CREATE TABLE IF NOT EXISTS alunos(
id_aluno INTEGER PRIMARY KEY auto_increment,
alunos_id_turma INTEGER NOT NULL,
alunos_id_user INTEGER NOT NULL,
presenca INTEGER DEFAULT '0' NOT NULL,
FOREIGN KEY (alunos_id_turma) REFERENCES turma(id_turma),
FOREIGN KEY (alunos_id_user) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS userComplemento(
id_complemento INTEGER PRIMARY KEY auto_increment,
id_do_user INTEGER NOT NULL,
tag VARCHAR(20) NOT NULL,
profissao VARCHAR(40) NOT NULL,
funcao VARCHAR(30) NOT NULL,
superentendenciaDaSUBPAV VARCHAR(20) NOT NULL,
CAP VARCHAR(20) NOT NULL,
unidadeBasicaDeSaude VARCHAR(40) NOT NULL,
FOREIGN KEY (id_do_user) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS alunoApoiador(
id_aluno INTEGER PRIMARY KEY auto_increment,
apoiador_id_turma INTEGER NOT NULL,
apoiador_id_user INTEGER NOT NULL,
FOREIGN KEY (apoiador_id_turma) REFERENCES turma(id_turma),
FOREIGN KEY (apoiador_id_user) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS aula(
id_aula INTEGER PRIMARY KEY auto_increment,
aula_id_turma INTEGER NOT NULL,
inicio INTEGER NOT NULL,
termino INTEGER NOT NULL,
nome VARCHAR(20) NOT NULL,
FOREIGN KEY (aula_id_turma) REFERENCES turma(id_turma)
);

CREATE TABLE IF NOT EXISTS presenca(
id_presenca INTEGER PRIMARY KEY auto_increment,
id_do_user INTEGER NOT NULL,
id_da_aula INTEGER NOT NULL,
horario_da_presenca INTEGER NOT NULL,
FOREIGN KEY (id_do_user) REFERENCES user(id),
FOREIGN KEY (id_da_aula) REFERENCES aula(id_aula)
);
--SELECT (strftime('%s','2004-01-01 02:34:56'));
--select strftime('%s','now') - 10800;

