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

    viz = Visualizations(path = 'wordcloud.png', date = current_time, name = "WORD CLOUD")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure1.png', date = current_time, name = "MOST OCCURING WORD IN HEADING")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure2.png', date = current_time, name = "MOST OCCURING WORD IN TEXT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure3.png', date = current_time, name = "OVERALL SENTIMENT OF AUTHORS")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure4.png', date = current_time, name = "DATE WISE AUTHOR NEWS COUNT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure5.png', date = current_time, name = "OVERALL HEADING OF SENTIMENT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure6.png', date = current_time, name = "OVERALL TEXT OF SENTIMENT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure7.png', date = current_time, name = "WORD COUNT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure8.png', date = current_time, name = "MONTH WISE SENTIMENT OF HEADLINES")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure9.png', date = current_time, name = "MONTH WISE SENTIMENT OF TEXT")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure10.png', date = current_time, name = "AUTHOR WISE SENTIMENT OF HEADING(TOP 10)")
    session.add(viz)
    session.commit()
    
    viz = Visualizations(path = 'figure12.png', date = current_time, name = "AUTHOR WISE SENTIMENT OF TEXT(TOP 10)")
    session.add(viz)
    session.commit()
    viz = Visualizations(path = 'figure13.png', date = current_time, name = "YEAR WISE SENTIMENT OF HEADLINES")
    session.add(viz)
    session.commit()
    viz = Visualizations(path = 'figure14.png', date = current_time, name = "YEAR WISE SENTIMENT OF TEXT")
    session.add(viz)
    session.commit()
    
    