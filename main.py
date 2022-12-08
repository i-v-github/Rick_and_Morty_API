import requests

base_url = 'https://rickandmortyapi.com/api'


def main_request(endpoint, i):
    response = requests.get(base_url + endpoint + f'?page={i}')
    return response.json()


def get_pages(response):
    return response.get('info').get('pages')


def parse_json(response):
    charlist = []
    for item in response.get('results'):
        char = {
            'name': item.get('name'),
            'no_ep': len(item.get('episode'))
        }
        charlist.append(char)
    return charlist


if __name__ == '__main__':
    endpoint = '/character'

    data = main_request(endpoint,1)
    pages = get_pages(data)

    mainlist = []

    for i in range(1,pages+1):
        print(i)
        data = main_request(endpoint, i)
        charlist = parse_json(data)
        mainlist.extend(charlist)

    print(pages)

    print(len(mainlist))
