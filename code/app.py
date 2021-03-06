from sqlalchemy.orm import sessionmaker
from python_orm import Visualizations
from sqlalchemy import create_engine
import streamlit as st
import os
import pandas as pd
import numpy as np

from plot import linePlot


# basepath = os.path.abspath(os.getcwd())
data=pd.read_csv('news_summary.csv', encoding= "latin1")
st.dataframe(data)

st.plotly_chart(linePlot([]))
# engine =create_engine('sqlite:///project_db.sqlite3')
# Session =sessionmaker(bind=engine)
# sess =Session()

def showWorldCloud():
    st.header('Top 50 Words in News')
    st.image('figures/wordcloud.png', use_column_width=True)
    st.text("Here is the Description")

st.title('News Analytica')
st.sidebar.title('Options')
viz = st.sidebar.button('Visualize')
st.sidebar.button('View Dataset')
# select_value = st.selectbox("What would you like to Visualize?", options = ['Select', 'WordCloud', 'Most Occuring Words'])

# data = sess.query(Visualizations).all()
if viz:
    select_value = st.selectbox("What would you like to Visualize?", options = ['Select', 'WordCloud', 'Most Occuring Words'])

    if select_value=="WordCloud":
        st.header('Top 50 Words in News')
        st.image('figures/wordcloud.png', use_column_width=True)
        st.text("Here is the Description")


# for d in data:
#     st.header(d.name)
#     st.image('figures/'+d.path, use_column_width=True)


