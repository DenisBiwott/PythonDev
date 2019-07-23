import json

with open('new_states.json') as f:
    states = (f)
    data = json.load(f)

json_string = json.dumps(data, indent=2, sort_keys=True)
print(json_string)

# This code created the new_states_.json file
with open('new_states_.json', 'w') as f:
    f.write(json_string)    #
    print("Done")
