import pandas as pd
def load_and_explore_data(df):
    """
    Initial data exploration and summary statistics
    """
    print("="*80)
    print("STEP 1: DATA EXPLORATION")
    print("="*80)
    
    # Basic info
    print("\n1.1 Dataset Shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n1.2 Data Types:")
    print(df.dtypes)
    
    print("\n1.3 Missing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({'Missing': missing, 'Percentage': missing_pct})
    print(missing_df[missing_df['Missing'] > 0] if len(missing_df[missing_df['Missing'] > 0])>0 else ' No missing valuses' )
    
    print("\n1.4 Duplicate Rows:")
    duplicates = df.duplicated().sum()
    print(f"Total duplicates: {duplicates}" if duplicates>0 else 'No duplicated rows')
    
    print("\n1.5 Statistical Summary:")
    print(df.describe())
    return df
