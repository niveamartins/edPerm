import sys
from utilities.loggers import get_logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.model.Base import Base
from database.model.Model import *

logger = get_logger(sys.argv[0])
logger.info("Estabelecendo conexão com o banco de dados")
engine = create_engine(
    'mysql+pymysql://bd:L4bn3t@localhost:3306/EdPermanente')
Base.metadata.create_all(engine)
logger.info("Inicializando a poll de conexões")
Session = sessionmaker(bind=engine)


def get_session():
    try:
        return Session()
    except:
        logger.error("Não foi possivel criar a conexão")
