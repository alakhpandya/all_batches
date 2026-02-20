from flask import Flask, request
import pandas as pd
import streamlit as st
import pickle
import sklearn

with open("./venv/cars24_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask is running fantastic!!!!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if data["year"] > 2022:
        return {"error": "Model trained on 2022 data."}, 400

    input_df = pd.DataFrame([data])
    prediction = pipeline.predict(input_df)[0]

    return {"Predicted Price": round(float(prediction),2)}