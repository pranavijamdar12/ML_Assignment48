import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1],[2],[3],[4],[5]])

Y = np.array([20000,25000,30000,35000,40000])

# craete model 
model = LinearRegression()

# train model
model.fit(X,Y)

#Predicted salary for 6 years

predication = model.predict([[6]])
print("Predication Salary for 6 years Exprinece:",predication[0])

# Regression line
Y_pred = model.predict(X)

plt.scatter(X,Y)
plt.plot(X,Y_pred)

plt.xlabel("Exprience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()
