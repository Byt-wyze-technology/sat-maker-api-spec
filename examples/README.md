# SAT Maker API — Client Examples

This folder contains minimal client examples for calling the **Byt-Wyze SAT Maker API**.

Each example sends a `POST /generate` request to:

`https://byt-wyze.com/api/sat-maker/generate`

with a JSON body matching the schema in [`openapi.yaml`](../openapi.yaml).

## Examples

- `python/basic_client.py` – simple usage with the `requests` library  
- `javascript/basic_client.js` – browser / Node-style `fetch` example  
- `curl/example.sh` – one-liner command-line example

All examples assume you have a valid **API key** and pass it as:

`X-API-Key: YOUR_API_KEY_HERE`
