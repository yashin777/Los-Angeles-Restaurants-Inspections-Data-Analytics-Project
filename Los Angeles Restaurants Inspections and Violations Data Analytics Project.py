#!/usr/bin/env python
# coding: utf-8

# # Los Angeles Restaruants Violations Data Analytics Project

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df1=pd.read_csv("inspections.csv")
df2=pd.read_csv("violations.csv")


# In[60]:


df1


# In[61]:


df1.loc[df1['score']==100]


# In[62]:


df1.describe()


# In[4]:


#Analyzing grade reported
df1['grade'].value_counts()


# In[64]:


df1['score']


# In[65]:


df1['score'].mode()


# In[66]:


df1['score'].min()


# In[5]:


df1['score'].max()


# In[67]:


df1.score.value_counts()


# In[68]:


df2


# In[6]:


gradeA=df1['grade']=='A'
gradeA


# In[91]:


df2['violation_description'].unique()


# In[71]:


df2['violation_code'].value_counts()


# In[72]:


df1.describe()


# In[73]:


df1.isnull().sum()
# program name has 402 null values


# In[74]:


df1['program_name']


# In[75]:


#let's see the 402 null values
df1[df1['program_name'].isna()]


# In[76]:


#replace the null values with 'none'
df1.fillna('None',inplace=True)


# In[77]:


df1.isnull().sum()


# In[78]:


df2.isnull().sum()


# # Apply the inner join to both tables to analyze

# In[11]:


df_inner=pd.merge(df1,df2,on='serial_number',how='inner')
pd.set_option('display.max_columns', None)


# In[12]:


df_inner


# In[13]:


df_inner.isnull().sum()


# In[14]:


grade_results=df_inner['grade'].value_counts()
grade_results.to_csv('grade_results.csv')


# In[15]:


grade_results


# In[20]:


violation_descriptions=df_inner['violation_description'].value_counts()
violation_descriptions.to_csv('violation_descriptions')


# In[19]:


violation_descriptions


# In[17]:


new_df=df_inner.loc[:,['activity_date','facility_city','facility_name','facility_state','grade','violation_description','violation_code']]
new_df


# In[18]:


# created a dataframe for only in the city of Los Angeles
LA_result=new_df.loc[new_df['facility_city']=='LOS ANGELES']
LA_result


# In[21]:


# facility_name that includes highest violation reported
LA_result['facility_name'].value_counts()


# In[22]:


LA_result['facility_name'].mode()


# In[23]:


Dodger=LA_result.loc[LA_result['facility_name']=='DODGER STADIUM']


# In[24]:


Dodger['violation_code'].value_counts()


# In[25]:


Staples_center=new_df.loc[new_df['facility_name']=='STAPLES CENTER (LEVY)']
Staples_center.to_csv('Staples_center.csv')


# In[26]:


LA_Coliseum=new_df.loc[new_df['facility_name']=='LA COLISEUM']
LA_Coliseum.to_csv('LA_Coliseum.csv')


# In[27]:


Dodger.to_csv('Dodger.csv')


# In[ ]:


LA_result['grade']=='A'


# In[103]:


LA_result.to_csv('LA_result.csv') 


# In[100]:


new_df.to_csv('new_df.csv')


# In[31]:


result1=new_df.loc[new_df['grade']=='A']
result1.to_csv('result1.csv')
result1


# In[49]:


result1['violation_description'].mode()


# In[90]:


len(result1)


# In[47]:


result2=new_df.loc[new_df['grade']=='B']
result2


# In[89]:


len(result2)


# In[94]:


result3=new_df.loc[new_df['grade']=='C']
result3


# In[95]:


len(result3)


# In[46]:


result2['violation_description'].value_counts()


# In[43]:


violation_description.to_csv('violation_description.csv')


# In[34]:


# violation_code F044 has the highest count


# In[20]:


df_inner['violation_code'].value_counts()


# In[31]:


df_inner['score'].min()


# In[32]:


df_inner['score'].max()


# In[ ]:


df_inner.loc[]


# # Which facility address has the violation code F044

# In[22]:


common_violation_code=df_inner.loc[df_inner['violation_code']=='F044']
common_violation_code


# In[23]:


df_inner.isnull().sum()


# In[24]:


df_inner['violation_description'].value_counts()


# In[81]:


df_inner.to_csv('inner_join.csv')

