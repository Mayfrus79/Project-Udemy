import requests
 
 # http:// -> 80
 # https:// -> 443
url = 'https://www.tecmundo.com.br/?ab=true&'
response = requests.get(url)
 
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
# print(response.headers)
print(response.text)
