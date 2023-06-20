#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\ADMIN\Downloads\Netflix Dataset (2).csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.size


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data.info()


# Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
# 
# duplicate()

# In[11]:


data.head()


# In[12]:


data.shape


# In[14]:


data[data.duplicated()]


# In[16]:


data.drop_duplicates(inplace= True)


# In[17]:


data.shape


# Task. 2) Is there any Null Value present in any column ? Show with Heat-map.

# Isnull()

# In[18]:


data.head()


# In[19]:


data.isnull()


# In[20]:


data.isnull().sum()


# Seaborn library (heat-map)

# In[21]:


sns.heatmap(data.isnull())


# Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?

# Isin()

# In[31]:


data.head()


# In[26]:


data[data["Title"].isin(['House of cards'])]


# str.contains()

# In[30]:


data[data['Title'].str.contains('House of cards')]


# Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# dtype()

# In[33]:


data.dtypes


# to_datetime

# In[35]:


data['Date_N']=pd.to_datetime(data['Release_Date'])


# In[36]:


data.head()


# In[37]:


data.dtypes


# dt.year.value_count()

# In[38]:


data['Date_N'].dt.year.value_counts()


# Bar Graph

# In[40]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# groupby()

# In[41]:


data.head(2)


# In[46]:


data.groupby('Category').Category.count()


# Countplot()

# In[47]:


sns.countplot(data['Category'])


# Q. 4) Show all the Movies that were released in year 2000.

# creating new column

# In[49]:


data.head(2)


# In[52]:


data['year']=data['Date_N'].dt.year


# In[53]:


data.head(2)


# Filtering

# In[58]:


data[ (data['Category']=='Movie') & (data['year']==2000) ]


# In[59]:


data[ (data['Category']=='Movie') & (data['year']==2020) ]


# In[60]:


data.head(2)


# Q. 5) Show only the Titles of all TV Shows that were released in India only.

# In[62]:


data[ (data['Category']=='TV Show') & (data['Country']=="India") ] ["Title"]


# Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[63]:


data.head(2)


# In[65]:


data['Director'].value_counts().head(10)


# Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# Filtering(And.Or Operators)

# In[66]:


data.head(2)


# In[69]:


data[(data['Category']=='Movie')& (data['Type']=="Comedies")]


# In[70]:


data[(data['Category']=='Movie')& (data['Type']=="Comedies")|(data['Country']=='United Kingdom')]


# Q. 8) In how many movies/shows, Tom Cruise was cast ?

# In[71]:


data.head(2)


# In[72]:


data[data['Cast']=='Tom Cruise']


# Str.contains()
# 

# Creating new data-frame

# In[73]:


data_new=data.dropna()


# In[74]:


data_new.head(2)


# In[76]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# Q. 9) What are the different Ratings defined by Netflix ?

# nunique()

# In[81]:


data.head(2)


# In[79]:


data['Rating'].nunique()


# Unique

# In[80]:


data['Rating'].unique()


# Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?

# In[82]:


data.head(2)


# In[83]:


data[(data['Category']=="Movie")& (data["Rating"]=='TV-14')].shape


# In[85]:


data[(data['Category']=="Movie")& (data["Rating"]=='TV-14')& (data['Country']=='Canada')].shape


# Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?

# In[86]:


data.head(2)


# In[88]:


data[(data['Category']=='TV Show')& (data['Rating']=='R')&(data['year']>2018)]


# Q. 10) What is the maximum duration of a Movie/Show on Netflix ?

# In[89]:


data.head(2)


# In[90]:


data.Duration.unique()


# In[91]:


data.Duration.dtypes


# str.split()

# In[92]:


data.head(2)


# In[94]:


data[["Minutes","Unit"]]= data["Duration"].str.split(" ",expand = True)


# In[95]:


data.head(2)


# max()

# In[96]:


data["Minutes"].max()


# min()

# In[97]:


data["Minutes"].min()


# In[98]:


data["Minutes"].mean()


# In[99]:


data.dtypes


# Q. 11) Which individual country has the Highest No. of TV Shows ?

# In[100]:


data.head(2)


# In[101]:


data_tvshow= data[data['Category']=="TV Show"]


# In[102]:


data_tvshow.head(2)


# In[103]:


data_tvshow.Country.value_counts()


# In[104]:


data_tvshow.Country.value_counts().head(1)


# Q. 12) How can we sort the dataset by Year ?

# In[105]:


data.head(2)


# In[106]:


data.sort_values(by = "year")


# In[107]:


data.sort_values(by ='year', ascending = False)


# Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.

# In[ ]:





# Category is 'Movie' and Type is 'Dramas'

# or

# Category is 'TV Show' & Type is 'Kids' TV'.

# In[108]:


data.head(2)


# In[109]:


data [ (data['Category']=="Movie")& (data['Type']== "Dramas")].head(2)


# In[110]:


data[(data['Category']=='Tv show')& (data['Type']=="kids' TV")]


# In[111]:


(data['Category']=="Movie")& (data['Type']== "Dramas") | (data['Category']== 'Tv Show')& (data['Type']=="kids' TV")


# In[ ]:




