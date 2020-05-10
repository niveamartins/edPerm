from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://bd:L4bn3t@localhost:3306/EdPermanente')

Session = sessionmaker(bind=engine)

def get_session():
    try:
        return Session()
    except:
        print("deu merda")