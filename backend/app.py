
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests
# from config import GEMINI_API_KEY, GEMINI_API_ENDPOINT
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# app = Flask(__name__)
# CORS(app)

# @app.route('/generate-playlist', methods=['POST'])
# def generate_playlist():
#     data = request.get_json()
#     mood = data.get('mood', '')

#     # Call Gemini API to get keywords/genres/artists
#     headers = {
#         "Content-Type": "application/json"
#     }
#     params = {
#         "key": GEMINI_API_KEY
#     }
#     payload = {
#         "contents": [
#             {"parts": [{"text": f"Suggest music genres, keywords, or artists for this mood: {mood}. Respond with a comma-separated list."}]}
#         ]
#     }
#     try:
#         gemini_response = requests.post(GEMINI_API_ENDPOINT, headers=headers, params=params, json=payload)
#         gemini_response.raise_for_status()
#         gemini_data = gemini_response.json()
#         # Parse Gemini response for suggestions
#         suggestions = ""
#         if "candidates" in gemini_data and gemini_data["candidates"]:
#             suggestions = gemini_data["candidates"][0]["content"]["parts"][0]["text"]
#         else:
#             suggestions = "pop, happy, upbeat"
#     except Exception as e:
#         suggestions = "pop, happy, upbeat"

#     # Use Spotify API to search for tracks
#     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#         client_id=SPOTIFY_CLIENT_ID,
#         client_secret=SPOTIFY_CLIENT_SECRET
#     ))
#     # Use the first suggestion as the search query
#     search_query = suggestions.split(',')[0].strip() if suggestions else mood
#     results = sp.search(q=search_query, type='track', limit=5)
#     tracks = []
#     for item in results['tracks']['items']:
#         tracks.append({
#             "title": item['name'],
#             "artist": item['artists'][0]['name'],
#             "album_art": item['album']['images'][0]['url'] if item['album']['images'] else ""
#         })

#     playlist = {
#         "tracks": tracks,
#         "mood": mood,
#         "gemini_suggestions": suggestions
#     }
#     return jsonify(playlist)

# if __name__ == '__main__':
#     app.run(debug=True)

import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# --- CONFIG IMPORTS ---
from config import GEMINI_API_KEY, GEMINI_API_ENDPOINT
from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# --- SETUP ---
app = Flask(__name__)
CORS(app) 

# --- SPOTIFY AUTHENTICATION (App-Only, No User Login) ---
# This uses your developer credentials to search for public song data.
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# --- RECOMMENDATION ROUTE ---
@app.route('/api/get-recommendations', methods=['POST'])
def get_recommendations():
    mood = request.get_json().get('mood', 'happy')
    
    prompt = f"Suggest 5 comma-separated keywords for a Spotify search based on the mood: {mood}"
    
    gemini_payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        gemini_response = requests.post(f"{GEMINI_API_ENDPOINT}?key={GEMINI_API_KEY}", json=gemini_payload)
        gemini_response.raise_for_status() # Raise an error for bad responses
        suggestions = gemini_response.json()["candidates"][0]["content"]["parts"][0]["text"]
        search_query = suggestions.split(',')[0].strip()
    except Exception as e:
        # If Gemini fails, use the original mood as the search query
        print(f"Gemini call failed: {e}")
        search_query = mood

    # Search Spotify for tracks using the query
    results = sp.search(q=search_query, type='track', limit=20)
    
    # Format the tracks into a simple list
    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            "title": item['name'],
            "artist": item['artists'][0]['name'],
            # Get the smallest available album art image
            "album_art": item['album']['images'][-1]['url'] if item['album']['images'] else ""
        })

    return jsonify({"tracks": tracks})

# --- STARTS THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True, port=8888)