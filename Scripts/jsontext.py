import json as js

data = open("Data/Jsontests.json")
data = js.load(data)

print(type(data))
print(data)