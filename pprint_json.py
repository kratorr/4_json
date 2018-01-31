import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_json = json.load(f)
            return raw_json
    except ValueError:
          print("JSON file should be encoded in utf-8")

def pretty_print_json(json_content):
    return json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    print(pretty_print_json(load_data(sys.argv[1])))
