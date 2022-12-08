import requests

if __name__ == '__main__':
    base_url = 'https://rickandmortyapi.com/api'
    endpoint = '/character'

    response = requests.get(base_url + endpoint)

    print(response.text)

    data = response.json()

    print(data)
