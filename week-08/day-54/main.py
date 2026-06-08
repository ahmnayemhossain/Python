try:
    import requests
except ImportError:
    requests = None


def demo_request(method_name, endpoint, payload=None):
    print(f"{method_name} -> {endpoint}")
    if payload:
        print(f"Payload: {payload}")


print("Welcome to Habit Tracker API Client!")

base_url = "https://httpbin.org"
habit_name = input("Enter habit name: ").strip()

if requests is None:
    print("Requests not available. Running in demo mode.")
    demo_request("POST", f"{base_url}/post", {"habit": habit_name})
    demo_request("PUT", f"{base_url}/put", {"habit": habit_name, "status": "done"})
    demo_request("DELETE", f"{base_url}/delete", {"habit": habit_name})
else:
    try:
        post_response = requests.post(f"{base_url}/post", json={"habit": habit_name}, timeout=10)
        put_response = requests.put(
            f"{base_url}/put",
            json={"habit": habit_name, "status": "done"},
            timeout=10,
        )
        delete_response = requests.delete(f"{base_url}/delete", json={"habit": habit_name}, timeout=10)
        print(f"POST status: {post_response.status_code}")
        print(f"PUT status: {put_response.status_code}")
        print(f"DELETE status: {delete_response.status_code}")
    except Exception:
        print("Network failed. Running in demo mode.")
        demo_request("POST", f"{base_url}/post", {"habit": habit_name})
        demo_request("PUT", f"{base_url}/put", {"habit": habit_name, "status": "done"})
        demo_request("DELETE", f"{base_url}/delete", {"habit": habit_name})
