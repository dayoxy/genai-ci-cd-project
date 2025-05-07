import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    df.dropna(inplace=True)
    X = df.drop('target', axis=1)
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)