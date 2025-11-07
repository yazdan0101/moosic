import pandas as pd
from src.load_data import load_and_explore_data


if __name__ == "__main__":
    df=pd.read_csv('data/raw/spotify_songs.csv')
    load_and_explore_data(df)