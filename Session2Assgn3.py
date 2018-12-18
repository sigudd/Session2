#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Define a lambda function: echo_name echo_name = (lambda ) Call echo_name with parameters ("acadgild",5) result = echo_name ("acadgild",5) Print result print()
echo_name= lambda name1,echo_int:name1*echo_int
result = echo_name("acadgild",5)
print (result)


# In[2]:


#2) Convert temperature in Celsius to Fahrenheit using map() and lambda functions Sample input Celsius = [49.2, 26.5, 47.3, 47.8] Expected Output [120.56, 79.7, 117.14, 118.03999999999999]
Celsius = [49.2, 26.5, 47.3, 47.8]
Fahrenheit = list(map(lambda temp:((float(9)/5)*temp)+32,Celsius))
print(Fahrenheit)


# In[3]:


#3) The function filter(function, list) filters out all the elements of a list, for which the function function returns True. The function filter(f,l) needs a function f as its first argument. f re turns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list Q. print the letters that are vowels using filter and lambda functions sample_string = "Welcome to AcadGild" Expected Output ['e', 'o', 'e', 'o', 'A', 'a', 'i']
input ="Welcome to AcadGild"
def filterOwels(input):
    for letter in input:
        if letter.lower() in ['a','e','i','o','u']:
            return True
        else:
            return False

result = list(filter(filterOwels,input))
print(result)


# In[4]:


#4) Use generator expression to print out only alphabets from the following string string = "123@Welc34ometo12@ac#adGild" Output : 'WelcometoacadGild'
def my_gen(input):
    for letter in input:
        if letter.isalpha():
            yield letter

output = ''

for alphabet in my_gen("123@Welc34ometo12@ac#adGild"):
      output += alphabet

print(output)


# In[5]:


#5) Implement a function longestWord() that takes a list of words and returns the longest one. Sample Word List word= ["January","Feburary","March","April","May","June","July"] Expected Output ['Feburary']
def wordLength(word):
    return len(word)

def longestWord(words):
    max_len = len(max(words,key=wordLength))
    return [x for x in words if len(x) == max_len]

words= ["January","Feburary","March","April","May","June","July"]
print (longestWord(words))


# In[ ]:




