import requests

url = 'https://www.websiteplanet.com/pt-br/'

# Send a GET request to the API
response = requests.get(url)

# Check the status code and respond accordingly
if response.status_code == 200:
    print("✅ Everything is fine!")
    users = response.json()
    print("\nUser List:")
    for user in users:
        print(f"- {user['name']} ({user['email']})")

elif response.status_code == 400:
    print("❌ Bad request (400).")
elif response.status_code == 401:
    print("❌ Unauthorized (401).")
elif response.status_code == 404:
    print("❌ Resource not found (404).")
elif response.status_code >= 500:
    print("❌ Server error (5xx).")
else:
    print(f"⚠️ Unexpected status code: {response.status_code}")
