#!/usr/bin/env python3

import yaml
import sys
import os

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file. Details: {e}")
        sys.exit(1)
    
def lookup_person(data, name, output_field):
    for person in data:
        if person.get('name', '').lower() == name.lower():
            return person.get(output_field, f"Field not found.")
    return f"Name not found."

def main(argv):
    # Validate the number of arguments
    if len(argv) != 2:
        print("Usage: lookup-cli <name> <output_field>")
        sys.exit(2)

    # Extract name and output field from the arguments
    name = argv[0]
    output_field = argv[1]
    
    # Path to the YAML file
    file_path = 'people_data.yaml'

    # Read and process the YAML file
    data = read_yaml(file_path)

    # Lookup the person's information
    result = lookup_person(data, name, output_field)

    print(result)

if __name__ == "__main__":
    main(sys.argv[1:])