# 🎬 Movie Recommendation System

This is a **Movie Recommendation System** built using **Streamlit, Scikit-learn, and TMDB API**.  
It recommends **10 similar movies** based on **cosine similarity** of TF-IDF vectorized tags.  

---

## 🚀 Features
- 🔍 **Select a movie** from the dropdown menu.
- 🎭 **Get 10 similar movie recommendations** based on content similarity.
- 🖼️ **View movie posters** fetched dynamically from the TMDB API.
- 📜 **See a short overview** of each recommended movie.
- ⚠️ **Warning if no movie is selected** before clicking "Recommend."

---

## 🛠️ Installation

### 1️⃣ Clone the Repository  
```sh 
git clone https://github.com/SHIGINVP/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```


### 2️⃣ Install Dependencies

Ensure you have Python 3.8+ installed, then install dependencies:

```sh
pip install -r requirements.txt
```



## 📥 Download Dataset from Kaggle
### 3️⃣ Get Your Kaggle API Token

This project requires a dataset from Kaggle. Follow these steps to download it:

1. Sign in to [Kaggle](https://www.kaggle.com/)

2. Go to your **account settings**
	- Click on your **profile** > **Account**

3. **Scroll down to ‘API’** and click on **‘Create New API Token’**
	- This will download a file named **kaggle.json**



## 🎯 Generate the movie_data.pkl File

### 4️⃣Run the Jupyter Notebook

Before running the Streamlit app, you must generate `movie_data.pkl`:

```sh
jupyter notebook
```

Then, open `Movie_recommendation_system.ipynb` and run all the cells.
This will process the dataset and create `movie_data.pkl`, which is required for the app.


## ▶️ Run the Streamlit App

Once the `movie_data.pkl` file is generated, start the Streamlit app:

```sh
streamlit run app.py
```


## 📌 Project Structure

```sh
📂 Movie-Recommendation-System
│── 📂 data                     # Dataset folder (downloaded from Kaggle)
│── 📜 app.py                   # Streamlit app
│── 📜 Movie_recommendation_system.ipynb  # Jupyter Notebook (for generating pkl file)
│── 📜 requirements.txt         # Required Python libraries
│── 📜 README.md                # Project documentation
│── 📜 movie_data.pkl           # Generated file (not provided, must be created)
│── 📜 kaggle.json              # Kaggle API key file (should be placed in ~/.kaggle)

```


## 🔑 API Key Setup

This project uses The Movie Database (TMDB) API to fetch posters.
Replace the api_key in app.py with your own TMDB API key:

api_key = "your_tmdb_api_key_here"

Get a free API key from [TMDB](https://www.themoviedb.org/).

## 🔥 Demo
- Example output:
![Movie Recommendation System UI](https://github.com/SHIGINVP/Movie-Recommendation-System/blob/main/Movie_Recommendation_System_UI.png)

## 📌 Requirements

Check `requirements.txt` for dependencies.



## 📜 License

This project is licensed under the MIT License.



