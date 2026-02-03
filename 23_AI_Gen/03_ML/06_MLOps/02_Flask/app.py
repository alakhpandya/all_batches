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
    # converting make & model to numerical values using target encoder
    te_data_df = pd.DataFrame([{
        "make" : data["make"].lower(),
        "model" : data["model"].lower()
    }])
    te_result = target_encoder.transform(te_data_df[["make", "model"]])

    # converting one-hot columns into numeric columns:
    ohe_data_df = pd.DataFrame([{
        "seller_type" : data["seller_type"],
        "fuel_type" : data["fuel_type"]
    }])
    ohe_data = ohe.transform(ohe_data_df[onehot_cols])
    ohe_df = pd.DataFrame(data=ohe_data, columns=ohe.get_feature_names_out())

    # Encoding label encoding columns:
    label_data_df = pd.DataFrame([{
        "transmission_type" : data["transmission_type"]
    }])
    label_data = label_encoder.transform(label_data_df.iloc[label_col])
    label_df = pd.DataFrame(data=label_data, columns=label_col)

    return {
        "target_encoded_features" : te_result.to_dict(orient="records"),
        "ohe_encoded_features" : ohe_df.to_dict(orient="records"),
        "label_encoded_features" : label_df.to_dict(orient="records")
    }

if __name__ == "__main__":
    app.run(debug=True)