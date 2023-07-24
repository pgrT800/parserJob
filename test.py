import requests

response = requests.get('https://www.youtube.com/watch?v=7R5hrrr4rTs')
print(response.status_code)