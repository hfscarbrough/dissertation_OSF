from serpapi import GoogleSearch
import pandas as pd

# Replace with your actual API key
api_key = "71c4f0f7fa4afe845515e6ecca6a69168917cd1246f1dffe3e674c7c4328db95"

query ='"Ran, H., Kasli, M., & Secada, W. G. (2021). A Meta-Analysis on Computer Technology Intervention Effects on Mathematics Achievement for Low-Performing Students in K-12 Classrooms. Journal of Educational Computing Research, 59(1), 119–153. https://doi.org/10.1177/0735633120952063"'
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
df.to_excel("M10015-full.xlsx", index=False)
print(f"✅ Saved {len(all_results)} results to M10015-full.xlsx")