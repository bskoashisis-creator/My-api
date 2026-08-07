import os
import json
import requests

url = os.environ.get("API_URL")
token = os.environ.get("API_TOKEN")

try:
    response = requests.get(url, params={"token": token}, timeout=10)
    data = response.json()

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Successfully updated data.json!")

except Exception as e:
    print("Error:", e)
