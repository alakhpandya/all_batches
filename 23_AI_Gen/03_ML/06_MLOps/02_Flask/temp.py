# from flask import Flask, request
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

label_col = "transmission_type"
onehot_cols = ["seller_type", "fuel_type"]

temp_df = pd.DataFrame([{
    "seller_type" : "Individual",
    "fuel_type" : "Petrol"
}])

ohe_data = ohe.transform(temp_df[onehot_cols])
ohe_df = pd.DataFrame(data=ohe_data, columns=ohe.get_feature_names_out())
print(ohe_df)