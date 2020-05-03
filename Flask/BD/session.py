from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#TODO: ver as credencias de acesso ao bd com o matheus e raphael
engine = create_engine('mysql://[user]:[senha]@127.0.0.2:3306/EdPermanente')

Session = sessionmaker(bind=engine)

def get_session():
    try:
        return Session()
    except:
        print("deu merda")