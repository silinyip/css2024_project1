#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:28:11 2024

@author: SiLin
"""

import pandas as pd
url = "https://github.com/silinyip/css2024_project1/blob/ba820817728baab53cd59e64758d9e20fdf54a23/movie_dataset.csv?raw=true"
df = pd.read_csv(url, index_col = 0)

# restart kernel for each question

# Question 1
df.dropna(inplace = True)
df = df.reset_index(drop=True)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop=True)

df.sort_values(by = "Rating", ascending = False)


# Question 2
df.dropna(inplace = True)
df = df.reset_index(drop=True)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop=True)

avg_rev = df["Revenue (Millions)"].mean()
print(avg_rev)


# Question 3
df.dropna(inplace = True)
df = df.reset_index(drop=True)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop=True)

years_q3 = [2015, 2016, 2017]
filt_q3 = df["Year"].isin(years_q3)
df_q3 = df.loc[filt_q3] #, ["Year", "Revenue (Millions)"]]
avg_rev_q3 = df_q3["Revenue (Millions)"].mean()


# Question 4
year_q4 = [2016]
filt_q4 = df["Year"].isin(year_q4)
df_q4 = df.loc[filt_q4]
df_q4.reset_index()


# Question 5
filt_q5 = (df["Director"] == "Christopher Nolan")
df[filt_q5]


# Question 6
filt_q6 = (df["Rating"] > 8.0)
df_q6 = df.loc[filt_q6]


# Question 7
filt_q7 = (df["Director"] == "Christopher Nolan")
df[filt_q7]
df_q7 = df.loc[filt_q7]
avg_rating_q7 = df_q7["Rating"].mean()


# Question 8
df.dropna(inplace = True)
df = df.reset_index(drop=True)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop=True)

year_2006 = [2006]
filt_q8_2006 = df["Year"].isin(year_2006)
df_q8_2006 = df.loc[filt_q8_2006]
avg_rating_q8_2006 = df_q8_2006["Rating"].mean()

year_2007 = [2007]
filt_q8_2007 = df["Year"].isin(year_2007)
df_q8_2007 = df.loc[filt_q8_2007]
avg_rating_q8_2007 = df_q8_2007["Rating"].mean()

year_2008 = [2008]
filt_q8_2008 = df["Year"].isin(year_2008)
df_q8_2008 = df.loc[filt_q8_2008]
avg_rating_q8_2008 = df_q8_2008["Rating"].mean()

year_2016 = [2016]
filt_q8_2016 = df["Year"].isin(year_2016)
df_q8_2016 = df.loc[filt_q8_2016]
avg_rating_q8_2016 = df_q8_2016["Rating"].mean()


# Question 9
years_q9 = [2006, 2016]
filt_q9 = df["Year"].isin(years_q9)
df_filt_q9 = df.loc[filt_q9]
num_movies_2006 = df_filt_q9[df_filt_q9["Year"] == 2006].shape[0]
num_movies_2016 = df_filt_q9[df_filt_q9["Year"] == 2016].shape[0]
percent_increase_q9 = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100


# Question 10
actors_q10 = ["Chris Pratt", "Matthew McConaughey", "Mark Wahlberg", "Bradley Cooper"]
actor_filt_q10 = df["Actors"].apply(lambda actors: any(str(actor) in str(actors) for actor in actors_q10))
df_filt_q10 = df[actor_filt_q10]
all_actors_q10 = df_filt_q10["Actors"].str.split(', ').explode()
actor_counts_q10 = all_actors_q10.value_counts()
print("Number of times each actor was mentioned:")
print(actor_counts_q10)


# Question 11
all_genres_q11 = df["Genre"].str.split(', ').explode()
unique_genres_q11 = all_genres_q11.unique()
num_unique_genres_q11 = len(unique_genres_q11)
print(f"Number of unique genres: {num_unique_genres_q11}")


# Question 12
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()

print("Correlation Matrix:")
print(correlation_matrix)





















