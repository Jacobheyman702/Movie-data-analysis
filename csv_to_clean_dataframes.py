import pandas as pd

#Rotten Tomatoes Reviews
rt_review_df = pd.read_csv('zippedData/rt.reviews.tsv.gz', delimiter = '\t', encoding = 'unicode_escape')

#Rotten Tomatoes Movie Info
rt_movie_info = pd.read_csv('zippedData/rt.movie_info.tsv.gz', delimiter = '\t', encoding = 'unicode_escape')

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
