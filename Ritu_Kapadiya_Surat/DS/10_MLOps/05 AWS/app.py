import numpy as np
import pandas as pd
import sklearn
import pickle
from datetime import datetime
from flask import Flask, request

def split_name(df):
  df = df.copy()
  df["full_name"] = df["full_name"].str.lower()
  df["make"] = df["full_name"].apply(lambda x : x.split()[0])
  df["model"] = df["full_name"].apply(lambda x : " ".join(x.split()[1:]))
  df.drop(columns="full_name", inplace=True)
  return df

def seats_tranformer(df):
  df = df.copy()
  # computing age of the car
  df["age"] = datetime.now().year - df["year"]
  # converting seats
  df["5"] = np.where(df["seats"] == 5, 1, 0)
  df[">5"] = np.where(df["seats"] > 5, 1, 0)
  df.drop(columns=["year", "seats"], inplace=True)
  return df

with open("cars24_final_pipe.pkl", "rb") as f:
  pipe = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  return "<h1>Flask app is running on AWS!!</h1>"

@app.route("/predict", methods=["POST"])
def predict():
  data = request.json
  X = pd.DataFrame(data={
    "full_name" : [data["full_name"]],
    "year" : [data["year"]],
    "seller_type" : [data["seller_type"]],
    "km_driven" : [data["km_driven"]],
    "fuel_type" : [data["fuel_type"]],
    "transmission_type" : [data["transmission_type"]],
    "mileage" : [data["mileage"]],
    "engine" : [data["engine"]],
    "max_power" : [data["max_power"]],
    "seats" : [data["seats"]]
  })
  # y_pred = pipe.predict(X)
  # return f"Predicted selling price = {y_pred} Lacs"
  y_pred = pipe.predict(X)[0]
  return f"Predicted selling price = {round(y_pred, 2)} Lacs"

if __name__ == "__main__":
  app.run(port=8000, debug=True, host="0.0.0.0")