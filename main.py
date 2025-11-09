import pandas as pd
from src.pipeline import execute_pipeline

if __name__ == "__main__":
    df=pd.read_csv('data/raw/spotify_songs.csv')
    execute_pipeline(df)