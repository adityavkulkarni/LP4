#!/usr/bin/env python
# coding: utf-8

# In[13]:


import kaggle
def update_data():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('sudalairajkumar/covid19-in-india', path='/home/aditya/LPIV-Covid/data', unzip=True)


# In[ ]:




