# a program to predict car safety

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("CSV Files\car.data")
print(data.head())  # To check if our data is loaded correctly

# to create a label encoder
le = preprocessing.LabelEncoder()

# fit transform takes each column and returns an array
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

# to recombine data into a feature list and label list
X = list(zip(buying, maint, door, persons, lug_boot, safety))  # features
y = list(cls)  # labels
# to split the data into training and testing (train wiht 90% and test with 10% of the data)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

# knn (k nearest neighbors) requires the whole dataset so is computational heavy
# better to use on small datasets
# k value is how many points we use to make the decision

model = KNeighborsClassifier(n_neighbors=9)
# to train the model
model.fit(x_train, y_train)
# to score the model
acc = model.score(x_test, y_test)
print(acc)

# to test the model
predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
# to look at neighbours to better understand the accuracy of the model
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)