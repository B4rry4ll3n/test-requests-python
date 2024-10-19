import requests as rq

url = "https://jsonplaceholder.typicode.com/todos/1"
response = rq.get(url)

# Print the response in JSON format
print(response.json())
