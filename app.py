

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/550?api_key=97eec547f090d527a97ae009cba8a534&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies=[]
    recommend_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
"Which movie you want to see?",
movies['title'].values)
if st.button("Recommend"):
    names,posters =Recommend(selected_movie_name)
    #for i in recommendation:
        #st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
'''

st.header("Collaborative Filtering Recommendations (SVD)")
user_input = st.number_input("Enter User ID (1-943)", min_value=1, max_value=943)


def recommend_cf(user_input):
    pass


if st.button("Recommend using CF"):
    recommendations = recommend_cf(user_input)
    for index, row in recommendations.iterrows():
        st.write(row['title'])

def hybrid_recommend(user_id, selected_movie):
    # From content-based
    content_movies, _ = Recommend(selected_movie)  # from your old function

    # From CF
    cf_movies = recommend_cf(user_id)['title'].values

    # Combine (e.g., simple union or scoring)
    hybrid = list(set(content_movies) | set(cf_movies))
    return hybrid[:5]  # Top 5 merged


st.header("Hybrid Recommendation System")
if st.button("Hybrid Recommend"):
    hybrid_result = hybrid_recommend(user_input, selected_movie_name)
    for movie in hybrid_result:
        st.write(movie) '''


