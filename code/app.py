from sqlalchemy.orm import sessionmaker
from python_orm import Visualizations
from sqlalchemy import create_engine
import streamlit as st

engine =create_engine('sqlite:///project_db.sqlite3')
Session =sessionmaker(bind=engine)
sess =Session()


data = sess.query(Visualizations).all()
print(data)

for d in data:
    st.title(d.name)
    st.image('../figures/'+d.path)