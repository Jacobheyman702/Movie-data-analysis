# Movie Data Analysis (Create Better Title)

**Authors**: Jacob Heyman, Mitch Krieger

## Overview

A one-paragraph overview of the project, including the business problem, data, methods, results and recommendations.

## Business Problem

Summary of the business problem you are trying to solve, and the data questions that you plan to answer in order to solve them.

***
Questions to consider:
* What are the business's pain points related to this project?
* How did you pick the data analysis question(s) that you did?
* Why are these questions important from a business perspective?
***

**Current research questions:**
1. Which genre of movies has the highest average net **profit** over the past 10 years?
2. Which genre of movies has the greatest upward trend over the past 10 years for average net profit?
3. What is the relations between budget and box office gross? Domestically vs foriegn?
4. Which directors/writers/actors make the most profitable movies?
5. Relationship between rating and gross? Run-time and gross?

## Data

Describe the data being used for this project.

***
Questions to consider:
* Where did the data come from, and how do they relate to the data analysis questions?
* What do the data represent? Who is in the sample and what variables are included?
* What is the target variable?
* What are the properties of the variables you intend to use?
***

Data Sets:
* rt_reviews_df - **Rotten Tomatoes Critics Reviews** - id, review, rating, fresh, critic, top_critic, publisher, date
* rt_movie_info_df - **Rotten Tomatoes Movie Info** - id, synopsis, genre, director, writer, theater_date, dvd_date, currency, box_office, runtime, studio
* imdb_title_df - **IMDB Movie titles & genre** - tconst, primary_title, original_title, start_year, runtime_minutes, genres
* imdb_name_df - **IMDB Staff Names & Jobs** - nconst, primary_name, birth_year, death_year, primary_profession, known_for_titles (tconst)
* imdb_title_akas_df - **IMDB Movie Region & Language** - title_id (tconst), ordering, title, region, language, type, attributes, _originaltitle
* imdb_title_crew_df - **IMDB Movie Directors & Writers** - tconst, directors(nmconst), writers (nmconst)
* imdb_principles_df - **IMDB Movie Principle Roles & Crew)** - tconst, ordering, nconst, category, job, character
* imdb_title_rating_df - **IMDB Ratings** - tconst, avgeragerating, numvotes
* bom_movie_gross_df - **Box Office Grosses** - title, studio, domestic_gross, foreign_gross, year
* movie_budgets_df - **Box Office Grosses & Budgets** - id, movie, release_date, production_budget, domestic_gross, worldwide_gross

## Methods

Describe the process for analyzing or modeling the data. For Phase 1, this will be descriptive analysis.

***
Questions to consider:
* How did you prepare, analyze or model the data?
* Why is this approach appropriate given the data and the business problem?
***

## Results

Present your key results. For Phase 1, this will be findings from your descriptive analysis.

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

Here is an example of how to embed images from your sub-folder:

### Visual 1
![graph1](./images/viz1.png)

## Conclusions

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── __init__.py                         <- .py file that signals to python these folders contain packages
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── code
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── visualizations.py               <- .py script to create finalized versions of visuals for project
│   ├── data_preparation.py             <- .py script used to pre-process and clean data
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
