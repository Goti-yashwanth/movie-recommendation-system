from watchmode_api import get_movie_details
import streamlit as st
import pickle
import pandas as pd
import ast
from collections import Counter
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

st.set_page_config(
page_title="Netflix Movie Recommender",
page_icon="🎬",
layout="wide"
)

# -------------------------
# TITLE
# -------------------------

st.markdown("""
<h1 style='text-align:center;color:red'>
🎬 Netflix Movie Recommendation System
</h1>

<h4 style='text-align:center'>
Find your next favorite movie 🍿
</h4>
""",
unsafe_allow_html=True)

st.write("---")

# -------------------------
# SEARCH
# -------------------------

selected_movie=st.selectbox(
"🔍 Search Movie",
movies['title'].values
)

# -------------------------
# RECOMMEND FUNCTION
# -------------------------

def recommend(movie):

    movie_index=movies[
    movies['title']==movie
    ].index[0]

    distances=similarity[movie_index]

    movie_list=sorted(
    list(enumerate(distances)),
    reverse=True,
    key=lambda x:x[1]
    )[1:6]

    recommendations=[]
    scores=[]

    for i in movie_list:

        recommendations.append(
        movies.iloc[i[0]].title
        )

        scores.append(
        round(i[1]*100,2)
        )

    return recommendations,scores


# -------------------------
# RECOMMENDATION SECTION
# -------------------------

if st.button("🎥 Recommend"):

    with st.spinner(
    "Finding movies..."
    ):

        names,scores=recommend(
        selected_movie
        )

        st.subheader(
        "Recommended Movies"
        )

        cols=st.columns(5)

        for col,name,score in zip(
        cols,
        names,
        scores
        ):

            with col:

                details=get_movie_details(
                name
                )

                if details:

                    title=details.get(
                    'title',
                    name
                    )

                    poster=details.get(
                    'poster',
                    "https://via.placeholder.com/300x450.png?text=No+Poster"
                    )

                    rating=details.get(
                    'rating',
                    'N/A'
                    )

                    year=details.get(
                    'year',
                    'N/A'
                    )

                    movie_type=details.get(
                    'type',
                    'N/A'
                    )

                    overview=details.get(
                    'overview',
                    'No description available'
                    )

                    st.image(
                    poster,
                    width=200
                    )

                    st.markdown(
                    f"""
                    ### {title}

                    ⭐ Rating: {rating}

                    📅 Year: {year}

                    🎥 Type: {movie_type}

                    🎯 Similarity: {score}%
                    """
                    )

                    st.caption(
                    overview
                    )

# -------------------------
# REAL BAR CHART
# -------------------------

st.write("---")

st.subheader(
"🎭 Genre Distribution"
)

movie_data=pd.read_csv(
"tmdb_5000_movies.csv"
)

all_genres=[]

for genre in movie_data['genres']:

    try:

        genres=ast.literal_eval(
        genre
        )

        for g in genres:

            all_genres.append(
            g['name']
            )

    except:
        pass


genre_count=Counter(
all_genres
)

top_genres=pd.DataFrame(

genre_count.most_common(10),

columns=[
'Genre',
'Count'
]
)

fig,ax=plt.subplots(
figsize=(8,4)
)

top_genres.plot(
kind='bar',
x='Genre',
y='Count',
ax=ax
)

ax.set_title(
"Top Genres from TMDB Dataset"
)

ax.set_xlabel(
"Genres"
)

ax.set_ylabel(
"Number of Movies"
)

st.pyplot(fig)

# -------------------------
# METRICS
# -------------------------

st.write("---")

c1,c2,c3=st.columns(3)

c1.metric(
"Movies",
len(movies)
)

c2.metric(
"Recommendations",
5
)

c3.metric(
"Algorithm",
"Content + Cosine"
)