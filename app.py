import streamlit as st
import pickle
import pandas as pd
import requests
import time

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=97eec547f090d527a97ae009cba8a534&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Fetching poster failed for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"

def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)  # polite delay for API
    return recommended_movies, recommended_posters

# Load Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox("Choose a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    names, posters = Recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
