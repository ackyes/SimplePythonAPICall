import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint # + query

response = requests.get(url)
breeds = response.json()["message"]

#get a list of all breeds from API call
all_breeds = breeds.keys()

# loop and print out each key
for breed in all_breeds:
  print(breed)

# displays all poodles subbreeds
poodle_subbreeds = breeds["poodle"]
input("Press enter to get all poodle subreeds")
for sub in poodle_subbreeds:
  print(sub)