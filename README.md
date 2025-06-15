# movie_recommeder_system
full stack movie recommendation system



🚀 Introduction

A machine learning-based Movie Recommendation System that suggests movies similar to a selected movie.

Uses content-based filtering and similarity measures.

Developed with Python and deployed using Streamlit.

🎯 Objective

Provide personalized movie recommendations based on similarity scores.

Enhance user experience with relevant movie suggestions and posters.

🛠️ Technology Stack

Programming Language: Python

Framework: Streamlit

Libraries: Pandas, Pickle, Requests

Dataset: Movie dataset stored in a pickle file

API Used: The Movie Database (TMDb) API for fetching movie posters

🔍 Methodology

Data Collection: Load movie dataset from a pickle file.

Data Processing: Convert dataset into a Pandas DataFrame.

Similarity Computation: Use a precomputed similarity matrix (similarity.pkl).

Recommendation Algorithm:

Takes a movie title as input.

Retrieves movie index and computes similarity scores.

Returns top 5 most similar movies.

Fetches movie posters using the TMDb API.

User Interface:

Built with Streamlit.

Dropdown to select a movie.

Button to generate recommendations.

Displays five recommended movie titles with posters.

🎨 Implementation

Python-based recommendation function (Recommend(movie)).

Streamlit UI for user interaction.

TMDb API integration for fetching movie posters.

📊 Results

Successfully provides movie recommendations based on input.

Displays recommended movies with posters for a better user experience.

🚀 Future Enhancements

Hybrid Recommendation System: Combine content-based and collaborative filtering.

User Authentication: Personalized recommendations based on user watch history.

Real-Time Updates: Fetch live movie data for updated recommendations.

Enhanced UI/UX: Improve frontend design and interactivity.

📌 Conclusion

A practical application of machine learning and data science.

Uses TMDb API for enhanced visual experience.

Future improvements can make the system more robust and personalized.
