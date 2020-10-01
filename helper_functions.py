import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv_to_clean_dataframes import *
plt.style.use('seaborn')

def genre_dataframe_select(genre):
    """
    Returns a dataframe of only entries that have a specified genre listed
    """
    return droped_genres_dataframe.loc[droped_genres_dataframe.genres.str.contains(genre)]


def genre_vs_net (genre,ax):
    """
    Returns an axis that plots a genres's worldwide net performace as a barchart over the past 10 years
    """
    
    df = genre_dataframe_select(genre)
    y = df.groupby(['start_year'])['worldwide_net'].mean()[:10]
    x = y.index
    
    ax.bar(x, y)
    ax.set_title(f'{genre}')
    ax.set_xticks([])
    ax.set_ylim(bottom=0,top= 5.5e8)
    return ax

def genre_vs_percent_gross (genre,ax):
    """
    Returns an axis that plots a genres's percentage worldwide gross performace as a barchart over the past 10 years
    """
    df = genre_dataframe_select(genre)
    y = df.groupby(['start_year'])['percent_gross'].mean()[:10]
    x = y.index
    
    ax.bar(x, y)
    ax.set_title(f'{genre}')
    ax.set_xticks([])
    ax.set_ylim(bottom=0,top= 2e3)
    return ax

def label_chart(ax,title=None,xlabel=None,ylabel=None):
    """
    Sets title and axis labels on a given axes
    """
    if title:
        ax.set_title(title)
        
    if xlabel:
        ax.set_xlabel(xlabel)
    
    if ylabel:
        ax.set_ylabel(ylabel)
        
    return None
