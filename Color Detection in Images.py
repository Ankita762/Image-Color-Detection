#!/usr/bin/env python
# coding: utf-8

# In[29]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[30]:


img=cv2.imread(r"C:\Users\ANKITA TAPADAR\Desktop\images.jpg")


# In[31]:


plt.figure(figsize=(20,8))
plt.imshow(img)


# In[32]:


rgb1= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[33]:


plt.figure(figsize=(20,8))
plt.imshow(rgb1)


# In[34]:


hsv=cv2.cvtColor(rgb1, cv2.COLOR_RGB2HSV)


# In[87]:


#lower_range = np.array([35,100,100]) #green
#upper_range = np.array([65,255,255])

#lower_range = np.array([15,99,56]) #yellow
#upper_range = np.array([35,255,255])

#lower_range = np.array([0,155,84]) #red
#upper_range = np.array([10,255,255])

#lower_range = np.array([70,50,50]) #sea-green
#upper_range = np.array([95,255,255])

lower_range = np.array([95,50,50]) #blue
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)


# In[88]:


mask = cv2.inRange(hsv, lower_range, upper_range)


# In[89]:


plt.figure(figsize=(20,8))
plt.imshow(mask)


# In[90]:


res = cv2.bitwise_and(rgb1,rgb1,mask=mask)


# In[91]:


plt.figure(figsize=(20,8))
plt.imshow(res)


# In[23]:


cv2.imshow('image',rgb1)


# In[ ]:
