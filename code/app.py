from sqlalchemy.orm import sessionmaker
from python_orm import Visualizations
from sqlalchemy import create_engine
import streamlit as st
import os
import pandas as pd
import numpy as np

from plot import *
from preparedData import Data

sidebar = st.sidebar
data = Data()



def showWorldCloud():
    st.header('Top 50 Words in News')
    st.image('figures/wordcloud.png', use_column_width=True)
    st.text("Here is the Description")

st.title('News Analytica')
st.image('logo.jpg')
st.markdown("---")
sidebar = st.sidebar

def viewData():
    st.header('Data Used in Project')
    dataframe = pd.read_csv('news_summary.csv', encoding="latin1")

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object' : 'Categorical', 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analyseAuthors():

    with st.spinner("Loading Plot..."):
        st.header('Author Analysis')
        occ = st.selectbox(
            options=['News Headlines Text', 'News Summary Text'], label="Select Option for Authorwise Sentiments")
        if occ == 'News Headlines Text':
            dataToPlot = data.getAuthorSentiments('headlines')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))
        elif occ == 'News Summary Text':
            dataToPlot = data.getAuthorSentiments('text')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))



def analyseSentiments():
    with st.spinner("Loading Plot..."):

        st.header('Word Analysis\n')
        occ = st.selectbox(
            options=['News Headlines', 'News Summary'], label="Select the Analysis")
        if occ == 'News Headlines':
            dataToPlot = data.getHeadingCount()
            st.plotly_chart(
                plotBar(dataToPlot, "Most Word Occurences", "Word", "Word Count"))
        elif occ == 'News Summary':
            dataToPlot = data.getTextCount()
            st.plotly_chart(
                plotBar(dataToPlot, "Most Word Occurences", "Word", "Word Count"))
        st.markdown("---")

        ch = st.selectbox(options=['Authorwise Sentiment', 'News Heading Text Sentiment',
                                'News Summary Text Sentiment'], label="Select the Analysis")
        if ch == 'Authorwise Sentiment':
            st.plotly_chart(plotBar(data.getAuthorwiseSentiment(
            ), "Author Wise News Sentiments", "Polarity", "No. of News"))
        elif ch == 'News Heading Text Sentiment':
            st.plotly_chart(plotBar(data.getHeadingSentiment(),
                                    " News Heading Sentiments", "Polarity", "No. of News"))
        elif ch == 'News Summary Text Sentiment':
            st.plotly_chart(plotBar(data.getSummarySentiment(),
                                    " News Summary Sentiments", "Polarity", "No. of News"))

    


def analyseTimeline():

    with st.spinner("Loading Plot..."):

        st.header('Timeline Anaysis\n')
        st.plotly_chart(plotBar(data.getDatewiseNews(),
                                "Timeline of No. of News Published", "Date", "No. of News"))

        st.markdown("---")

        st.header('Month wise Sentiments')
        occ = st.selectbox(
            options=['News Headlines Text', 'News Summary Text'], label="Select Option for Monthwise Sentiments")
        if occ == 'News Headlines Text':
            dataToPlot = data.getMonthSentiments('headlines')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))
        elif occ == 'News Summary Text':
            dataToPlot = data.getMonthSentiments('text')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))

        st.markdown("---")

        st.header('Year wise Sentiments')
        occ = st.selectbox(
            options=['News Headlines Text', 'News Summary Text'], label="Select Option for Yearwise Sentiments")
        if occ == 'News Headlines Text':
            dataToPlot = data.getYearSentiments('headlines')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))
        elif occ == 'News Summary Text':
            dataToPlot = data.getYearSentiments('text')
            st.plotly_chart(plotGroupedBar(dataToPlot, [
                        "Positive", "Negative", "Neutral"], 'title', 'xlabel', 'ylabel', ['green', 'indianred', 'lightblue']))



def generateWordCloud():

    with st.spinner("Loading Plot..."):

        st.header('New Headlines text WordCloud')
        st.image("../figures/wordcloud.png")

        st.markdown("---")

        st.header('New Summary text WordCloud')
        st.image("../figures/wordcloud1.png")


choice = sidebar.selectbox(options=['View Database', 'Analyse Authors',
                                    'Overall Sentiment Analysis', 'Timeline Analysis', 'WordCloud'], label="Select an option")

if choice == 'View Database':
    viewData()
elif choice == 'Analyse Authors':
    analyseAuthors()
elif choice == 'Overall Sentiment Analysis':
    analyseSentiments()
elif choice == 'Timeline Analysis':
    analyseTimeline()
elif choice == 'WordCloud':
    generateWordCloud()
