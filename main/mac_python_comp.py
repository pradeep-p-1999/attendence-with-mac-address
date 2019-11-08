#!/usr/bin/env python
# coding: utf-8

# In[415]:


import pandas as pd


# In[416]:


test_x='test1.csv'
check_x='check.csv'


# In[417]:


test_df=pd.read_csv(test_x,header=0,encoding = 'unicode_escape')
check_df=pd.read_csv(check_x,header=0,encoding = 'unicode_escape')


# In[418]:


x_df = ((test_df[test_df['Ping'] != '[n/a]' ])) 


# In[419]:


xx_df=x_df.reset_index(drop=True)


# In[420]:


xxx_df=xx_df.join(check_df)


# In[421]:


xxx_dfx=xxx_df


# In[422]:


xxx_dfx=xxx_dfx.dropna()


# In[430]:


s=xxx_dfx['mac_adres']
s=len(s)
s=s


# In[431]:



d=xxx_df['MAC Address']
d=len(d)
d=d-1


# In[432]:


col_name=['present']
x_c=pd.DataFrame(columns=col_name)


# In[435]:


fg=[]
for i in range(s):
    for j in range(d):
        a =  xxx_df.iloc[i]['mac_adres'] == xxx_df.iloc[j]['MAC Address']
        
        if a == True:
            b=xxx_dfx.iloc[i]['stud_name']
            fg.append(b)
print(fg)


# In[ ]:





# In[ ]:




