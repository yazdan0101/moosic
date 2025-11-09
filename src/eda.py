import matplotlib.pyplot as plt
import seaborn as sns
import math
def perform_eda(df):
    """
    Visualize distributions and relationships in the data
    """
    print("\n" + "="*80)
    print("STEP 3: EXPLORATORY DATA ANALYSIS")
    print("="*80)
    
    feature_cols = ['danceability', 'energy', 'valence','tempo', 'speechiness', 'acousticness', 
                               'instrumentalness', 'duration_ms','liveness']
    
    # 3.1 Distribution plots
    print("\n3.1 Creating distribution plots...")
    n_features = len(feature_cols)
    n_cols = 2
    n_rows = math.ceil(n_features / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 16))
    fig.subplots_adjust(hspace=.6)
    axes = axes.ravel()
    
    for idx, col in enumerate(feature_cols):
        axes[idx].hist(df[col], bins=50, edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribution of {col}', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel(col)
        axes[idx].set_ylabel('Frequency')
        axes[idx].grid(True, alpha=0.3)
    
    plt.savefig('visualization/01_feature_distributions.png', bbox_inches='tight')
    print("Saved: 01_feature_distributions.png")
    
    # 3.2 Box plots for outlier visualization
    print("\n3.2 Creating box plots...")
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 16))
    fig.subplots_adjust(hspace=.6)
    axes = axes.ravel()
    for idx, col in enumerate(feature_cols):
        axes[idx].boxplot(df[col], vert=True)
        axes[idx].set_title(f'Box Plot: {col}', fontsize=12, fontweight='bold')
        axes[idx].set_ylabel(col)
        axes[idx].grid(True, alpha=0.3)
    plt.savefig('visualization/02_feature_boxplots.png',bbox_inches='tight')
    print("Saved: 02_feature_boxplots.png")
    # 3.3 Correlation matrix
    print("\n3.3 Creating correlation matrix...")
    correlation_matrix = df[feature_cols].corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Feature Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('visualization/03_correlation_matrix.png', bbox_inches='tight')
    
    # 3.4 Pairwise relationships (sample of key features)
    print("\n3.4 Creating pairplot for key features...")
    key_features = ['danceability', 'energy', 'valence', 'acousticness']
    
    pairplot_data = df[key_features].sample(min(1000, len(df)))  # Sample for performance
    sns.pairplot(pairplot_data, diag_kind='kde', plot_kws={'alpha': 0.6})
    plt.suptitle('Pairwise Relationships (Key Features)', y=1.01, fontsize=16, fontweight='bold')
    plt.savefig('visualization/04_pairplot.png',bbox_inches='tight')
    print("Saved: 04_pairplot.png")