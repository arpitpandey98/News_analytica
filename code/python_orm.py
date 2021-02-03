import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
now = datetime.now()

Base=declarative_base()

#main code starts

class Visualizations(Base):
    __tablename__ ="userinputs"
     
    id=Column(Integer,primary_key=True)
    path=Column(String)
    date=Column(String)
    name=Column(String)

if __name__=="__main__":


    engine= create_engine('sqlite:///project_db.sqlite3')
    Base.metadata.create_all(engine)
    Session =sessionmaker(bind=engine)
    session =Session()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    name
    viz = Visualizations(path = 'figure3.png', date = current_time, name = "Visualization 1")
    session.add(viz)
    session.commit()