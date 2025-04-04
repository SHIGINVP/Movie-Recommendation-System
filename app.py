import streamlit as st
import pandas as pd
import requests
import pickle

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id', 'overview']].iloc[movie_indices]  # Include 'overview'

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')  # Avoid errors if no poster
    return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

# Streamlit UI
st.title("🎥 Movie Recommendation System")

# Add a placeholder option at the top of the movie list
movie_options = ["Select a movie..."] + list(movies['title'].values)

# Dropdown menu with placeholder
selected_movie = st.selectbox("Select a movie:", movie_options, index=0)

# Show warning if the user clicks without selecting a movie
if st.button("Recommend"):
    if selected_movie == "Select a movie...":
        st.warning("⚠️ Please select a movie before getting recommendations!")
    else:
        recommendations = get_recommendations(selected_movie)

        st.write("### Top 10 Recommended Movies:")

        # Create a 2x5 grid layout
        for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
            cols = st.columns(5)  # Create 5 columns for each row
            for col, j in zip(cols, range(i, i+5)):
                if j < len(recommendations):
                    movie_title = recommendations.iloc[j]['title']
                    movie_id = recommendations.iloc[j]['movie_id']
                    movie_overview = recommendations.iloc[j]['overview']
                    poster_url = fetch_poster(movie_id)

                    with col:
                        if poster_url:
                            st.image(poster_url, width=130)
                        st.write(f"**{movie_title}**")  # Bold movie title
                        st.markdown(f"<p style='text-align: justify; font-size: 12px;'>{movie_overview}</p>", unsafe_allow_html=True)  # Styled overview

