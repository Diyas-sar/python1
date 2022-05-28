#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
a = np.array([[ 1, 2, 3, 3, 1],[6, 8, 11, 10, 7]]).T
a


# In[56]:


mean_a = a.mean(axis = 0)
mean_a


# In[57]:


a_centered = a-mean_a
a_centered


# In[60]:


a_centered_sp = a_centered[:,0]@a_centered[:,1]
a_centered_sp


# In[65]:


b =a_centered_sp/(len(a_centered)-1)


# In[ ]:




