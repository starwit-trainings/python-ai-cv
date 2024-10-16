import requests

url = "http://worldtimeapi.org/api/timezone/Europe/Berlin"
response = requests.post(url)
print(response.elapsed.total_seconds())