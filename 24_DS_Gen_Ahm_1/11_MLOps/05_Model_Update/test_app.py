import pickle
import numpy as np
import pandas as pd

with open("cars24_test_model.pkl", "rb") as f:
    model = pickle.load(f)

# print(model)
test_data = np.array([
    [0.724138, 0.020764, 0.167241, 0.184834, 0.111111, 0.275862, 0.194048, 0.240897, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0]
])

print(model.predict(test_data))

# Problems:
"""
- Input data is scaled
- Input data is also encoded (ohe, le & te)
- Sample input data coming from frontend would be like:
["Hyundai", "Grand i10 Asta", 2016, Individual, 20000, Petrol, Manual, 18.90, 1197.0, 82.00, 5]
- Therefore, we have to convert the above data in a form that our model takes
"""
# Problem: We cannot again create & train the scalers and encoders here