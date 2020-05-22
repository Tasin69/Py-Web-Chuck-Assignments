# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to
#  http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
#  contact a web service and retrieve JSON for the web service and parse that data,
#  and retrieve the first place_id from the JSON. A place ID is a textual identifier
#  that uniquely identifies a place as within Google Maps.

# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset
#  of the Google Data:

# http://py4e-data.dr-chuck.net/json?

# This API uses the same parameter (address) as the Google API.
#  This API also has no rate limit so you can test as often as you like.
#  If you visit the URL with no parameters, you get "No address..." response.

# To call the API, you need to include a key= parameter and provide the address that you
#  are requesting as the address= parameter that is properly URL encoded using the
#  urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint is as shown above.
# You will get different results from the geojson and json endpoints so make sure
#  you are using the same end point as this autograder is using. 

import urllib as ub
import json

# Basic url to api before we add the location
service_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    addr = input("Enter location: ")
    if len(addr) < 1: break
    params = {'address' : addr, 'key' : 42}
    url = service_url + ub.parse.urlencode(params) # Final url created by
    print('Retrieving', url)                                   #  merging the address
    
    uh = ub.request.urlopen(url)
    data = uh.read().decode()
    
    # If the final url is fine, load the json data. Otherwise, make it None
    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('\n............Failed to retrieve.............')
        continue
    print('\nPlace ID:',json_data['results'][0]['place_id'])