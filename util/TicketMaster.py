import requests
import json

class TicketMaster:
    
    def __init__(self, api_key, response_type='application/json'):
        
        self.headers = {'Accept': response_type, 'Content-Type': 'application/json'}
    
    def getJsonResponse(self, url_base, params):
        
        response = requests.get(url_base, headers=self.headers, params=params)
        return json.loads(response.text)
    
    def getLocations(self, **params):
        
        url_base = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey=M81pNFXZAR8GC7mteoDUdALwVk8ly2sI'
        json = self.getJsonResponse(url_base, params)
        response = {"events": []}
        for event in json["_embedded"]["events"]:
            temp = {}
            temp['name'] = event['name']
            temp['locale'] = event['locale']
            temp['dates'] = event['dates']
            response['events'].append(temp)
        return response
            