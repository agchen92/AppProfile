#!/usr/bin/env python
# coding: utf-8

# In[16]:


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
googleplay_header = googleplay[0]
googleplay = googleplay[1:]


# In[17]:


#To make the data easier to explore. Let's create a function
#named explore_data so we can use it repeatedly to print rows
#in a more readable way.

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# In[14]:


#Explore App Store data.
print(ios_header)
explore_data(ios, 0, 3, True)

#We can see that the App Store data has 7197 rows and 16 colummns.
#From initial glance, we can see that relevant columns include 'track_name'
#'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', and 'prime_genre'.'


# In[20]:


#Explore Google Play data.
print(googleplay_header)
explore_data(googleplay, 0, 3, True)

#We can see that the Google Play data has 10841 rows and 13 colummns.
#From initial glance, we can see some relevant columns for this research
#include "App", "Category", "Rating", "Type", "Price", "Content Rating",
#and "Genres".


# In[ ]:




