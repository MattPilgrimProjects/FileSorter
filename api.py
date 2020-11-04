import requests
import app
import library

def spotify_web_api(params):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': app.settings["spotify_api"],
    }

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

    return response.json()


params = (
    ('q', 'Slipknot wait and bleed'),
    ('type', 'track,artist'),
    ('limit', '20'),
    ('market','US'),
    ('include_external','audio')

)


content = spotify_web_api(params)

library.json.export_json("slipknot-wait-and-bleed.json",content)

# https://musicbrainz.org/ws/2/artist/?query=slipknot%20wait%20and%20bleed&fmt=json

# https://musicbrainz.org/ws/2/url/?query=Slipknot&fmt=json

# <iframe src="https://open.spotify.com/embed/album/2dL9Q5AtIv4Rw1L6lKcIUc" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>


# <iframe width="560" height="315" src="https://www.youtube.com/embed/B1zCN0YhW1s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>