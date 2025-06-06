import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Position_Salaries.csv')

X = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=42)

regressor.fit(X,y) 

print(regressor.predict([[6.5]]))

