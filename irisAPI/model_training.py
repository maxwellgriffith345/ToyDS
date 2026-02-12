import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
import pickle
import os

# load the data
iris = load_iris(as_frame=True)
X,y = iris['data'],iris['target']


# NOT DOING CROSS VALIDATION HERE
# withholding a test set for the API
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size = 0.10, random_state = 42)


# train the model
# how many layers will this have by default?
clf = tree.DecisionTreeClassifier()
clf  = clf.fit(X_train,y_train)
