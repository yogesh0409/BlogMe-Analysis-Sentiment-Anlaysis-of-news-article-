#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[80]:


data =pd.read_excel('E:/Data Analytic Project/BlogMe Sentiment and Keyword Analysis/articles.xlsx')


# In[81]:


data.head(10)


# In[82]:


#information of data
data.info()


# In[83]:


#summary of data
data.describe()


# In[85]:


data.groupby(['source_id'])['article_id'].count()


# In[86]:


#number of reaction by publisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()


# In[87]:


#droping the column

data= data.drop('engagement_comment_plugin_count' ,axis=1)


# In[18]:


#creating the keyword to identify the title 


# In[88]:


length=len(data)
keyword = 'crash'


# In[89]:


keyword_flag =[]
for x in range(0,length):
    heading = data['title'][x]
    try:
        if keyword in heading:
            flag =1 
        else:
            flag =0
    except:
        flag =0
    keyword_flag.append(flag)
            


# In[90]:


def keywordflag(keyword):
    length=len(data)
    keyword_flag =[]
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag =1 
            else:
                flag =0
        except:
            flag =0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag=keywordflag('murder')
            
    
    


# In[91]:


#creating the new column 

data['keyword_flag']=pd.Series(keywordflag)


# In[ ]:


#Sentiment analysis using the vader


# In[92]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[93]:


sent_int =SentimentIntensityAnalyzer()


# In[94]:


text =data['title'][16]


# In[95]:


sent =sent_int.polarity_scores(text)


# In[96]:


sent


# In[97]:


neg = sent['neg']


# In[98]:


pos =sent['pos']


# In[99]:


neu =sent['neu']


# In[ ]:


#analyzing the +ve & -ve & neutral reviews


# In[100]:


title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length=len(data)


# In[101]:


for x in range(0,length):
    try:
        text =data['title'][x]
        sent_int =SentimentIntensityAnalyzer()
        sent =sent_int.polarity_scores(text)
        neg = sent['neg']
        pos =sent['pos']
        neu =sent['neu']
    except:
        neg =0
        pos =0
        neu =0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
    


# In[102]:


title_neg_sentiment =pd.Series(title_neg_sentiment)
title_pos_sentiment =pd.Series(title_pos_sentiment)
title_neu_sentiment =pd.Series(title_neu_sentiment)


# In[104]:


data['Negative'] =title_neg_sentiment
data['Positive'] =title_pos_sentiment
data['Neutral'] =title_neu_sentiment


# In[105]:


data


# In[ ]:


#exporting into excel


# In[107]:


data.to_excel('blogme_clean.xlsx',sheet_name ='blogmedata',index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




