import joblib
import os
from lightgbm import LGBMRegressor

def load_model(path="src/model.pkl"):
    return joblib.load(path)

def train_model(X,y, n_estimators=100, learning_rate=0.1,random_state=42):
    model = LGBMRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        random_state=random_state
    )
    model.fit(X,y)
    return model   