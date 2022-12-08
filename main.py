import requests

base_url = 'https://rickandmortyapi.com/api'


def main_request(endpoint):
    response = requests.get(base_url + endpoint)
    return response.json()


def get_pages(response):
    return response.get('info').get('pages')

def parse_json(response):
    for character in response.get('results'):
        print(character.get('name'),len(character.get('episode')))
    return



if __name__ == '__main__':
    endpoint = '/character'

    data = main_request(endpoint)

    pages = get_pages(data)

    print(pages)

    parse_json(data)
