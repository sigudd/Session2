#!/usr/bin/env python
# coding: utf-8

# In[5]:


num=input("enter the Numbers with ',' separated :")
listNum=[num]
print(listNum)


# In[26]:


row=5
num=0
for i in range(0,row):
    for j in range(0, i+1):
        print("*",end="")
    print("\r")
for i in range(row,0,-1):
    for j in range(0, i-1):
        print("*",end="")
    print("\r")    


# In[29]:


name=input("Enter a name")
rvrs=name[::-1]
print(rvrs)


# In[35]:


print("WE, THE PEOPLE OF INDIA,\n    having solemnly resolved to constitute India into a SOVEREIGN,!\n\tSOCIALIST,SECULAR,DEMOCRATIC REPUBLIC\n\tand to secure to all its citizens")


# In[ ]:




