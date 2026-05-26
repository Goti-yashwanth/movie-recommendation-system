import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge
movies = movies.merge(credits,on='title')

movies = movies[
['movie_id',
'title',
'overview',
'genres',
'keywords',
'cast',
'crew']
]

movies.dropna(inplace=True)


# Convert JSON strings

def convert(text):
    L=[]

    for i in ast.literal_eval(text):
        L.append(i['name'])

    return L


movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['cast']=movies['cast'].apply(convert)


# Convert overview into list
movies['overview']=movies['overview'].apply(
    lambda x:x.split()
)

# Create tags
movies['tags']=(
movies['overview']+
movies['genres']+
movies['keywords']+
movies['cast']
)

new_df=movies[['movie_id','title','tags']]

new_df['tags']=new_df['tags'].apply(
    lambda x:" ".join(x)
)

# Vectorize
cv=CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors=cv.fit_transform(
    new_df['tags']
).toarray()

# Similarity
similarity=cosine_similarity(
    vectors
)

# Save files
pickle.dump(
    new_df,
    open('movies.pkl','wb')
)

pickle.dump(
    similarity,
    open('similarity.pkl','wb')
)

print("Recommendation engine created")