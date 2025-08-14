import json
import os
import time
import requests

DATA_FILE = "/data/data.json"
HA_URL = "http://supervisor/core/api/states/sensor.home_service_next"
HEADERS = {
    "Authorization": "Bearer " + os.environ.get("SUPERVISOR_TOKEN"),
    "Content-Type": "application/json",
}

def send_state():
    if not os.path.exists(DATA_FILE):
        data = {"next_service_date": "2025-12-31"}
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    payload = {
        "state": data["next_service_date"],
        "attributes": {
            "friendly_name": "Next Service Date",
            "icon": "mdi:calendar-clock"
        }
    }
    resp = requests.post(HA_URL, headers=HEADERS, json=payload)
    print("HA API response:", resp.status_code, resp.text)

if __name__ == "__main__":
    print("Home Service Notifier running...")
    while True:
        send_state()
        time.sleep(3600)  # Päivitä kerran tunnissa

