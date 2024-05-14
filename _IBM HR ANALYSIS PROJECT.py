#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("HR-Employee-Attrition 1.csv")
df


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


#Education field is having 2 null values and job role having 1 null value


# In[ ]:





# In[7]:


df[df.isnull().any(axis=1)]


# In[ ]:





# In[ ]:





# In[8]:


df['EducationField']=df['EducationField'].fillna('Other')


# In[9]:


df[df.isnull().any(axis=1)]


# In[10]:


df['JobRole']=df['JobRole'].fillna(method='bfill')


# In[11]:


df[df.isnull().any(axis=1)]


# In[ ]:





# In[12]:


df.duplicated()


# # Deal with outliers

# In[13]:


#Box plot, Z score, Domain knowledge is needed


# In[14]:


df1=df.copy()


# In[15]:


df1


# In[16]:


from scipy import stats


# In[17]:


z_score=stats.zscore(df['Age'])
thresold=3
outliers= (z_score>thresold) | (z_score<-thresold)


# In[18]:


outliers


# In[19]:


df1[outliers==True]


# In[20]:


import seaborn as sns
sns.boxplot(df['Age'])


# In[21]:


import numpy as np


# In[22]:


numerical_columns=df1.select_dtypes(include=['number']).columns.tolist()
numerical_columns


# In[23]:


categorical_columns=df1.select_dtypes(include=['object']).columns.tolist()
categorical_columns


# In[24]:


import matplotlib.pyplot as plt


# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

fig, axes = plt.subplots(nrows=len(numerical_columns), ncols=1, figsize=(10, 6*len(numerical_columns)))
for i, col in enumerate(numerical_columns):
    sns.boxplot(x=df[col], ax=axes[i])
    z_score = stats.zscore(df[col])
    threshold = 3
    outliers = (z_score > threshold) | (z_score < -threshold)
    df = df[~outliers]

plt.tight_layout()
plt.show()


# In[26]:


df1


# In[ ]:





# In[27]:


df1.to_csv('cleaned_data.csv',index=False)


# In[ ]:





# In[30]:


get_ipython().system('pip install mysql-connector-python')
import mysql.connector 
from mysql.connector import Error


# In[33]:


data_mapping={'int64':'INT','object':'TEXT'}


# In[36]:


import mysql.connector
from mysql.connector import Error

# Assuming df2 is defined somewhere in your code

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='new_hrdb',
        user='root',
        password='Bhavna@2420'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version:", db_info)
        cursor = connection.cursor()

        columns = ",".join([f"{col} {data_mapping[str(df1[col].dtype)]}" for col in df1.columns])
        cursor.execute(f'create table if not exists employee ({columns})')

        data = [tuple(i) for i in df1.values]
        cursor.executemany(f"insert into employee values ({','.join(['%s']* len(df1.columns))})", data)

        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into employee table")

except Error as e:
    print("Something went wrong:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




