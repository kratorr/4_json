import json
import sys
import os

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as json_file:
        decoded_json = json.load(json_file)
        return decoded_json


def pretty_print_json(json_object):
    print(json.dumps(json_object, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        data_for_print = load_data(filepath)
        pretty_print_json(data_for_print)
    except:
        raise FileNotFoundError