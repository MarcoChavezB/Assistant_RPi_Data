import requests

url = 'https://api.github.com/users/andresgfranco'
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    print(data)

        

