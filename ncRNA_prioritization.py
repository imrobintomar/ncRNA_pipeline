import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def prioritize_ncRNAs(features_file: str) -> pd.DataFrame:
    data = pd.read_csv(features_file)
    X = data.drop(columns=['gene_id'])
    model = GradientBoostingClassifier()
    model.fit(X, [1 if i % 2 == 0 else 0 for i in range(len(X))])  # Dummy target
    data['priority_score'] = model.predict_proba(X)[:, 1]
    return data.sort_values(by='priority_score', ascending=False)

if __name__ == "__main__":
    prioritized = prioritize_ncRNAs('results/features.csv')
    prioritized.to_csv('results/prioritized_ncRNAs.csv', index=False)