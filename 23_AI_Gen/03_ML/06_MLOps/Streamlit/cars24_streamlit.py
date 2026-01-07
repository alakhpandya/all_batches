import pandas as pd
import streamlit as st
import pickle
import sklearn

df = pd.read_csv("./venv/cars24-car-price.csv")

# st.title("Car price prediction using cars24 data")
st.write(
    """
    # Car price prediction using cars24 data
    """
)
st.dataframe(df.head())

"""
km_driven - 120000
mileage - 20
engine - 1200
max_power - 85
age - 8
make - Maruti
model - Baleno Delta
manual - 1
5 - 1
>5 - 0
seller_type_Individual - 1
seller_type_Trustmark Dealer - 0
fuel_type_Diesel - 0
fuel_type_Electric - 0
fuel_type_LPG - 0
fuel_type_Petrol - 0
input_features = [120000, 20, 1200, 85, 8, Maruti, Baleno Delta, 1, 1, 0, 1, 0, 0, 0, 0, 0]
"""

col1, col2 = st.columns(2)

fuel_type = col1.selectbox(
    "Fuel Type:", ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
)
engine = col1.slider("Engine Size:", min_value=800, max_value=6500, step=100)

transmission_type = col2.selectbox("Transmission:", ["Manual", "Automatic"])
seats = col2.selectbox("Seats:", [2, 4, 5, 6, 7, 9, 11, 14])
inputs = [fuel_type, engine, transmission_type, seats]

input_features = [120000, 20, 1200, 85, 8, "Maruti", "Baleno Delta", 1, 1, 0, 1, 0, 0, 0, 0, 0]

def predict_price(input_features):
    with open("./venv/cars24_final.pkl", "rb") as file:
        artifacts = pickle.load(file)
        ohe = artifacts["ohe"]
        target_encoder = artifacts["target_en"]
        scaler = artifacts["scaler"]
        model = artifacts["model"]
    
    result = target_encoder.transform([input_features[5], input_features[6]])

    return result


if st.button("Predice Price"):
    price = predict_price(input_features)
    st.write(price[0])