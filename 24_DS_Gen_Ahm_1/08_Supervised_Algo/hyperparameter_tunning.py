import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X_train = pd.read_pickle("preprocessed_X_sm.pickle")
X_test = pd.read_pickle("X_test.pickle")
y_train = pd.read_pickle("y_sm.pickle")
y_test = pd.read_pickle("y_test.pickle")

rf_clf = RandomForestClassifier(max_depth=4, random_state=7)

params = {
    "n_estimators" : np.arange(100, 500, 50),    # 20
    "criterion" : ["gini", "entropy"],    # 2
    "max_depth" : np.arange(3, 16, 1),    # 13
    "bootstrap" : [True, False],          # 2
    "max_features" : [8, 9, 10]     # 16
}

from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(estimator=rf_clf, 
                                   param_distributions=params, 
                                   n_iter=50,
                                   n_jobs=-1,
                                   cv=5,
                                   scoring="accuracy"                
                                   )

random_search.fit(X_train, y_train)