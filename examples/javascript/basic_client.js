const API_URL = "https://byt-wyze.com/api/sat-maker/generate";
const API_KEY = process.env.BYTWYZE_API_KEY || "YOUR_API_KEY_HERE";

async function main() {
  const payload = {
    n_vars: 200,
    n_clauses: 800,
    family: "structured",   // or "random"
    ces_min: 0.3,
    ces_max: 0.7,
    seed: 123456,
    format: "dimacs"
  };

  const resp = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": API_KEY
    },
    body: JSON.stringify(payload)
  });

  if (!resp.ok) {
    console.error("Error:", resp.status, await resp.text());
    return;
  }

  const data = await resp.json();
  console.log("CNF:", data.cnf.substring(0, 500) + "...");
  console.log("Metadata:", data.metadata);
}

main().catch(console.error);
