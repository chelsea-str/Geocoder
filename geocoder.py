import requests


def extract_cords(contact, address, name):
    var_dict = {'contact': contact, 'address': address, 'name': name}
    place_api = 'YOUR_PLACE_API_KEY'
    geocode_api = 'YOUR_GEOCODE_API_KEY'
    base_url = "https://maps.googleapis.com/maps/api/"
    place_api_url = f"place/textsearch/json?query={contact or name}&key={place_api}&region=ZA"
    geocode_api_url = f"geocode/json?address={address}&key={geocode_api}&region=ZA"
    cords_list = []

    for item, value in var_dict.items():
        if item == 'contact' or item == 'name':
            url = base_url + place_api_url
            geo = requests.get(url)
        else:
            url = base_url + geocode_api_url
            geo = requests.get(url)
        if geo.status_code not in range(200, 299):
            cords_list.append('None')
            cords_list.append('None')
        else:
            retry_count = 0
            while retry_count < 3:
                try:
                    results = geo.json()['results'][0]
                    lat = results['geometry']['location']['lat']
                    lng = results['geometry']['location']['lng']
                    if lat < -34.83 or lat > -22.12 or lng < 16.49 or lng > 32.89:
                        cords_list.append('None')
                        cords_list.append('None')
                    else:
                        cords_list.append(lat)
                        cords_list.append(lng)
                    break
                except (KeyError, IndexError):
                    cords_list.append('None')
                    cords_list.append('None')
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    retry_count += 1
                    if retry_count == 3:
                        cords_list.append('None')
                        cords_list.append('None')
                        break
                    else:
                        continue
    print(cords_list)


