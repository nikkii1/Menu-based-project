#!/usr/bin/env python3

import cgi
import cgitb
import json
from geopy.geocoders import Nominatim

cgitb.enable()  # Enable debugging

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    form = cgi.FieldStorage()
    address = form.getvalue('address')

    if not address:
        response = {"error": "Address is required"}
        print(json.dumps(response))
        return

    try:
        # Initialize geolocator and get the latitude and longitude
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.geocode(address)

        if location:
            response = {
                "address": address,
                "latitude": location.latitude,
                "longitude": location.longitude
            }
        else:
            response = {"error": "Address not found"}
    except Exception as e:
        response = {"error": str(e)}

    print(json.dumps(response))

if __name__ == "__main__":
    main()