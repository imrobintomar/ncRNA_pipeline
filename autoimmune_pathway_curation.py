import requests
import pandas as pd

def fetch_kegg_pathway(pathway_id: str) -> dict:
    url = f"https://rest.kegg.jp/get/{pathway_id}"
    response = requests.get(url)
    return response.text

def curate_pathways(pathway_ids: list) -> pd.DataFrame:
    pathway_data = []
    for pid in pathway_ids:
        data = fetch_kegg_pathway(pid)
        pathway_data.append({'pathway_id': pid, 'data': data})
    return pd.DataFrame(pathway_data)

if __name__ == "__main__":
    pathways = ['hsa04620', 'hsa05320']
    curated = curate_pathways(pathways)
    curated.to_csv('results/curated_pathways.csv', index=False)