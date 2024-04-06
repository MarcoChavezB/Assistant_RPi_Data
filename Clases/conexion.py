import requests

url = 'https://api.github.com/users/andresgfranco'
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    print(data)

        

# def get_data_from_api(url):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         # Process the data here
#         return data
#     else:
#         print("Error: Failed to retrieve data from the API")
#         return None

# # Replace 'api_url' with the actual URL of the API you want to connect to
# api_url = 'https://api.example.com'
# data = get_data_from_api(api_url)

# if data:
#     # Do something with the data
#     print(data)