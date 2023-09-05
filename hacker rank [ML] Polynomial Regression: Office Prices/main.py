# Prolem url:
# https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Read data from the file
with open("data.txt", "r") as file:
    data =file.read()

lines = data.split("\n")

# extract the number of feature F, and the number of data points N
F, N = map(int, lines[0].split())

# extracting the training data
train_data = np.array([list(map(float, line.split())) for line in lines[1:N+1]])

# extracting the test data
T = int(lines[N+1])
test_data = np.array([list(map(float, line.split())) for line in lines[N+2:N+2+T]])

# extracting the features as X_train, and the target as y_train
X_train = train_data[:, :-1]
y_train = train_data[:, -1]

# Create polynomial features for the training data
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X_train)

# Train a linear regression model on the polynomial featrue
model = LinearRegression().fit(X_poly, y_train)

#print(X_poly.shape, y_train.shape)
#The training data has been successfully transformed into polynomial features with a degree of 3. We have a total of 10 polynomial features for the 100 training data points.

# Transform the test data into polynomial features
X_test_poly=poly.transform(test_data)

#  Predict the price using the trained model
prediction = model.predict(X_test_poly)

for price in prediction:
    print(price)



