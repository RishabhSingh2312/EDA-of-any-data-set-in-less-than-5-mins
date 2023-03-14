#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install pandas')


# In[19]:


##!pip install pandas-profiling


# In[20]:


import pandas as pd
from pandas_profiling import ProfileReport


# In[21]:


# Reading a dataframe
df= pd.read_csv("housing.csv")


# In[22]:


df


# In[23]:


#Generate a report
profile=ProfileReport(df)
profile.to_file(output_file="housing.html")


# In[24]:


profile


# In[ ]:




