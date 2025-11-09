import pandas as pd

def clean_data(df):
    """
    Clean the dataset: handle duplicates, missing values, and outliers
    """
    print("\n" + "="*80)
    print("STEP 2: DATA CLEANING")
    print("="*80)
    
    df_clean = df.copy()
    df_clean.columns=df_clean.columns.str.strip()
    
    # 2.1 Handle duplicates based on name and artist
    print("\n2.1 Handling Duplicates...")
    initial_rows = len(df_clean)
    
    # Identify numeric and non-numeric columns
    numeric_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns.tolist()
    non_numeric_cols = [col for col in df_clean.columns if col not in numeric_cols + ['name', 'artist']]
    
    # Create aggregation dictionary
    agg_dict = {col: 'mean' for col in numeric_cols}
    agg_dict.update({col: 'first' for col in non_numeric_cols})
    
    df_clean = df_clean.groupby(['name', 'artist'], as_index=False).agg(agg_dict)
    print(f"Removed {initial_rows - len(df_clean)} duplicate rows")
    print(f"Remaining rows: {len(df_clean)}")
    
    # 2.2 Handle missing values
    print("\n2.2 Handling Missing Values...")
    missing_before = df_clean.isnull().sum().sum()
    
    # For numeric columns, fill with median
    for col in numeric_cols:
        if df_clean[col].isnull().any():
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    # For non-numeric columns, fill with mode or 'Unknown'
    for col in non_numeric_cols:
        if df_clean[col].isnull().any():
            df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else 'Unknown', inplace=True)
    
    missing_after = df_clean.isnull().sum().sum()
    print(f"Filled {missing_before - missing_after} missing values")
    
    # 2.3 Detect and handle outliers using IQR method
    print("\n2.3 Outlier Detection (IQR Method)...")
    
    feature_cols = ['danceability', 'energy', 'key', 'loudness', 'mode',
                    'speechiness', 'acousticness', 'instrumentalness', 
                    'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
    df_clean=df_clean.loc[(df_clean['loudness']<=0) &  (df_clean['tempo'] !=0)]
    
    print("\n2.5 Data frame after cleaning")
    print(f'Count of Rows={len(df_clean)}')
    return df_clean