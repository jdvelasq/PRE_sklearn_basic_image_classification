"""GitHub Classroom autograding script."""

import pickle

from sklearn import datasets
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()
data = digits.images.reshape((len(digits.images), -1))

with open("estimator.pickle", "rb") as file:
    new_clf = pickle.load(file)

accuracy = accuracy_score(
    y_true=digits.target,
    y_pred=new_clf.predict(data),
)

assert accuracy > 0.96
