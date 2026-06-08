from urllib.parse import quote

try:
    import requests
except ImportError:
    requests = None


def fallback_country_info(country_name):
    return {
        "name": country_name,
        "capital": "Demo Capital",
        "population": 123456,
        "region": "Demo Region",
    }


print("Welcome to Country Info Finder!")

country_name = input("Enter country name: ").strip()

if requests is None:
    info = fallback_country_info(country_name)
else:
    try:
        encoded_country = quote(country_name)
        response = requests.get(f"https://restcountries.com/v3.1/name/{encoded_country}", timeout=10)
        response.raise_for_status()
        data = response.json()[0]
        info = {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["Unknown"])[0],
            "population": data.get("population", 0),
            "region": data.get("region", "Unknown"),
        }
    except Exception:
        info = fallback_country_info(country_name)

print(f"Country: {info['name']}")
print(f"Capital: {info['capital']}")
print(f"Population: {info['population']}")
print(f"Region: {info['region']}")
