
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv('u.data.csv', sep='\t',names=r_cols,usecols=range(3))
m_cols = ['movie_id','title']
ratings.head()


# In[ ]:


movies = pd.read_csv('u.item.csv',sep='|',names=m_cols,usecols=range(2))


# In[ ]:


ratings=pd.merge(movies,ratings)
ratings.head()


# In[ ]:


movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
movieRatings.head()


# In[11]:


starWarsRatings= movieRating['Star Wars (1977)']
starWarsRatings.head()


# In[ ]:


similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
df.head()


# In[ ]:


similarMovies.order(ascending=False)


# In[ ]:


similarMovies.sort_values(ascending=False)


# In[ ]:


movieStats=ratings.groupby('title').agg({'ratings': [np.size,np.mean]})
movieStats.head()


# In[ ]:


popularMovies = movieStats['ratings']['size'] >= 100
movieStats[popularMovies].sort([('ratings','mean')],ascending=False)[:15]


# In[ ]:


df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.head()


# In[ ]:


df.sort(['similarity'], ascending=False)[:15]


# In[ ]:


import pandas as pd
r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv('u.data.csv', sep='\t',names=r_cols,usecols=range(3))
m_cols = ['movie_id','title']
ratings.head()
movies = pd.read_csv('u.item.csv',sep='|',names=m_cols,usecols=range(2))
ratings=pd.merge(movies,ratings)
ratings.head()


# In[ ]:


userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()


# In[ ]:


corrMatrix = userRatings.corr()
corrMatrix.head()


# In[ ]:


corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()


# In[ ]:


myRatings= userRatings.loc[0].dropna()
myRatings


# In[ ]:


simCandidates = pd.Series()
for i in range(0,len(myRatings.index)):
    print('Adding sims for '+myRatings.index[i] + '...')
    # Retrieve similar movies to this one that I need
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print('sorting ....')
simCandidates.sort_values(inplace= True , ascending = False)
print(simCandidates.head(10))


# In[ ]:


simCandidates = simCandidates.groupby(simCandidates.index).sum()


# In[ ]:


simCandidates.sort_values(inplace= True , ascending = False)
simCandidates.head(10)


# In[ ]:


filteredSims = simCandidates.drop(myRatings.index)
filtered.head(10)

