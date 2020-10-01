import pandas as pd

#IMDB Titles
imdb_title_df = pd.read_csv('zippedData/imdb.title.basics.csv.gz')

#IMDB Staff Names & Jobs
imdb_name_df = pd.read_csv('zippedData/imdb.name.basics.csv.gz')
#Drop 'birth_year','death_year', 'primary_profession', unessacary for analysis
imdb_name_df.drop(['birth_year','death_year', 'primary_profession'], axis=1, inplace= True)

#IMDB Movie Region & Language
imdb_title_akas_df = pd.read_csv('zippedData/imdb.title.akas.csv.gz')
#Rename title_id to tconst for joining purposes
imdb_title_akas_df.rename({'title_id':'tconst'}, axis=1, inplace = True)

#IMDB Movie Writers & Directors
imdb_title_crew_df = pd.read_csv('zippedData/imdb.title.crew.csv.gz')

#IMDB Movie Principle Roles
imdb_principles_df = pd.read_csv('zippedData/imdb.title.principals.csv.gz')

#IMDB Ratings
imdb_title_rating_df = pd.read_csv('zippedData/imdb.title.ratings.csv.gz')
#Drop numvotes, unnessacary for analysis
imdb_title_rating_df.drop(['numvotes'], axis = 1, inplace = True)

#Box Office Grosses
bom_movie_gross_df = pd.read_csv('zippedData/bom.movie_gross.csv.gz')

#Box Office Grosses and Budgets
movie_budget_df = pd.read_csv('zippedData/tn.movie_budgets.csv.gz')
#strip strings of dollarsigns & commas, then convert to int 
movie_budget_df['worldwide_gross'] = movie_budget_df['worldwide_gross'].str.replace('$','').str.replace(',','').astype(int)
movie_budget_df['domestic_gross'] = movie_budget_df['domestic_gross'].str.replace('$','').str.replace(',','').astype(int)
movie_budget_df['production_budget'] = movie_budget_df['production_budget'].str.replace('$','').str.replace(',','').astype(int)
#Create worldwide net profit and percent gross of budget columns
movie_budget_df['worldwide_net'] = movie_budget_df['worldwide_gross'] - movie_budget_df['production_budget']
movie_budget_df['foreign_gross'] = movie_budget_df['worldwide_gross'] - movie_budget_df['domestic_gross']
movie_budget_df['percent_gross'] = (movie_budget_df['worldwide_net'] / movie_budget_df['production_budget'])*100
#Rename movie column to primary_title for joining purposes/consistency
movie_budget_df.rename({'movie':'primary_title'}, axis = 1, inplace = True)
#Drop release_date, redundant from year column
movie_budget_df.drop(['release_date'],axis = 1, inplace = True)


#joined dataframes
joined_table = imdb_title_df.merge(movie_budget_df, how='left', on = 'primary_title')
joined_table = joined_table.merge(imdb_title_rating_df, how='left', on = 'tconst')
#Drop NA values, due to question revolving around bugets vs grosses
joined_table.dropna(subset = ['production_budget'], inplace = True)
joined_table.drop(['id'],axis = 1, inplace = True)


#No missing values for gross:
noZero_gross = joined_table.loc[(joined_table.domestic_gross>0.0)&(joined_table.worldwide_gross>0) ]

#one to one join to incoroporate writers & directors
crew_grosses_df = pd.merge(noZero_gross,imdb_title_crew_df,how='inner',on='tconst')

#one to many join to incorporate principle roles (actors,writers,directors, composers, and so on)
principles_grosses_df = pd.merge(noZero_gross,imdb_principles_df,how='inner',on='tconst')

#no missing values for genres:
droped_genres_dataframe = noZero_gross.dropna(subset = ['genres'])
