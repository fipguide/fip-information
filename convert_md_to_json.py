import os
import json

def find_files(directory, filetype):
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(filetype):
                md_files.append(os.path.join(root, file))
    return md_files

def create_json_from_md(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        value = file.read()
    key = os.path.basename(md_file).rsplit('_', 1)[0]
    json_data = {key: value}
    json_file_path = md_file.replace('.md', '.json')

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print(f"Converting: '{json_file_path}'")

def create_md_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    key = os.path.basename(json_file).rsplit('_', 1)[0]
    if key not in json_data:
        print(f"Skipping:'{json_file}'")
        return

    md_file_path = json_file.replace('.json', '.md')

    content = json_data[key]

    if os.path.exists(md_file_path):
        print(f"Converting: '{md_file_path}'")
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(str(content))
        print(f"Removing: '{json_file}'")
        os.remove(json_file)
        return
    else:
        print(f"Skipping:'{json_file}'")
        return
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Converting md to json and vice versa.')
    parser.add_argument('action', choices=['to-json', 'to-md'], help='Converting the files from md to json (to-json) or from json to md (to-md).')
    parser.add_argument('-d', '--directory', default='.', help='The directory to be searched recursivly.')
    
    args = parser.parse_args()

    if args.action == 'to-json':
        md_files = find_files(args.directory, '.md')
        for md_file in md_files:
            create_json_from_md(md_file)
    elif args.action == 'to-md':
        json_files = find_files(args.directory, '.json')
        for json_file in json_files:
            create_md_from_json(json_file)
