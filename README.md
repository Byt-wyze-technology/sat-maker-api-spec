# SAT Maker API — Specification & Usage

The **SAT Maker API** is Byt-Wyze’s deterministic SAT instance generator.

It produces **CNF formulas with controllable structural hardness**, using a CES-style weighting scheme and repeatable seeds.  
This repository contains:

- The **public API specification** (endpoints, parameters, response schema)
- **Client examples** in multiple languages
- Notes on **best practices for benchmarking and reproducible research**

> ⚠️ The implementation of the generator itself is **closed-source**.  
> This repo documents how to **call** the SAT Maker service from your tools, solvers, and experiments.

---

## 1. Overview

The SAT Maker API lets you:

- Generate SAT instances with a fixed random **seed** (deterministic, repeatable)
- Control **size** (number of variables / clauses)
- Control **hardness bands** via CES-style parameters
- Choose different **instance families** (structured vs more random)
- Export in **DIMACS CNF** or JSON-encoded CNF
- Attach **metadata** (CES score, seed, checksum, timestamp, etc.) to each instance

Typical use cases:

- Benchmarking SAT solvers
- Building reproducible datasets for ML over SAT
- Stress-testing preprocessing and proof logging
- Teaching and experimentation

---

## 2. Getting Access

There are two ways to call the API:

1. **Via RapidAPI (recommended for most users)**  
2. **Directly from Byt-Wyze (for partners / internal integrations)**

### 2.1 RapidAPI

1. Go to the SAT Maker listing on RapidAPI.  
2. Click **"Subscribe"** (choose a plan or the free tier, if available).  
3. Copy your **API Key** from RapidAPI.
4. Note the **host** and **base URL** shown in the “Code Snippets” panel.

You will typically see something like:

- `X-RapidAPI-Key: YOUR_RAPIDAPI_KEY`
- `X-RapidAPI-Host: YOUR_RAPIDAPI_HOST`
- Base URL: `https://YOUR_RAPIDAPI_HOST/generate`

> Replace `YOUR_RAPIDAPI_HOST` and paths below with the values shown in RapidAPI  
> for the SAT Maker API. The examples here are illustrative.

### 2.2 Direct Byt-Wyze Access (optional)

For research collaborations or bulk / on-premise use, contact:

- **Email:** info@byt-wyze.com  
- **Website:** https://byt-wyze.com  

---

## 3. API Endpoints (high-level spec)

> The full OpenAPI / Swagger spec will live in `openapi.yaml` in this repo.  
> Below is a human-readable summary.

### `POST /generate`

Generate a new SAT instance.

**Request body (JSON):**

```json
{
  "n_vars": 200,
  "n_clauses": 800,
  "family": "structured",
  "ces_min": 0.4,
  "ces_max": 0.6,
  "seed": 123456,
  "format": "dimacs"
}
import requests

url = "https://sat-maker-api.byt-wyze.com/generate"

payload = {
    "n_vars": 200,
    "n_clauses": 800,
    "family": "structured",
    "ces_min": 0.4,
    "ces_max": 0.6,
    "seed": 123456,
    "format": "dimacs"
}

response = requests.post(url, json=payload, headers={
    "X-API-Key": "YOUR_API_KEY"
})

print(response.json())
import fetch from "node-fetch";

const res = await fetch("https://sat-maker-api.byt-wyze.com/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY"
  },
  body: JSON.stringify({
    n_vars: 200,
    n_clauses: 800,
    family: "structured",
    ces_min: 0.4,
    ces_max: 0.6,
    seed: 123456,
    format: "dimacs"
  })
});

const data = await res.json();
console.log(data);
curl -X POST "https://sat-maker-api.byt-wyze.com/generate" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
        "n_vars": 200,
        "n_clauses": 800,
        "family": "structured",
        "ces_min": 0.4,
        "ces_max": 0.6,
        "seed": 123456,
        "format": "dimacs"
      }'
