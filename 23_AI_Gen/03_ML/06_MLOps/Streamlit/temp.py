import pandas as pd
import pickle
import sklearn



input_features = [120000, 20, 1200, 85, 8, "Maruti", "Baleno Delta 1.2", 1, 1, 0, 1, 0, 0, 0, 0, 0]

def predict_price(input_features):
    with open("./venv/cars24_final.pkl", "rb") as file:
        artifacts = pickle.load(file)
        ohe = artifacts["ohe"]
        target_encoder = artifacts["target_en"]
        scaler = artifacts["scaler"]
        model = artifacts["model"]
    
    input_features[5], input_features[6] = target_encoder.transform([[input_features[5], input_features[6]]])
    X_scaled = scaler.transform([input_features])
    price = model.predict(X_scaled)
    price = scaler.inverse_transform(price)
    return price

price = predict_price(input_features)
print(price)