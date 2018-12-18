#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The myReduceSum function works like reduce function for finding sum of all given values
import sys
sys.setrecursionlimit(100)
#this myReduce function finds the sum of all the numbers upto the given number. eg Number:3 gives 1+2+3=6 as result
def myReduceSum(n):
    if n==1:
        return 1
    else:
        return (n)+myReduceSum(n-1)

sumRange = 7
print(myReduceSum(sumRange-1))


# In[2]:


# The myReduceSum function works like reduce function for finding sum of all given values
from functools import reduce
lst =range(7) 
reduce(lambda x,y: x+y,lst)


# In[18]:


# The myfilterList function works like filter function for given list of values, which returns all even values
def myFilterEvenList(rangeLimit):
    evenList = []
    for num in range(rangeLimit):
        if num%2==0:
            evenList.append(num)
    return evenList

rangeLimit = 20
print(myFilterEvenList(rangeLimit))


# In[4]:


#2.Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]



myLst = [letter for letter in 'ACADGILD']
print(myLst)


# In[5]:


myLst = [letter*i  for letter in 'xyz' for i in list(range(1,5))]
print(myLst)


# In[6]:



myLst = [letter*i for i in list(range(1,5)) for letter in 'xyz']
print(myLst)


# In[7]:


myLst = [ list(range(x,x+y)) for x in range(2,6) for y in range(4,5) ]
print(myLst)


# In[8]:


myLst = [ (x,y) for x in range(1,4) for y in range(1,4) ]
print(myLst)


# In[9]:


#Implement a function longestWord() that takes a list of words and returns the longest one

def longestWord(lstOfWords):
    maxLen = 0
    maxWord = ''
    for word in lstOfWords:
        if len(word)>maxLen:
            maxLen = len(word)
            maxWord = word
    return word

words = ['Hi','Hello','how','are','acadgild']
print('the longest word is: ', longestWord(words))


# In[ ]:




