from util import FMSetlist, TicketMaster, get_api_key
from db import SQLEngine
from flask import Flask, request

app = Flask(__name__)

@app.route('/v1/setlist', methods=['GET'])
def generate_setlist():
    params = request.get_json()
    artistName = params['name']
    api_key = get_api_key.get_api_key()['spotify']
    FMSetlists = FMSetlist.FMSetlist(api_key)
    setList = FMSetlists.getSetlist(artistName=artistName)
    resp = { "setlist": [] }
    for tup in setList:
       resp["setlist"].append(tup[1])
    return resp, 200


@app.route('/v1/nearbyconcerts', methods=['GET'])
def get_nearby_concerts():
    params = request.get_json()
    location = params['location']
    api_key = get_api_key.get_api_key()['ticketmaster']
    TicketMasterObj = TicketMaster.TicketMaster(api_key)
    response = TicketMasterObj.getLocations(postalCode=location)
    print(response)
    return response, 200

# print(generate_setlist('Dua Lipa'))
# print(get_nearby_concerts('94704'))


@app.route('/v1/relatedartists', methods=['GET'])
def get_related_artists():
    params = request.get_json()
    target_artist = params['name']
    # login info
    host = "concertmanager.postgres.database.azure.com"
    dbname = "ConcertManager"
    user = "romitbarua@concertmanager"
    password = "concertManager1234!"
    sslmode = "require"

    engine = SQLEngine.SQLEngine(host, dbname, user, password, sslmode)

    related_artist_qry = f"select related_a_name.artistname \"Name\" from artists target_a inner join related_artists related_a on related_a.targetaid = target_a.aid inner join artists related_a_name on related_a_name.aid = related_a.relatedaid where target_a.artistname = '{target_artist}'"
    results = engine.query(related_artist_qry)
    print(results)
    return results, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)