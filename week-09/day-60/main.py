try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except ImportError:
    webdriver = None
    By = None

print("Welcome to Auto Form Filler Demo!")

form_data = {
    "name": "Nayem",
    "email": "nayem@example.com",
    "message": "This is a demo form submission.",
}

if webdriver is None:
    print("Selenium is not installed. Demo mode only.")
    for key, value in form_data.items():
        print(f"Would fill {key} = {value}")
else:
    print("Selenium is available. Add a target URL before running live automation.")
    for key, value in form_data.items():
        print(f"Prepared field {key} = {value}")
