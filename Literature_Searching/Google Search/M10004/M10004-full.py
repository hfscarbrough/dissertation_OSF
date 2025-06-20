from serpapi import GoogleSearch
import pandas as pd

# Replace with your actual API key
api_key = "a9dd7c19346ce7a8adab7442d876364dc2f99ced0677ef9c97e568886ffc1e46"

query ='"Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). A meta-analysis of the worked examples effect on mathematics performance. Educational Psychology Review, 35(1), Article 11. https://doi.org/10.1007/s10648-023-09745-1"'
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
df.to_excel("M10004-full.xlsx", index=False)
print(f"✅ Saved {len(all_results)} results to M10004-full.xlsx")