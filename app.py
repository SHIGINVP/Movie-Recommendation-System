import streamlit as st
import pandas as pd
import requests
import pickle

# Load data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Recommendation logic
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id', 'overview']].iloc[movie_indices]

# Fetch poster from TMDB
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

# Page config
st.set_page_config(layout="wide")

# Centered title
st.markdown("<h1 style='text-align: center;'>🎥 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Layout: Two columns
left_col, right_col = st.columns([1, 2])

# --- LEFT COLUMN ---
with left_col:
    st.subheader("🎞️ Select a Movie")
    movie_options = ["Select a movie..."] + list(movies['title'].values)
    selected_movie = st.selectbox("", movie_options, index=0)

    if selected_movie != "Select a movie...":
        selected = movies[movies['title'] == selected_movie].iloc[0]
        poster = fetch_poster(selected['movie_id'])

        st.subheader("🎬 Selected Movie")

        selected_tile = f"""
            <div style="
                display: flex;
                background-color: #818181;
                border-radius: 15px;
                padding: 10px;
                margin-bottom: 15px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.15);
                color: white;
            ">
                <img src="{poster}" style="width: 100px; height: auto; border-radius: 10px; margin-right: 15px;">
                <div>
                    <h4 style="margin: 0 0 5px 0;">{selected_movie}</h4>
                    <p style="text-align: justify; font-size: 13px; margin: 0;">{selected['overview']}</p>
                </div>
            </div>
        """
        st.markdown(selected_tile, unsafe_allow_html=True)

# --- RIGHT COLUMN ---
with right_col:
    if selected_movie != "Select a movie...":
        st.subheader("📽️ Recommended Movies")

        recommendations = get_recommendations(selected_movie)

        for index in range(len(recommendations)):
            rec = recommendations.iloc[index]
            rec_poster = fetch_poster(rec['movie_id'])

            tile_html = f"""
                <div style="
                    display: flex;
                    background-color: #818181;
                    border-radius: 15px;
                    padding: 10px;
                    margin-bottom: 15px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
                    color: white;
                ">
                    <img src="{rec_poster}" style="width: 80px; height: auto; border-radius: 10px; margin-right: 15px;">
                    <div>
                        <h4 style="margin: 0 0 5px 0;">{rec['title']}</h4>
                        <p style="text-align: justify; font-size: 13px; margin: 0;">{rec['overview']}</p>
                    </div>
                </div>
            """
            st.markdown(tile_html, unsafe_allow_html=True)

