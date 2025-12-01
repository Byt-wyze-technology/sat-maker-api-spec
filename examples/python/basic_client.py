import os
import json
import requests

# SAT Maker API endpoint
API_URL = "https://byt-wyze.com/api/sat-maker/generate"

# Put your real key here or in the environment as BYTWYZE_API_KEY
API_KEY = os.getenv("BYTWYZE_API_KEY", "YOUR_API_KEY_HERE")

payload = {
    "n_vars": 200,
    "n_clauses": 800,
    "family": "structured",      # or "random"
    "ces_min": 0.3,
    "ces_max": 0.7,
    "seed": 123456,
    "format": "dimacs"           # or "json"
}

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

def main():
    resp = requests.post(API_URL, headers=headers, json=payload)
    resp.raise_for_status()

    data = resp.json()
    cnf = data.get("cnf")
    metadata = data.get("metadata", {})

    print("CNF instance:")
    print(cnf[:500] + "\n..." if isinstance(cnf, str) and len(cnf) > 500 else cnf)
    print("\nMetadata:")
    print(json.dumps(metadata, indent=2))

if __name__ == "__main__":
    main()
