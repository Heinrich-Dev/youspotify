import spotipy
import os
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, session, url_for, redirect, request

'''
-- SOURCES --
Synsation's Spotify OAuth: Automating Discover Weekly Playlist - Full Tutorial -- https://www.youtube.com/watch?v=mBycigbJQzA&t
Spotipy's ReadTheDocs Page -- https://spotipy.readthedocs.io/en/2.22.1/#authorization-code-flow
Flask's Project Documentation -- https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
Flask's Deploying to Production Documentation -- https://flask.palletsprojects.com/en/3.0.x/deploying/
'''

#create app
app = Flask(__name__)

app.config['SESSION_NAME'] = 'Spotify'
app.secret_key = os.getenv('SESSION_SECRET_KEY')
TOKEN = 'token'

@app.route("/")
def authenticate():
    url = create_authenticator().get_authorize_url()
    return redirect(url)

@app.route("/redirect")
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token = create_authenticator().get_access_token(code)
    session[TOKEN] = token
    return redirect(url_for('saveTinyDesk', external = True))
    
@app.route("/tinydesk")
def saveTinyDesk():
    try:
        token = get_token()
    except:
        return redirect('/')
    return("AUTH SUCCESS")

def create_authenticator():
    #requires the environment variables to be set: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
    scope = 'user-library-read playlist-modify-public playlist-modify-private'
    return SpotifyOAuth(redirect_uri=url_for('redirect_page', _external = True), scope=scope)

def get_new_token():
    token = session.get(TOKEN, None)
    if not token:
        redirect(url_for('authenticate', external=False))
    
    now = int(time.time())
    if(token['expires_at'] - now < 60):
        auth = create_authenticator()
        token = auth.refresh_access_token(token['refresh-token'])