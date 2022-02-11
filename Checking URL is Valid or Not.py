#!/usr/bin/env python
# coding: utf-8

# In[2]:


#checking whether the url is valid or not

import re

def isvalidurl(str):
    formatofurl = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p=re.compile(formatofurl)
    
    if(re.search(p,str)):
        return True
    else:
        return False
url = "https://www.youtube.com/"

if(isvalidurl(url) == True):
    print("yes")
else:
    print("No")


# In[ ]:




