#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Python program to get a set of
# places according to your search
# query using Google Places API

# importing required modules
import requests, json

# enter your api key here
api_key = 'AIzaSyBlOP6WbEBoce4SHGscO_d_yi8iZXDSzDc'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = input('Search query: ')

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +'&key=' + api_key)

# json method of response object convert
# json format data into python format data
x = r.json()

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

# keep looping upto length of y
for i in range(len(y)):
    # Print value corresponding to the
    #'name' key at the ith index of y
    print(y[i]['name'])
    print(y[i]['geometry'])
    print(y[i]['types'])
    print(y[i]['rating'])
    print(y[i]['business_status'])
    print(y[i]['formatted_address'])


# In[ ]:


get_ipython().system(u'pip install requests')


# In[7]:


x.values()


# In[ ]:



