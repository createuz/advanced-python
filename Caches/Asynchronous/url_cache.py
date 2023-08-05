import json
import httpx


async def fetch_data(*, update: bool = False, json_cache: str, url: str):
    if not update:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                print('✅ Fetched data from local cache!')
                return json_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'No local cache found... ({e})')

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            if response.text:
                json_data = response.json()
                with open(json_cache, 'w') as file:
                    json.dump(json_data, file)
                return json_data
            else:
                print('Empty response received.')
        except httpx.HTTPError as http_ex:
            print(f"HTTP Exception: {http_ex}")
        except json.JSONDecodeError as json_ex:
            print(f"JSON Decode Error: {json_ex}")
    return None


if __name__ == '__main__':
    url = 'https://dummyjson.com/comments'
    json_cache = 'comments.json'

    import asyncio

    data = asyncio.run(fetch_data(update=False, json_cache=json_cache, url=url))
    if data is not None:
        print(data)
