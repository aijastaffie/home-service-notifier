import json
import os

DATA_FILE = "/data/data.json"  # polku missä data.json säilyy addonissa

def main():
    print("Home Service Notifier test mode")
    
    # Pyydetään syöte
    next_service = input("Enter next service date (YYYY-MM-DD): ")
    
    # Tallennetaan JSON-muodossa
    data = {
        "next_service_date": next_service
    }
    
    # Varmistetaan että kansio on olemassa
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    
    print(f"Data saved to {DATA_FILE}")

if __name__ == "__main__":
    main()

