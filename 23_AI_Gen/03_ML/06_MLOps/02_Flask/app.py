from flask import Flask, request
import pandas as pd
import streamlit as st
import pickle
import sklearn
import category_encoders

with open("./venv/cars24_final_model.pkl", "rb") as file:
    artifacts = pickle.load(file)
    model = artifacts["model"]
    label_encoder = artifacts["label_encoder"]
    ohe = artifacts["onehot_encoder"]
    target_encoder = artifacts["target_encoder"]
    scaler_X = artifacts["scaler_X"]
    scaler_y = artifacts["scaler_y"]
    feature_order = artifacts["feature_order"]

app = Flask(__name__)
label_col = "transmission_type"
onehot_cols = ["seller_type", "fuel_type"]

@app.route("/", methods=["GET"])
def home():
    return "Flask is running!!!!"

# input_features = [120000, 20, 1200, 85, 8, "Maruti", "Baleno Delta", 1, 1, 0, 1, 0, 0, 0, 0, 0]

@app.route("/predict", methods=["POST"])
def prediction():
    data = request.get_json()

    # -------- Target Encoding --------
    te_df = pd.DataFrame([{
        "make": data["make"].lower(),
        "model": data["model"].lower()
    }])
    te_result = target_encoder.transform(te_df)

    # -------- One Hot Encoding --------
    ohe_df = pd.DataFrame([{
        "seller_type": data["seller_type"],
        "fuel_type": data["fuel_type"]
    }])
    ohe_data = ohe.transform(ohe_df)
    ohe_df = pd.DataFrame(ohe_data, columns=ohe.get_feature_names_out())

    # -------- Label Encoding --------
    label_df = pd.DataFrame([{
        "transmission_type": data["transmission_type"]
    }])
    label_data = label_encoder.transform(label_df[label_col])
    label_df = pd.DataFrame(label_data, columns=[label_col])

    # -------- Numerical Features --------
    num_df = pd.DataFrame([{
        "km_driven": data["km_driven"],
        "mileage": data["mileage"],
        "engine": data["engine"],
        "max_power": data["max_power"],
        "seats": data["seats"]
    }])

    # -------- Combine all features --------
    final_df = pd.concat([num_df, te_result, ohe_df, label_df], axis=1)

    # -------- Arrange column order --------
    final_df = final_df[feature_order]

    # -------- Scale --------
    X_scaled = scaler_X.transform(final_df)

    # -------- Predict --------
    y_scaled = model.predict(X_scaled)

    # -------- Inverse scale --------
    prediction = scaler_y.inverse_transform(y_scaled.reshape(-1,1))[0][0]

    return {"Predicted Price": round(float(prediction),2)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)