# 🎵 Moosic - Music Clustering Project

## 📖 Overview
**Moosic** is a data science project that uses clustering techniques to automatically group 5,000 music tracks into playlists based on their audio features.  
The goal is to discover natural groupings among songs — for example, by tempo, energy, danceability, valence, and other extracted attributes — and create playlists that represent distinct musical moods or styles.

## 🧠 Objective
The main objective of this project is to:
- Analyze a dataset of 5,000 songs and their audio features.
- Apply clustering algorithms (such as K-Means, DBSCAN, or Hierarchical Clustering).
- Visualize the clusters and interpret what musical traits define each playlist.
- Generate representative playlists from the discovered clusters.

## 🏗️ Project Structure
```
📁 moosic/
├── data/               
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── eda.py
│   ├── clustering.py
│   └── pipeline.py
├── .gitignore
├── requirements.txt
├── README.md
└── main.py       
```

## ⚙️ Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/moosic.git
   cd moosic
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
You can run the project using:
```bash
python main.py
```

## 🧩 Features
- Data cleaning and preprocessing of audio feature data.
- Implementation of multiple clustering algorithms (e.g., K-Means, DBSCAN).
- Dimensionality reduction (e.g., PCA, t-SNE) for visualization.
- Evaluation of cluster quality using metrics like silhouette score.
- Visualization of clusters and playlists.
- Export of clustered playlists for further analysis.

## 🧪 Testing
Run all tests using:
```bash
pytest
```

## 📊 Technologies Used
- **Python**
- **NumPy**, **Pandas** – Data analysis
- **scikit-learn** – Machine learning and clustering
- **Matplotlib**, **Seaborn** – Visualization
- **Jupyter Notebook** – Exploratory analysis

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## ✨ Author
**Yazdan**  
Junior Data scientist & Software Developer 
📍 Based in Germany  
📧 yazdan.mohammadi.dev@gmail.com

https://www.yazdan.tech
