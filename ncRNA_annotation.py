import pandas as pd

def annotate_ncRNAs(ncRNA_ids: list) -> pd.DataFrame:
    annotations = []
    for ncRNA in ncRNA_ids:
        annotations.append({'ncRNA_id': ncRNA, 'function': 'Unknown', 'location': 'chr1:1000-2000'})
    return pd.DataFrame(annotations)

if __name__ == "__main__":
    ncRNA_list = ['ncRNA_1', 'ncRNA_2']
    annotations = annotate_ncRNAs(ncRNA_list)
    annotations.to_csv('results/ncRNA_annotations.csv', index=False)