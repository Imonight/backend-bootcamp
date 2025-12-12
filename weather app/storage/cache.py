import os
import json
import time

CACHE_FILE = "cache.json"


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(city, data):
    cache = load_cache()
    cache[city] = {"timestamp": time.time(), "data": data}
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)
