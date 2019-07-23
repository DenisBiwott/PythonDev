#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


# data = pd.read_csv('music.csv')
# x = data.drop(
# columns=['genre'])
# y = data['genre']
# model = DecisionTreeClassifier()
# model.fit(x, y)
# joblib.dump(model, 'genre_predictions.joblib')

pred_genre = joblib.load('genre_predictions.joblib')
pred_genre.predict([[21, 1], [22, 0]])


# In[ ]:





# In[ ]:




