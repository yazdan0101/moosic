from src.apply_pca import apply_pca
from src.clean_data import clean_data
from src.eda import perform_eda
from src.load_data import load_and_explore_data
from src.prepare_features import prepare_features


def execute_pipeline(df):
    load_and_explore_data(df)
    cleaned_df = clean_data(df)
    perform_eda(cleaned_df)
    x_scaled, _, _ = prepare_features(cleaned_df)
    apply_pca(x_scaled)
