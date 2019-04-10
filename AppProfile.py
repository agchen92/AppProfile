#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
For this project, my goal is to find profiles for profitable mobile apps
on the Google Play market and Apple App Store. Let's assume that I am working
for a company that builds mobile apps as an buiness operations associate and is
looking to use a data-driven approach to determine what type of mobile apps to 
make that are profitable.

The goal of the project will be working with datasets regarding Andriod and iOS
apps and then coming up with data insights to see what kind of apps attract more
users.
'''

from csv import reader

#Let's first import the App Store data.
open_file = open('AppleStore.csv')
read_file = reader(open_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

#Then import the Google Play data.
open_file = open('googleplaystore.csv')
read_file = reader(open_file)
googleplay = list(read_file)
googleplay_header = ios[0]
googleplay = ios[1:]

