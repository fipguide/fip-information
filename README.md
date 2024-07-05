# fip-information

Information about FIP

## Testing

Converting ADOC to JSON:
`python3 convert_adoc_to_json.py to-json --directory information`

Render the JSON using the acient tool:
`npx json-dereference -s ./information/belgium/belgium_de.json -o out.json`

Converting JSON to ADOC (and deleting the JSON files, so it's basically a revert):
`python3 convert_adoc_to_json.py to-adoc --directory information`
