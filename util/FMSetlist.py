import requests
import json

class FMSetlist:
    
    def __init__(self, api_key, response_type='application/json'):
        
        self.headers = {'Accept':response_type, 'x-api-key':api_key}
    
    def getJsonResponse(self, url_base, params):
        
        response = requests.get(url_base, headers=self.headers, params=params)
        return json.loads(response.text)
    
    def getSetlist(self, **params):
        
        url_base = 'https://api.setlist.fm/rest/1.0/search/setlists'
        json = self.getJsonResponse(url_base, params)
        
        setlist = []
        main_artist = json['setlist'][0]['artist']['name']
        setlist_json = json['setlist'][0]['sets']['set']
        
        for songs_json in setlist_json:
            for song in songs_json['song']:
                song_name = song['name']
                if 'cover' in song.keys():
                    cover_artist = song['cover']['name']
                    setlist.append((cover_artist, song_name))
                else:
                    setlist.append((main_artist, song_name))
        print(setlist)
        return setlist