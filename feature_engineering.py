import pandas as pd
from sklearn.preprocessing import StandardScaler

def engineer_features(expression_file: str, gwas_file: str) -> pd.DataFrame:
    expression = pd.read_csv(expression_file)
    gwas = pd.read_csv(gwas_file)
    merged = pd.merge(expression, gwas, on='gene_id')
    scaler = StandardScaler()
    merged_scaled = pd.DataFrame(scaler.fit_transform(merged.drop(columns=['gene_id'])), columns=merged.columns[1:])
    merged_scaled['gene_id'] = merged['gene_id']
    return merged_scaled

if __name__ == "__main__":
    features = engineer_features('data/expression.csv', 'data/gwas.csv')
    features.to_csv('results/features.csv', index=False)