from src.load_data import load_and_explore_data
from src.clean_data import clean_data
from src.eda import perform_eda
def execute_pipeline(df):
    load_and_explore_data(df)
    cleaned_df=clean_data(df)
    perform_eda(cleaned_df)
    
    