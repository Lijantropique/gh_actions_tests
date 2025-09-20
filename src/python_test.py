import yaml

# Open the YAML file in read mode
with open('./src/config.yaml', 'r') as file:
    # Load the YAML content into a Python dictionary
    data = yaml.safe_load(file)

# Access and print the value associated with key 'a'
if 'a' in data:
    print(f"Value of key 'a': {data['a']}")
else:
    print("Key 'a' not found in the YAML file.")