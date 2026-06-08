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


def demo_convert(base_currency, target_currency, amount):
    demo_rates = {"USD": 110.0, "EUR": 120.0, "BDT": 1.0}
    base_rate = demo_rates.get(base_currency, 1.0)
    target_rate = demo_rates.get(target_currency, 1.0)
    return amount * base_rate / target_rate


load_env_file()

print("Welcome to Currency Converter with API!")

base_currency = input("Enter base currency: ").strip().upper()
target_currency = input("Enter target currency: ").strip().upper()
amount = float(input("Enter amount: "))

api_key = os.getenv("EXCHANGE_RATE_API_KEY")

if requests is None or not api_key:
    converted_amount = demo_convert(base_currency, target_currency, amount)
    print("Using demo conversion data.")
else:
    try:
        response = requests.get(
            f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}",
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        rate = data["conversion_rates"][target_currency]
        converted_amount = amount * rate
    except Exception:
        converted_amount = demo_convert(base_currency, target_currency, amount)
        print("Using demo conversion data.")

print(f"Converted amount: {converted_amount:.2f} {target_currency}")
