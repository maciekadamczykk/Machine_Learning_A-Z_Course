import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.metrics import confusion_matrix

df = pd.read_csv("Social_Network_Ads.csv")

X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test)

classifier = SVC(kernel='rbf',random_state=42)
classifier.fit(X_train,y_train) 

y_pred = classifier.predict(X_test)

print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)), axis=1))

acc = accuracy_score(y_pred,y_test)

cf_matrix = confusion_matrix(y_pred,y_test)

sns.heatmap(cf_matrix, annot=True, cmap="Blues")
plt.show()

print(acc)
