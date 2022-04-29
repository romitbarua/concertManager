import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

class Spotify:
    
    def __init__(self, client_id, client_secret, redirect_uri, username, scope):
        
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.username = username
        self.scope = scope
        self.sp_scc = None
        self.sp_soa = None
        
    def connectClientCredentials(self):
        auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp_scc = spotipy.Spotify(auth_manager=auth_manager)
        
    def connectOAuth(self):
        auth_manager = SpotifyOAuth(client_id=self.client_id,
                            client_secret=self.client_secret,
                            redirect_uri=self.redirect_uri,
                            username=self.username,
                           scope=self.scope)
        self.sp_soa = spotipy.Spotify(auth_manager=auth_manager)
        
    def getArtistID(self, artist):
        artist_data = self.sp_scc.search(q='artist:' + artist, type='artist')
        artist_id = artist_data['artists']['items'][0]['id']
        return artist_id
        
    def getRelatedArtists(self, target_artist):
        if self.sp_scc == None:
            self.connectClientCredentials()
        
        artist_id = self.getArtistID(target_artist)
        related_artists = self.sp_scc.artist_related_artists(artist_id)
        
        related_artist_df = pd.DataFrame(columns=['TargetArtistName', 'TargetArtistSpotifyID', 'RelatedArtistName', 'RelatedArtistSpotifyID'])
        
        for artist in related_artists['artists']:
            related_artist_df = related_artist_df.append(pd.DataFrame([[target_artist, artist_id, artist['name'], artist['id']]], columns=['TargetArtistName', 'TargetArtistSpotifyID', 'RelatedArtistName', 'RelatedArtistSpotifyID']))
            
        return related_artist_df