import pandas as pd
from sklearn.preprocessing import RobustScaler


def prepare_features(df):
    """
    Prepare features for clustering: selection, engineering, and scaling
    """
    print("\n" + "=" * 80)
    print("STEP 4: FEATURE ENGINEERING & SCALING")
    print("=" * 80)

    # 4.1 Select clustering features
    clustering_features = [
        'danceability', 'energy', 'valence',
        'tempo', 'speechiness', 'acousticness', 'instrumentalness', 'duration_ms', 'liveness'
    ]

    X = df[clustering_features].copy()

    print(f"Total features: {X.shape[1]}")

    # 4.3 Scaling using RobustScaler (better for outliers)
    print("\n4.2 Scaling features using RobustScaler...")
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)

    print("Scaling completed!")
    print("\nScaled data summary:")
    print(X_scaled_df.describe())

    return X_scaled_df, scaler, X.columns.tolist()
