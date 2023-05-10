import requests
import time


def extract_cords(contact, address, name):
    var_dict = {'contact': contact, 'address': address, 'name': name}
    key = 'YOUR_PLACE_API_KEY'
    base_url = "https://maps.googleapis.com/maps/api/"
    place_url = f"place/textsearch/json?query={contact or name}&key={key}&region=ZA"
    geocode_url = f"geocode/json?address={address}&key={key}&region=ZA"
    cords_list = []

    for item, value in var_dict.items():
        current_delay = 0.1
        max_delay = 600
        if item == 'contact' and item is not None or item == 'name':
            url = base_url + place_url
        else:
            url = base_url + geocode_url

        while True:
            try:
                geo = requests.get(url)
            except IOError:
                pass
            else:
                if geo.status_code in range(200, 299):
                    try:
                        results = geo.json()['results'][0]
                        lat = results['geometry']['location']['lat']
                        lng = results['geometry']['location']['lng']
                        if lat < -34.83 or lat > -22.12 or lng < 16.49 or lng > 32.89:
                            cords_list.append('Wrong co-ordinates')
                            cords_list.append('Wrong co-ordinates')
                        else:
                            cords_list.append(lat)
                            cords_list.append(lng)
                        break
                    except IndexError:
                        pass
                elif geo.status_code in range(200, 299):
                    cords_list.append('Unsuccessful')
                    cords_list.append('Unsuccessful')
                    break

            if current_delay > max_delay:
                print('Taking too long')
                cords_list.append('Took too long')
                cords_list.append('Took too long')
                break
            print(f'Waiting {current_delay} seconds before retrying.')
            time.sleep(current_delay)
            current_delay *= 2
    return cords_list
