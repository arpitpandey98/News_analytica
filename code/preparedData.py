import pandas as pd
from collections import Counter
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS 

class Data:

    def __init__(self, path="news_summary.csv"):
        self.df = pd.read_csv(path,encoding='latin1',parse_dates=['date'])
        self.df['month'] = pd.DatetimeIndex(self.df['date']).month
        self.df['day'] = pd.DatetimeIndex(self.df['date']).day
        self.df['year'] = pd.DatetimeIndex(self.df['date']).year

    def getHeadingCount(self):
        var=Counter(" ".join(self.df["headlines"]).split()).most_common(50)
        top_50_words=[item[0] for item in var]
        top_50_word_occurances=[item[1] for item in var]
        return pd.DataFrame(top_50_word_occurances, top_50_words)
        
    def getTextCount(self):
        var=Counter(" ".join(self.df["text"]).split()).most_common(50)
        return pd.DataFrame([item[1] for item in var], [item[0] for item in var])
    
    def getAuthorwiseSentiment(self):
        authors=self.df.author.unique()
        author_text=[]

        for author in authors:
            author_text.append(' '.join(self.df.loc[self.df.author==author].headlines.values))
        sentiment={}
        for text in author_text:
            blob=TextBlob(text)
            if(blob.sentiment.polarity>0):
                if("positive" in sentiment):
                    sentiment["positive"] += 1
                else:
                    sentiment["positive"]=1
            elif(blob.sentiment.polarity==0):
                if("neutral" in sentiment):
                    sentiment["neutral"] += 1
                else:
                    sentiment["neutral"]=1
            else:
                if("negative" in sentiment):
                    sentiment["negative"] += 1
                else:
                    sentiment["negative"]=1

        return pd.DataFrame(sentiment.values(), sentiment.keys())
    
    def getHeadingSentiment(self):
        sentiment={}.fromkeys(['positive', 'negative', 'neutral'], 0)
        for headline in self.df.headlines.values:
            blob = TextBlob(headline)
            var=blob.sentiment.polarity
            if(var>0):
                sentiment['positive'] +=1
            elif(var==0):
                sentiment['neutral'] +=1
            else:
                sentiment['negative'] +=1
            
        return pd.DataFrame(sentiment.values(), sentiment.keys())

    def getSummarySentiment(self):
        sentiment={}.fromkeys(['positive', 'negative', 'neutral'], 0)
        for headline in self.df.text.values:
            blob = TextBlob(headline)
            var=blob.sentiment.polarity
            if(var>0):
                sentiment['positive'] +=1
            elif(var==0):
                sentiment['neutral'] +=1
            else:
                sentiment['negative'] +=1
            
        return pd.DataFrame(sentiment.values(), sentiment.keys())


    def getDatewiseNews(self):
        return self.df.groupby("date").count().author

    def getWordCloud(self):
        comment_words = '' 
        stopwords = set(STOPWORDS) 
        
        # iterate through the csv file 
        for val in self.df.headlines: 
            
            # typecaste each val to string 
            val = str(val) 
        
            # split the value 
            tokens = val.split() 
            
            # Converts each token into lowercase 
            for i in range(len(tokens)): 
                tokens[i] = tokens[i].lower() 
            
            comment_words += " ".join(tokens)+" "
        return WordCloud(width = 800, height = 800, 
                        background_color ='black', 
                        stopwords = stopwords, 
                        min_font_size = 10).generate(comment_words) 


    def getMonthSentiments(self, which):
        months=self.df.month.unique()

        month_wise_sentiment = []

        for month in months:
            sentiment = {}.fromkeys(['pos', 'neu', 'neg'], 0)
            for head in self.df[self.df['month']==month][which].values:
                pol = TextBlob(head).sentiment.polarity

                if pol>0:
                    sentiment['pos']+=1
                elif pol<0:
                    sentiment['neg']+=1
                else:
                    sentiment['neu']+=1
            month_wise_sentiment.append(sentiment)

        months_names = ['August', 'July', 'February', 'January', 'December', 'June', 'May', 'April', 'March']

        return [pd.DataFrame({'pos':[dic['pos'] for dic in month_wise_sentiment]}, index = months_names),
                pd.DataFrame({'neg':[dic['neg'] for dic in month_wise_sentiment]}, index = months_names),
                pd.DataFrame({'neu':[dic['neu'] for dic in month_wise_sentiment]}, index = months_names)]


    def getAuthorSentiments(self, which):
        authors=self.df.author.unique()

        month_wise_sentiment = []

        for author in authors:
            sentiment = {}.fromkeys(['pos', 'neu', 'neg'], 0)
            for head in self.df[self.df['author']==author][which].values:
                pol = TextBlob(head).sentiment.polarity

                if pol>0:
                    sentiment['pos']+=1
                elif pol<0:
                    sentiment['neg']+=1
                else:
                    sentiment['neu']+=1
            month_wise_sentiment.append(sentiment)

        return [pd.DataFrame({'pos':[dic['pos'] for dic in month_wise_sentiment]}, index = authors),
                pd.DataFrame({'neg':[dic['neg'] for dic in month_wise_sentiment]}, index = authors),
                pd.DataFrame({'neu':[dic['neu'] for dic in month_wise_sentiment]}, index = authors)]


    def getYearSentiments(self, which):
        years=self.df.year.unique()

        year_wise_sentiment = []

        for year in years:
            sentiment = {}.fromkeys(['pos', 'neu', 'neg'], 0)
            for head in self.df[self.df['year']==year][which].values:
                pol = TextBlob(head).sentiment.polarity

                if pol>0:
                    sentiment['pos']+=1
                elif pol<0:
                    sentiment['neg']+=1
                else:
                    sentiment['neu']+=1
            year_wise_sentiment.append(sentiment)


        return [pd.DataFrame({'pos':[dic['pos'] for dic in year_wise_sentiment]}, index = years),
                pd.DataFrame({'neg':[dic['neg'] for dic in year_wise_sentiment]}, index = years),
                pd.DataFrame({'neu':[dic['neu'] for dic in year_wise_sentiment]}, index = years)]

