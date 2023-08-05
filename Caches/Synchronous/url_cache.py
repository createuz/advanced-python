import json
import requests


def fetch_data(*, update: bool = False, json_cache: str, url: str):
    if not update:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                print('Fetched data from local cache!')
                return json_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'No local cache found... ({e})')

    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.text:
            json_data = response.json()
            with open(json_cache, 'w') as file:
                json.dump(json_data, file)
            return json_data
        else:
            print('Empty response received.')
    except requests.exceptions.RequestException as req_ex:
        print(f"Request Exception: {req_ex}")
    except json.JSONDecodeError as json_ex:
        print(f"JSON Decode Error: {json_ex}")
    return None


if __name__ == '__main__':
    url = 'https://dummyjson.com/comments'
    json_cache = 'comments.json'

    data: dict = fetch_data(update=False, json_cache=json_cache, url=url)
    if data is not None:
        print(data)
