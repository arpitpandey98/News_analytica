import pandas as pd
from collections import Counter

class Data:

    def __init__(self, path="E:\\padh le\\project maj\\news_summary.csv"):
        self.df = pd.read_csv(path,encoding='latin1',parse_dates=['date'])

    def getHeadingCount(self):
        var=Counter(" ".join(self.df["headlines"]).split()).most_common(50)
        top_50_words=[item[0] for item in var]
        top_50_word_occurances=[item[1] for item in var]
        return pd.DataFrame({'top_50_words' : top_50_words , 'top_50_word_occurances' : top_50_word_occurances}),'top_50_words',  'top_50_word_occurances'