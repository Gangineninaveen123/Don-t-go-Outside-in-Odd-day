#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = 0
odd = 0
for i in my_tuple:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
print("total number of even numbers in my_tuple: ",even)
print("total number of odd numbers in my_tuple:",odd)


# In[ ]:




