--turma_id_user = professor
CREATE TABLE turma(
id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
turma_id_professor INTEGER NOT NULL,
codigo VARCHAR(50) NOT NULL,
curso VARCHAR(50) NOT NULL,
aulas INTEGER DEFAULT '0' NOT NULL,
FOREIGN KEY (turma_id_professor) REFERENCES user(id)
);

CREATE TABLE horario(
id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
horario_id_turma INTEGER NOT NULL,
dia_da_semana VARCHAR(20) NOT NULL,
horario_inicio TIME NOT NULL,
horario_termino TIME NOT NULL,
FOREIGN KEY (horario_id_turma) REFERENCES turma(id_turma)
);

CREATE TABLE alunos(
id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
alunos_id_turma INTEGER NOT NULL,
alunos_id_user INTEGER NOT NULL,
presenca INTEGER DEFAULT '0' NOT NULL,
FOREIGN KEY (alunos_id_turma) REFERENCES turma(id_turma),
FOREIGN KEY (alunos_id_user) REFERENCES user(id)
);

