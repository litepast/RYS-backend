# import requests
# import time

# url = 'http://127.0.0.1:5000/api/v1/insert-album-catalog/1oNccmu6KxWyQnGi9P7g5u'

# # Define the JSON data to send in the request body

# # Send a POST request with the JSON data in the body
# start= time.time()
# response = requests.put(url)

# # Print the response from the server
# print(response.text)
# end = time.time()
# print('tiempo de todo ', end - start)

import json

# Sample array of dictionaries
data = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    },
    {
        "name": "Bob",
        "age": 35,
        "city": "Seattle"
    }
]

# Convert array of dictionaries to JSON string
json_data = json.dumps(data)

# Write JSON string to a file
with open("data.json", "w") as json_file:
    json_file.write(json_data)


