import requests
import json


def get_homeworld_info(url):
    homeworld_response = requests.get(url)
    homeworld_data = homeworld_response.json()
    return {
        'name': homeworld_data['name'],
        'population': homeworld_data['population'],
        'terrain': homeworld_data['terrain']
    }

def get_starship_info(starship_name):
    api_url = f'https://swapi.dev/api/starships/'
    response = requests.get(api_url, params={'search': starship_name})
    data = response.json()

    if data['count'] == 0:
        return None

    starship = data['results'][0]
    pilots_info = []

    for pilot_url in starship['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()

        homeworld_info = get_homeworld_info(pilot_data['homeworld'])

        pilot_info = {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'weight': pilot_data['mass'],
            'homeworld': pilot_data['homeworld'],
            'homeworld_info': homeworld_info
        }

        pilots_info.append(pilot_info)

    starship_info = {
        'max_atmosphering_speed': starship['max_atmosphering_speed'],
        'pilots': pilots_info,
        'ship_name': starship['name'],
        'starship_class': starship['starship_class']
    }

    return starship_info

def main():
    starship_name = 'Millennium Falcon'
    starship_info = get_starship_info(starship_name)

    if starship_info:
        # Вывести в консоль
        print(json.dumps(starship_info, indent=4))

        # Сохранить в JSON-файл
        with open('millennium_falcon_info.json', 'w') as json_file:
            json.dump(starship_info, json_file, indent=4)

if __name__ == "__main__":
    main()
