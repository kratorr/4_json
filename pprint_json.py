import json
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        return raw_data


def pretty_print_json(data):
    return json.dumps((data), sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    print(pretty_print_json(load_data(sys.argv[1])))
