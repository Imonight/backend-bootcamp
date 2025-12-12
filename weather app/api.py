import time
import requests
from dotenv import load_dotenv
import os
from tenacity import retry, stop_after_attempt, wait_fixed
from storage.cache import load_cache, save_cache

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CACHE_EXPIRE= 60 * 60

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetching_weather(city):
    params = {"q":city, "appid":API_KEY, "units":"metric"}
    response = requests.get(BASE_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()

def get_weather(city):
    cache = load_cache()
    if city in cache:
        stored = cache[city]
        age = time.time() - stored["timsestamp"]
        if age < CACHE_EXPIRE:
            print(f"loading city {city} from cache")
            return stored["data"]
        else:
            print(f"Cache expired, refreshing {city}")
                
    print(f"fetching city {city} from api")
    try:
        print(f"fetching data through api")
        data = fetching_weather(city)
    except requests.exceptions.RequestException as e:
        print("Network Issues")
        return None
    
    cache[city] = data
    save_cache(city, data)
    return data
