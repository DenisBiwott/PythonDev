import json

with open('new_states.json') as f:
    states = (f)
    data = json.load(f)

# print only state names
for state in data['states']:
    print(state['name'])
