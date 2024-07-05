import os
import json

def find_files(directory, filetype):
    adoc_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(filetype):
                adoc_files.append(os.path.join(root, file))
    return adoc_files

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_json_from_adoc(adoc_file):
    with open(adoc_file, 'r', encoding='utf-8') as file:
        value = file.read()
    key = os.path.basename(adoc_file).rsplit('_', 1)[0]
    json_data = {key: value}
    json_file_path = adoc_file.replace('.adoc', '.json')

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print(f"Converting: '{json_file_path}'")

def create_adoc_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    key = os.path.basename(json_file).rsplit('_', 1)[0]
    if key not in json_data:
        print(f"Skipping:'{json_file}'")
        return

    adoc_file_path = json_file.replace('.json', '.adoc')

    content = json_data[key]

    if os.path.exists(adoc_file_path):
        print(f"Converting: '{adoc_file_path}'")
        with open(adoc_file_path, 'w', encoding='utf-8') as adoc_file:
            adoc_file.write(str(content))
        print(f"Removing: '{json_file}'")
        os.remove(json_file)
        return
    else:
        print(f"Skipping:'{json_file}'")
        return
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Converting adoc to json and vice versa.')
    parser.add_argument('action', choices=['to-json', 'to-adoc'], help='Converting the files from adoc to json (to-json) or from json to adoc (to-adoc).')
    parser.add_argument('-d', '--directory', default='.', help='The directory to be searched recursivly.')
    
    args = parser.parse_args()

    if args.action == 'to-json':
        adoc_files = find_files(args.directory, '.adoc')
        for adoc_file in adoc_files:
            create_json_from_adoc(adoc_file)
    elif args.action == 'to-adoc':
        json_files = find_files(args.directory, '.json')
        for json_file in json_files:
            create_adoc_from_json(json_file)
