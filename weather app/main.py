from api import get_weather

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    weather = get_weather(city)
    print("\nWeather data: ")
    print("Description:", weather["weather"][0]["description"])
    print("Temperature:", weather["main"]["temp"])
    print("feels like", weather["main"]["feels_like"])
