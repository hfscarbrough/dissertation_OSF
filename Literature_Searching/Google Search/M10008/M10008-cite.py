from serpapi import GoogleSearch
import pandas as pd

# Replace with your actual API key
api_key = "89ab3f2b2bea039af9e140ab4f2ca1ff2cc795e6fbb3a43dc94ccec7e9223821"

query ='"Arizmendi et al., 2021"'
results_per_page = 12
num_pages = 5  # You can change this to 5, 10, etc.

all_results = []

for page in range(num_pages):
    print(f"📄 Fetching page {page + 1}...")
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": results_per_page,
        "start": page * results_per_page,
        "no_cache": True
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for result in results.get("organic_results", []):
        all_results.append({
            "Title": result.get("title"),
            "URL": result.get("link"),
            "Snippet": result.get("snippet"),
            "Date": result.get("date")
        })

df = pd.DataFrame(all_results)
df.to_excel("M10008-cite.xlsx", index=False)
print(f"✅ Saved {len(all_results)} results to M10008-cite.xlsx")