import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("50_Startups.csv")

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

un = df["State"].unique()

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [-1])], remainder="passthrough")
x = np.array(ct.fit_transform(x))


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

np.set_printoptions(precision=2)

print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test), 1)), axis=1))