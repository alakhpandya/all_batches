import pandas as pd
import streamlit as st 
df = pd.read_csv("cars24-car-price-cleaned.csv")
# print(df)
print(df.info())

st.title("Car Price Predictor")

km_driven = st.number_input("KM Driven")
mileage = st.number_input("Mileage")
engine = st.number_input("Engine")
max_power = st.number_input("Max Power")
age = st.number_input("Age")

make = st.text_input("Make")
model_name = st.text_input("Model")


seller = st.radio("Seller",["Individual","Trustmark Dealer"], horizontal=True)
seats = st.radio("Seats", ["5",">5"],horizontal=True)

fuel = st.selectbox("Fuel", ["Diesel","Electric","LPG","Petrol"])
transmission = st.selectbox("Transmission", ["Manual","Automatic"])