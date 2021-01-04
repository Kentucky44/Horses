import pandas as pd

def get_data(nrows=10000, **kwargs):
    """method to get the training data (or a portion of it) from google cloud bucket"""

    #Loading Data
    path_races = "/Users/bruley-s/code/Kentucky44/Horses/Data/races.csv"
    path_runs = "/Users/bruley-s/code/Kentucky44/Horses/Data/runs.csv"

    races = pd.read_csv(path_races, nrows=nrows)
    runs = pd.read_csv(path_runs, nrows=nrows)

    # Features selection and Merging
    runs_data_df = runs[['race_id', 'won', 'horse_age', 'horse_country', 'horse_type', 'horse_rating',
       'horse_gear', 'declared_weight', 'actual_weight', 'draw', 'win_odds',
       'place_odds', 'horse_id']]
    races_data_df = races[['race_id', 'venue', 'config', 'surface', 'distance', 'going', 'race_class', 'date']]

    df = pd.merge(runs_data_df, races_data_df)

    return df
