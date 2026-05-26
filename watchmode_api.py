import requests

api_key = "jIFOwkfaqzk6NNJQG6gA10GFzRKe3mB6fsarUDNJ"

def get_movie_details(movie):

    url = f"https://api.watchmode.com/v1/search/?apiKey={api_key}&search_field=name&search_value={movie}"

    response = requests.get(url)
    data = response.json()

    try:

        result = data['title_results'][0]

        return {

            "title": result.get('name',"N/A"),
            "year": result.get('year',"N/A"),
            "type": result.get('type',"N/A"),
            "rating": result.get('user_rating',"N/A"),
            "overview": result.get('plot_overview',"No description available"),
            "poster": result.get(
                'poster',
                "https://via.placeholder.com/200x300.png?text=No+Poster"
            )

        }

    except:

        return None
    

    #"jIFOwkfaqzk6NNJQG6gA10GFzRKe3mB6fsarUDNJ"