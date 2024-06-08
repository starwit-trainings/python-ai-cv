# how to interact with JSON 

import json
from datetime import datetime

weatherSample = '''{
	"RESPONSE": {
		"RESULT": [
			{
				"WeatherObservation": [
					{
						"Sample": "2024-04-29T11:28:38.387+02:00",
						"Wind": [
							{
								"Height": 6
							}
						],
						"Id": "220735110",
						"Measurepoint": {
							"Id": 327,
							"Name": "Björklinge",
							"Geometry": {
								"SWEREF99TM": "POINT (646031.715 6659820.374)",
								"WGS84": "POINT (17.62248 60.0495)"
							}
						},
						"ModifiedTime": "2024-04-29T09:31:36.800Z",
						"Deleted": false
					}
				]
			}
		]
	}
}'''

#convert static example to Python object
weatherParsed = json.loads(weatherSample)
print(weatherParsed['RESPONSE']['RESULT'])

# reading from a file - Note: exception handling
with open("07-sample-data.json") as f:
    weatherParsed = json.load(f) # Note the subtle difference
print(len(weatherParsed['RESPONSE']['RESULT'][0]['WeatherObservation']))

for datapoint in weatherParsed['RESPONSE']['RESULT'][0]['WeatherObservation']:
    print("Data for ",datapoint['Id'])
    if 'Air' in datapoint:
        parsedDateTime = datetime.strptime(datapoint['ModifiedTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        print(parsedDateTime, datapoint['Air']['Temperature'])

# Tasks
# collect all (!) temperatures, WGS coordinates, Timestamp and ouput as a list
# can we display datetime better?

# Data structure is fairly complicated - save all found temperatures in a flat list
