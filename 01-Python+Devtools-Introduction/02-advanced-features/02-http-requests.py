import requests
import tempfile
import os

# simple request example, that calls a time server
def timeExample():
    url = "http://worldtimeapi.org/api/timezone/Europe/Berlin"
    resp = requests.get(url)
    print(resp.json())

# how to download a binary file e.g. zip files
def zipDownload():
    # Download a zip file
    url = "https://starwit-technologies.de/wp-content/uploads/2024/05/temperature-data.zip"
    resp = requests.get(url, stream=True)
    with open(tempfile.gettempdir()+"/temperature-data.zip", 'wb') as fd:
        for chunk in resp.iter_content(chunk_size=128):
            fd.write(chunk)

# how to query Sweden's trafikverket example
def trafikverketAPI():
    if os.environ['TRAFIKVERKET_API_KEY']:
        query = '<REQUEST>'
        query += '  <LOGIN authenticationkey="{}"/>'.format(os.environ['TRAFIKVERKET_API_KEY'])
        query += '  <QUERY objecttype="WeatherObservation" schemaversion="1" limit="20">'
        query += '    <FILTER></FILTER>'
        query += '  </QUERY>'
        query += '</REQUEST>'

        headers = {'Content-type': 'text/xml'}
        resp = requests.post("https://api.trafikinfo.trafikverket.se/v2/data.json", headers=headers, data=query)
        return resp.json()

timeExample()
zipDownload()
data = trafikverketAPI()

# Tasks
# write a function, that collects all temperature data from Trafikverket - use as much code as possible from example 07 from last section