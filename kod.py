
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data= pd.read_csv("N:\Desktop\d.txt")
data.columns=("time","user","comp")


# In[4]:


df=data.head(1000) 


# In[5]:


df['user1'], df['user2'] = df['user'].str.split('U').str
df['comp1'], df['comp2'] = df['comp'].str.split('C').str
df["comp2"] = df["comp2"].astype("int")
df["user2"] = df["user2"].astype("int")
df.head(1000)


# In[6]:


length = len(df.index)
length


# In[8]:


comp = int(input("enter a computer: "))
print(comp)
user = int(input("enter a user: "))
print(user)

#fiding the time of comp&user
for m in range(0,length):
    if comp==df['comp2'][m] and user==df['user2'][m]:
        print(m)
        break


# In[9]:


k=0;
i=0;
for i in range(m+1,length):
    if (df['comp2'][i] == comp):
        print("name of the users that logged into the computer:",df['time'][i],df['user'][i],df['comp'][i])
        k=k+1
print("the number of users that logged in after:",k)

