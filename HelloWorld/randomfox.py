# Learning API's here

import requests

response = requests.get('https://randomfox.ca/floof', timeout=30)

# print(response.status_code)
# print(response.text)

# This will have a slightly different format appearance than the print statement above, but it is
# in the JSON format
# print(response.json())
# Now we can store the information in the variable below
fox = response.json()
print(fox['image'])
