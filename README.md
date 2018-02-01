# Prettify JSON

This program prints a JSON file to the console in the pretty format.

# Quickstart

The program must be run using the console, the required argument is the path to the file.

How to run:
```bash
$ python3 pprint_json.py <file_path>
```
Example of script launch on Linux, Python 3.5:
```bash
$ python3 pprint_json.py geo.json
{
    "$schema": "http://json-schema.org/draft-06/schema#",
    "description": "A geographical coordinate",
    "id": "http://json-schema.org/geo",
    "properties": {
        "latitude": {
            "type": "number"
        },
        "longitude": {
            "type": "number"
        }
    },
    "type": "object"
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
