import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load known ncRNA-RBP interaction data
def load_interaction_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

# Train interaction prediction model
def train_model(data: pd.DataFrame) -> RandomForestClassifier:
    X = data.drop(columns=['interaction'])
    y = data['interaction']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Predict novel interactions
def predict_interactions(model: RandomForestClassifier, features: pd.DataFrame) -> pd.DataFrame:
    features['interaction_score'] = model.predict_proba(features)[:, 1]
    return features

if __name__ == "__main__":
    data = load_interaction_data('data/ncRNA_RBP_interactions.csv')
    model = train_model(data)
    test_features = pd.read_csv('data/test_features.csv')
    predictions = predict_interactions(model, test_features)
    predictions.to_csv('results/ncRNA_RBP_predictions.csv', index=False)