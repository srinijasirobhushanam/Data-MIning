
# coding: utf-8

# In[1]:


import json
import csv
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = []
with open('/home/ssirobh/data_mining/review.json') as f:
    for line in f:
        data.append(json.loads(line))


# In[3]:


len(data)


# In[4]:




data[0]



# In[5]:


reviewid = []
businessid= []
userid = []
stars = []
text = []
date = []

for entry in range(0, len(data)):     
    reviewid.append(data[entry]['review_id'])
    businessid.append(data[entry]['business_id'])
    userid.append(data[entry]['user_id'])
    stars.append(data[entry]['stars'])
    text.append(data[entry]['text'])
    date.append(data[entry]['date'])


# In[6]:


data = {'review_id':reviewid,'business_id':businessid,'user_id':userid,'stars':stars,'text':text,'date':date}
review_data  = pd.DataFrame(data)


# In[7]:


review_data.head()


# In[8]:


review_data.to_csv('review_data.csv')


# In[39]:


data2 = []
with open('/home/ssirobh/data_mining/business.json') as f:
    for line in f:
        data2.append(json.loads(line))
len(data2)
data2[1]


# In[40]:


business_id = []
city = []
state = []
stars = []
review_count = []
categories = []
postal_code = []
latitude = []
longitude = []
pricerange = []
is_open = []
name = []


for entry in range(0, len(data2)): 
        business_id.append(data2[entry]['business_id'])
        name.append(data2[entry]['name'])
        city.append(data2[entry]['city'])
        state.append(data2[entry]['state'])
        stars.append(data2[entry]['stars'])
        postal_code.append(data2[entry]['postal_code'])
        review_count.append(data2[entry]['review_count'])
        categories.append(data2[entry]['categories'])
        latitude.append(data2[entry]['latitude'])
        longitude.append(data2[entry]['longitude'])
        is_open.append(data2[entry]['is_open'])


# In[41]:



data2 = {'business_id ':business_id,'name':name,'city':city,'state':state,'stars':stars,'review_count':review_count,
        'categories':categories,'latitude':latitude,'longitude':longitude,'is_open':is_open,
        'postal_code':postal_code}
business_data  = pd.DataFrame(data2)


# In[42]:


IL = business_data[business_data['state']=='IL']   # PA NV NC IL OH AZ only keep these 6 states 
PA = business_data[business_data['state']=='PA'] 
NV = business_data[business_data['state']=='NV']
NC = business_data[business_data['state']=='NC']
OH = business_data[business_data['state']=='OH']
AZ = business_data[business_data['state']=='AZ']
frame = [IL,PA,NV,NC,OH,AZ]
business_info = pd.concat(frame)


# In[43]:


business = business_info[business_info['is_open']==1]   # only keep restaurants that are open
business.to_csv('business_data.csv')


# In[44]:


df = pd.read_csv('business_data.csv')
len(df)


# In[2]:


# Create review_subset
import pandas as pd 
df = pd.read_csv('business_data.csv')
df.head()

df2 = pd.read_csv('review_data.csv')

df['key'] = df.iloc[:,1]
review = df2[df2['business_id'].isin(df['key'])]  # only keep reviews for restaurants in business_data.csv
review = review.reset_index().iloc[:,2:]


# In[5]:


data3 = []
with open('/home/ssirobh/data_mining/user.json') as f:
    for line in f:
        data3.append(json.loads(line))
len(data3)  


# In[8]:


import json
data3 = []
with open('/home/ssirobh/data_mining/user.json') as f:
    for line in f:
        data3.append(json.loads(line))
len(data3)


# In[9]:


userid = []
average_stars= []
review_count = []
yelping_since = []

for entry in range(0, len(data3)):     
    userid.append(data3[entry]['user_id'])
    average_stars.append(data3[entry]['average_stars'])
    review_count.append(data3[entry]['review_count'])
    yelping_since.append(data3[entry]['yelping_since'])


# In[10]:


data3 = {'user_id':userid ,'average_stars':average_stars,'review_count':review_count,'yelping_since':yelping_since,'review_count':review_count}
user_data  = pd.DataFrame(data3)


# In[11]:


user_data.head(10)


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[18]:


review = pd.read_csv('/home/ssirobh/data_mining/reviewContent.txt',header='None',)

