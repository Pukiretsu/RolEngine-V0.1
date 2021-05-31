import json as js

data = open("Jsontests.json")

data = js.load(data)

print(type(data))
