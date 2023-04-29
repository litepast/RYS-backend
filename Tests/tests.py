import requests
import time

url = 'http://127.0.0.1:5000/api/v1/insert-album-catalog/0RPeS6tlJfJt1GQ1XilhkH'

# Define the JSON data to send in the request body

# Send a POST request with the JSON data in the body
start= time.time()
response = requests.put(url)

# Print the response from the server
print(response.text)
end = time.time()
print('tiempo de todo ', end - start)


