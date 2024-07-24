# fip-information

Information about FIP

## Testing

Converting MD to JSON:
`python3 convert_md_to_json.py to-json --directory information`

Render the JSON using the ancient tool:
`npx json-dereference -s ./information/belgium/belgium_de.json -o out.json`

Converting JSON to MD (and deleting the JSON files, so it's basically a revert):
`python3 convert_md_to_json.py to-md --directory information`

# Group of countries

The countries are grouped according to the UNSD:
https://de.wikipedia.org/wiki/Regionale_Gliederung#/media/Datei:Europe_subregion_map_UN_geoscheme.svg
