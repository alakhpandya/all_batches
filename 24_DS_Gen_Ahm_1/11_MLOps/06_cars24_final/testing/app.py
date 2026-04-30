import numpy as np
import pandas as pd
import sklearn
import pickle
from datetime import datetime

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

# X = pd.DataFrame(columns=["full_name", "year", "seller_type", "km_driven", "fuel_type", "transmission_type", "mileage", "engine", "max_power", "seats"])
# X.loc[len(X)] = ["Hyundai i20 Asta", 2010, "Individual", 60000, "Petrol", "Manual", 17.00, 1197.0, 80.00, 5]
# print(X)

X = pd.DataFrame(data={
   "full_name" : ["Hyundai i20 Asta"],
   "year" : [2010],
   "seller_type" : ["Individual"],
   "km_driven" : [60000],
   "fuel_type" : ["Petrol"],
   "transmission_type" : ["Manual"],
   "mileage" : [17],
   "engine" : [1197],
   "max_power" : [80],
   "seats" : [5]
})
# print(X)

y_pred = pipe.predict(X)[0]
print(f"Predicted selling price = {round(y_pred, 2)} Lacs")