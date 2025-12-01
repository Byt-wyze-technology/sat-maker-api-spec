#!/usr/bin/env bash

API_URL="https://byt-wyze.com/api/sat-maker/generate"
API_KEY="${BYTWYZE_API_KEY:-YOUR_API_KEY_HERE}"

curl -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $API_KEY" \
  -d '{
    "n_vars": 200,
    "n_clauses": 800,
    "family": "structured",
    "ces_min": 0.3,
    "ces_max": 0.7,
    "seed": 123456,
    "format": "dimacs"
  }'
