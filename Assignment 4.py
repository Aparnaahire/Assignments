#!/usr/bin/env python
# coding: utf-8

# Que 1)
#       Index brackets have many uses in python. First they are used to define "list literals", allowing you yo declare a list and its contents in your program.

# Que 2)
#       spam=[2,4,6,8,10]

# In[2]:


spam=[2,4,6,8,10]


# In[3]:


spam[2]="hello"


# In[4]:


spam


# Que 3)
#      spam=['a','b','c','d ']

# In[13]:


spam=['a','b','c','d']


# In[14]:


spam[int(int('3'*2)/11)]


# Que 4)

# In[15]:


spam[-1]


# Que 5)

# In[16]:


spam[:2]


# Que 6)

# In[17]:


bacon=[3.14,"cat",11,"cat",True]


# In[18]:


bacon.index("cat")


# Que 7)

# In[19]:


bacon.append(99)


# In[20]:


bacon


# Que 8)

# In[21]:


bacon=[3.14,"cat",11,"cat",True]


# In[22]:


bacon.remove("cat")


# In[23]:


bacon


# 

# Que 9)
# 
# The operator for list concatenation is + ,while the operator for list replication is * . 

# Que 10)
# 
#     append () will add values only to the end of list and insert() can add value anywhere in the list.

# Que 11)
# 
#     List methods clear() , pop(), and remove() to remove items from a list.

# Que 12)
#        The similarity between lists and strings in python is that both are sequences. Both lists and strings can be passed to len(), have indexes and slices , be used in for loops , be concatenated or replicated and be used with in and not in operators.
#        

# Que 13) The difference between the Tuples and list is that while the tuples are immutable objects and the list are mutable. List can have values added, removed, or changed. tuples cannot be changed at all.
#        

# Que 14)
#        (42) the trailing comma is mandatory

# Que 15) 
#        To get list value's tuple form we can use tuple() function,
#        and to get tuple value's list form we can use list() function
#        

# Que 16) They contain references to list values.
#        

# Que 17)
#        The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list . That is, only copy.deepcopy() will duplicate any lists inside the list.
