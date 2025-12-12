import requests, time
from tenacity import retry, stop_after_attempt, wait_fixed
from storage.cache import save_cache, load_cache

API_KEY = "5b3cd51ea288473311b108715ac6e0af"
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

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    weather = get_weather(city)
    print("\nWeather data: ")
    print("Description:", weather["weather"][0]["description"])
    print("Temperature:", weather["main"]["temp"])
    print("feels like", weather["main"]["feels_like"])


