from serpapi import GoogleSearch
import pandas as pd

# Replace with your actual API key
api_key = "031b4d2594a430f1590e7a17983320cf5f0ceebaf6254692a8097e79f7c5c2e8"

query ='"Hall, C., Dahl-Leonard, K., Cho, E., Solari, E. J., Capin, P., Conner, C. L., Henry, A. R., Cook, L., Hayes, L., Vargas, I., Richmond, C. L., & Kehoe, K. F. (2023). Forty Years of Reading Intervention Research for Elementary Students with or at Risk for Dyslexia: A Systematic Review and Meta-Analysis. Reading Research Quarterly, 58(2), 285–312. https://doi.org/10.1002/rrq.477"'
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
df.to_excel("M10019-full.xlsx", index=False)
print(f"✅ Saved {len(all_results)} results to M10019-full.xlsx")