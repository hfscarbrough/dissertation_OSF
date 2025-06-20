from serpapi import GoogleSearch
import pandas as pd

# Replace with your actual API key
api_key = "71c4f0f7fa4afe845515e6ecca6a69168917cd1246f1dffe3e674c7c4328db95"

query ='"Myers, J. A., Brownell, M. T., Griffin, C. C., Hughes, E. M., Witzel, B. S., Gage, N. A., Peyton, D., Acosta, K., & Wang, J. (2021). Mathematics Interventions for Adolescents with Mathematics Difficulties: A Meta-Analysis. Learning Disabilities Research & Practice, 36(2), 145–166. https://doi.org/10.1111/ldrp.12244"'
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
df.to_excel("M10012-full.xlsx", index=False)
print(f"✅ Saved {len(all_results)} results to M10012-full.xlsx")