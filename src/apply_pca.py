import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def apply_pca(X_scaled):
    """
    Apply PCA for visualization and variance analysis
    """
    print("\n" + "=" * 80)
    print("STEP 5: DIMENSIONALITY REDUCTION (PCA)")
    print("=" * 80)

    # 5.1 Apply PCA
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)

    # 5.2 Explained variance
    print("\n5.1 Explained Variance by Component:")
    explained_variance = pca.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance)

    for i, (var, cum_var) in enumerate(zip(explained_variance[:10], cumulative_variance[:10])):
        print(f"PC{i + 1}: {var:.4f} (Cumulative: {cum_var:.4f})")

    # 5.3 Visualize explained variance
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.bar(range(1, len(explained_variance) + 1), explained_variance, alpha=0.7, edgecolor='black')
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('Explained Variance by Component', fontweight='bold')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linewidth=2)
    plt.axhline(y=0.95, color='r', linestyle='--', label='95% Variance')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('visualization/05_pca_variance.png', bbox_inches='tight')
    print("\nSaved: 05_pca_variance.png")

    # Determine optimal number of components (95% variance)
    n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
    print(f"\n5.2 Components needed for 95% variance: {n_components_95}")

    return X_pca, pca, n_components_95
