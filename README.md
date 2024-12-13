# assessment
This project provides a CLI tool for looking up details about individuals from a YAML data file.

# Prerequisites
Ensure the following are installed on your system:
Docker

# Build the Docker Image
docker build -t lookup-cli .

# Run the Script
docker run --rm lookup-cli <name> <output_field>

# Opts:
- `--name <string>`: The name to lookup in the YAML file.
- `--output_field <string>`: The field to return for the given name (e.g., `age`, `occupation`).