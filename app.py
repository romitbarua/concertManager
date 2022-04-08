from util import FMSetlist, TicketMaster, get_api_key

def generate_setlist(artistName):
    api_key = get_api_key.get_api_key()['spotify']
    FMSetlists = FMSetlist.FMSetlist(api_key)
    return FMSetlists.getSetlist(artistName=artistName)
    
def get_nearby_concerts(location):
    api_key = get_api_key.get_api_key()['ticketmaster']
    TicketMasterObj = TicketMaster.TicketMaster(api_key)
    return TicketMasterObj.getLocations(postalCode=location)

# print(generate_setlist('Dua Lipa'))
# print(get_nearby_concerts('94704'))