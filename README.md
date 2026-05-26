# 🎬 Netflix Movie Recommendation System

A Netflix-style Movie Recommendation System built using Python, Machine Learning, Streamlit, TMDB dataset, and Watchmode API.

## 🚀 Features

- Movie recommendation using Content-Based Filtering
- Cosine Similarity algorithm
- Search with autocomplete
- Real movie posters
- Movie ratings
- Movie descriptions
- Movie release year
- Genre distribution graph
- Interactive Streamlit dashboard
- Netflix-style UI

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Watchmode API
- TMDB Dataset
- Matplotlib

## 📂 Project Structure

movie-recommendation-system/

├── app.py  
├── movie_recommendation.py  
├── watchmode_api.py  
├── requirements.txt  
├── README.md  

## 📊 Machine Learning Workflow

Dataset  
↓  
Data Cleaning  
↓  
Feature Engineering  
↓  
Count Vectorization  
↓  
Cosine Similarity  
↓  
Recommendation Engine  
↓  
Streamlit Dashboard  

## 📥 Dataset

Download TMDB dataset from Kaggle:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Download files:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

## ⚙️ Installation

Install required libraries:
bash
pip install -r requirements.txt
run preprocessing
python movie_recommendation.py
run application
python -m streamlit run app.py
