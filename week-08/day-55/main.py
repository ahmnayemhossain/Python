import os
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None


def load_env_file():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


load_env_file()

print("Week 08 Exam - Weather App Using API Safely")

city_name = input("Enter city name: ").strip()
api_base_url = os.getenv("WEATHER_API_URL", "https://wttr.in")

if requests is None:
    print("Requests not available. Using safe demo result.")
    print(f"{city_name}: 29 C, Partly cloudy")
else:
    try:
        response = requests.get(f"{api_base_url}/{city_name}?format=j1", timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        print(f"{city_name}: {current['temp_C']} C, {current['weatherDesc'][0]['value']}")
    except Exception:
        print("API failed. Using safe demo result.")
        print(f"{city_name}: 29 C, Partly cloudy")
