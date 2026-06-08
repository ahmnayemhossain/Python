try:
    import requests
except ImportError:
    requests = None


def fallback_weather(city_name):
    return {
        "city": city_name,
        "temperature_c": "29",
        "description": "Partly cloudy (demo data)",
    }


print("Welcome to Weather Checker CLI!")

city_name = input("Enter city name: ").strip()

if requests is None:
    weather = fallback_weather(city_name)
else:
    try:
        response = requests.get(f"https://wttr.in/{city_name}?format=j1", timeout=10)
        response.raise_for_status()
        data = response.json()
        weather = {
            "city": city_name,
            "temperature_c": data["current_condition"][0]["temp_C"],
            "description": data["current_condition"][0]["weatherDesc"][0]["value"],
        }
    except Exception:
        weather = fallback_weather(city_name)

print(f"City: {weather['city']}")
print(f"Temperature: {weather['temperature_c']} C")
print(f"Condition: {weather['description']}")
