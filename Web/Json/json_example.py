import json

people_string = '''
{
 "people": [
   {
    "name": "Denis Kipkoech",
    "phone": "790562100",
    "email": "denisbiwott@gmail.com",
    "has_licence": false
    },
    {
    "name": "Jojn Kimani",
    "phone": "7987689876",
    "email": "johnkimani@.com",
    "has_licence": true
   }
  ]
}
'''
data = json.loads(people_string)
print (data)
print()
print (type(data))
print()


for person in data['people']:
    print (person['name'], person['email'])

json_string = json.dumps(data, indent = 2, sort_keys = True)
print()
print(json_string)
