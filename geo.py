import pandas as pd
import os
from geopy import geocoders
from geopy.geocoders import GoogleV3

API_KEY = os.getenv("API1234")
g = GoogleV3(api_key=API_KEY)


loc_coordinates = []
loc_address = []
for address in df.Address:
    try:
        inputAddress = address
        location = g.geocode(inputAddress, timeout=15)
        loc_coordinates.append((location.latitude, location.longitude))
        loc_address.append(inputAddress)
    except Exception as e:
        print('Error, skipping address...', e)


df_geocodes = pd.DataFrame({'coordinate':loc_coordinates,'address':loc_address})
