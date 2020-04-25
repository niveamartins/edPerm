import datetime


def registerDateTime():
    tempo = str(datetime.datetime.now()).split(' ')
    DataeHoraDeCriacao = tempo[0]+' '+tempo[1].split('.')[0]
    return DataeHoraDeCriacao