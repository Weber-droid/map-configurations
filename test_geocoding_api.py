import requests
import json

def test_geocoding_api(api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    
    params = {
        "address": address,
        "key": api_key
    }
    
    print(f"Testing API Key with address: {address}...")
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]
            print("Success!")
            print(f"Coordinates: Latitude {lat}, Longitude {lng}")
            
        elif data["status"] == "REQUEST_DENIED":
            print("Request Denied.")
            print(f"Error Message: {data.get('error_message', 'No message provided.')}")
            print("\nCheck if 'Geocoding API' is enabled in your Google Cloud Console.")
            
        else:
            print(f"API returned status: {data['status']}")
            if "error_message" in data:
                print(f"Error: {data['error_message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    MY_KEY = ' Go get your api keyy brooo'
    test_geocoding_api(MY_KEY)
