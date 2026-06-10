import pandas as pd
import pickle
import sklearn
from category_encoders.target_encoder import TargetEncoder

with open("./venv/cars24_final.pkl", "rb") as f:
    artifacts = pickle.load(f)

model = artifacts["model"]
label_encoder = artifacts["label_encoder"]
onehot_encoder = artifacts["onehot_encoder"]
target_encoder = artifacts["target_encoder"]
scaler_X = artifacts["scaler_X"]
scaler_y = artifacts["scaler_y"]
feature_order = artifacts["feature_order"]

# print(feature_order)
# ['km_driven', 'transmission_type', 'mileage', 'engine', 'max_power', 'age', 'make', 'model', '5', '>5', 'seller_type_Dealer', 'seller_type_Individual', 'seller_type_Trustmark Dealer', 'fuel_type_CNG', 'fuel_type_Diesel', 'fuel_type_Electric', 'fuel_type_LPG', 'fuel_type_Petrol']
"""
user_input = {
      'km_driven': 115000, 
      'transmission_type': "Manual", 
      'mileage': 20, 
      'engine': 1200, 
      'max_power': 85, 
      'age': 8, 
      'make': "Maruti", 
      'model': "Baleno Delta 1.2", 
      '5': 1, 
      '>5': 0, 
      'seller_type_Dealer': 0, 
      'seller_type_Individual': 1, 
      'seller_type_Trustmark Dealer': 0, 
      'fuel_type_CNG': 0, 
      'fuel_type_Diesel': 0, 
      'fuel_type_Electric': 0, 
      'fuel_type_LPG': 0, 
      'fuel_type_Petrol': 1
}
"""
user_input = {
    'km_driven': 115000,
    'transmission_type': "Manual",
    'mileage': 20,
    'engine': 1200,
    'max_power': 85,
    'age': 8,
    'make': "Maruti",
    'model': "Baleno Delta 1.2",
    'seller_type': "Individual",
    'fuel_type': "Petrol",
    '5': 1, 
    '>5': 0
}

user_df = pd.DataFrame([user_input])
label_col = "transmission_type"
onehot_cols = ["seller_type", "fuel_type"]
target_encode_cols = ["make", "model"]

# ohe_feature_names = ["seller_type_Dealer", "seller_type_Individual", "seller_type_Trustmark Dealer", ]
ohe_feature_names = onehot_encoder.get_feature_names_out(onehot_cols)

user_df[label_col] = label_encoder.transform(user_df[label_col])
user_ohe = onehot_encoder.transform(user_df[onehot_cols])
user_ohe = pd.DataFrame(user_ohe, columns=ohe_feature_names)

user_df = user_df.drop(columns=onehot_cols)
user_df = pd.concat([user_df, user_ohe], axis=1)

user_df[target_encode_cols] = target_encoder.transform(user_df[target_encode_cols])
user_df = user_df[feature_order]
user_scaled = scaler_X.transform(user_df)

scaled_prediction = model.predict(user_scaled)

final_price = scaler_y.inverse_transform(
    scaled_prediction.reshape(-1, 1)
)

# print(f"Predicted Car Price: ₹ {final_price}")
print(f"Predicted Car Price: ₹ {final_price[0][0]:,.2f} Lacs")