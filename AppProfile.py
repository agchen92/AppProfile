#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


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


# In[4]:


#Explore App Store data.
print(ios_header)
explore_data(ios, 0, 3, True)

#We can see that the App Store data has 7197 rows and 16 colummns.
#From initial glance, we can see that relevant columns include 'track_name'
#'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', and 'prime_genre'.'


# In[5]:


#Explore Google Play data.
print(googleplay_header)
explore_data(googleplay, 0, 3, True)

#We can see that the Google Play data has 10841 rows and 13 colummns.
#From initial glance, we can see some relevant columns for this research
#include "App", "Category", "Rating", "Type", "Price", "Content Rating",
#and "Genres".


# In[8]:


#Now that we have explored some of the data inside this dataset
#let's go ahead and perform some basic data cleaning. Per the discussion
#on Kaggle, I have noticed that few of the rows have data that inconsistent
#with the rest.

print(googleplay[10472])  # incorrect row

#The row 10472 matches the app called Life Made WI-Fi Touchscreen Photo Frame, 
#and we can see that the rating is 19 above 5. I will delete this row because
#the rating is an error.

del googleplay[10472]


# In[9]:


#I will go ahead and perform more data cleaning on this dataset by
#removing duplicate apps and those that are not English.

for app in googleplay:
    name = app[0]
    if name == 'Instagram':
        print(app)


# In[10]:


duplicate_apps = []
unique_apps = []

for app in googleplay:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])


# In[12]:


reviews_max = {}

for app in googleplay:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
        
print('Expected length:', len(googleplay) - 1181)
print('Actual length:', len(reviews_max))


# In[15]:


googleplay_clean = []
already_added = []

for app in googleplay:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        googleplay_clean.append(app)
        already_added.append(name)
        
explore_data(googleplay_clean, 0, 3, True)


# In[ ]:




