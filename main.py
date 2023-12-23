import requests
import json
import os

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)
data = response.json()

with open('todos.json', 'w') as file:
    json.dump(data, file)

with open('todos.json', 'r') as file:
    todos = json.load(file)

for i, todo in enumerate(todos):
    with open(f'todo_{i+1}.json', 'w') as file:
        json.dump(todo, file)