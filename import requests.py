import requests
city = 'toronto'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'kIyHHXCx2QZtVzD9a5Dfdw==fqRavo7YTrtwuwPB'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)