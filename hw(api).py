import requests

response = requests.get('https://rickandmortyapi.com/api')
print(response.json())

morty = requests.get('https://rickandmortyapi.com/api/character/2')
print(morty.json())

status_unknown = requests.get('https://rickandmortyapi.com/api/character/?status=unknown')
print(status_unknown.json())

data = status_unknown.json()
carachters = data['results']
names = [carachter['name'] for carachter in carachters]
print(names)

with_error = requests.get('https://rickandmortyapi.com/api/character/?status=unknowntrnbbw')
if with_error.status_code == 404:
    print('404 error')
else:
    print('All great')

url = 'https://jsonplaceholder.typicode.com/todos'
data = {
    'userId': 13,
    'title': 'In search of Nemo',
    'completed': 'False'
}
response = requests.post(url, data)
if response.status_code == 201:
    print('Data post successful')
else:
    print(f'Error {response.status_code}')