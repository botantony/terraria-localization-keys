#!/usr/bin/env python3
#
# Small script that creates this language pack
import json
import os

input_dir = "files"
output_dir = "output"


def process_text(filename: str, input: str) -> str:
    json_object = json.loads(input)
    new_json_object = {}
    for primaryKey, d in json_object.items():
        new_json_object[primaryKey] = {}
        for secondaryKey in d:
            new_json_object[primaryKey][secondaryKey] = (
                f"{filename}.{primaryKey}.{secondaryKey}"
            )
    return json.dumps(new_json_object, sort_keys=True, indent=4)


if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        print(filename)
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        if os.path.isfile(input_path):
            with open(input_path, "r", encoding="utf-8") as infile:
                content = infile.read()

            processed = process_text(".".join(filename.split(".")[:-1]), content)

            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write(processed)

    print("\nDone!")
