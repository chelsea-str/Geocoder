def extract_lat_long_via_address(name, address_or_zipcode):
    import requests
    lat, lng = [], []
    geocode_api = 'AIzaSyCEVftlo0qT468oe778T91KgHI-lAkt1pQ'
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address_or_zipcode}&key={geocode_api}&region=ZA"
    geo = requests.get(geocode_url)
    if geo.status_code not in range(200, 299):
        return None, None
    try:
        results = geo.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
        if lat < -34.83 or lat > -22.12 or lng < 16.49 or lng > 32.89:
            return None, None
    except:
        pass
    p_lat, p_lng = [], []
    place_api = 'AIzaSyDpJDTavW7QSThSE0veqoWkcBAkHYjwHpI'
    place_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&key={place_api}&region=ZA"
    place_url = place_url.replace(" ", "%20")
    place = requests.get(place_url)
    if place.status_code not in range(200, 299):
        return None, None
    try:
        results = place.json()['results'][0]
        p_lat = results['geometry']['location']['lat']
        p_lng = results['geometry']['location']['lng']
    except:
        pass
    print(lat, lng)
    print(p_lat, p_lng)


extract_lat_long_via_address('Atterbury Bird & Animal Hospital', ' Atterbury Road, Menlo Park, 0081')
