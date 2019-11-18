#!/usr/bin/env python
# coding: utf-8

# In[106]:


from datetime import date
today = date.today()


# In[107]:


import pandas as pd

test_x='test1.csv'
check_x='check.csv'

test_df=pd.read_csv(test_x,header=0,encoding = 'unicode_escape')
check_df=pd.read_csv(check_x,header=0,encoding = 'unicode_escape')

x_df = ((test_df[test_df['Ping'] != '[n/a]' ])) 

xx_df=x_df.reset_index(drop=True)

xxx_df=xx_df.join(check_df)

xxx_dfx=xxx_df

xxx_dfx=xxx_dfx.dropna()


s=xxx_dfx['mac_adres']
s=len(s)
s=s
d=xxx_df['MAC Address']
d=len(d)
d=d-1
col_name=['names']
x_c=pd.DataFrame(columns=col_name)

fg=[]
for i in range(s):
    for j in range(d):
        a =  xxx_df.iloc[i]['mac_adres'] == xxx_df.iloc[j]['MAC Address']
        
        if a == True:
            b=xxx_dfx.iloc[i]['stud_name']
            fg.append(b)
print(fg)


# In[136]:


customer_data_file = 'attendence_mac.xlsx'
name_df = pd.read_excel(customer_data_file,
sheetname=0,
header=0,
index_col=False,
keep_default_na=True
)


# In[139]:


f=name_df['names']
f=len(f)
f=f
h=len(fg)


# In[140]:


x_c['names_fg']=fg


# In[141]:


l=[]
for i in range(f):
    count=0
    for j in range(h):
        a= name_df.iloc[i]['names'] == x_c.iloc[j]['names_fg']
        if a == True:
            count=count+1
    if count ==1:
        l.append('p')
        
    else:
        l.append('ab')
                
            


# In[142]:



name_df[today]=l


# In[143]:


final=name_df


# In[ ]:





# In[144]:


final.to_excel(r'attendence_mac.xlsx', index=False)


# In[ ]:




