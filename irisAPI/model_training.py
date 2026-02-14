import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
import os

# load the data
iris = load_iris(as_frame=True)
X,y = iris['data'],iris['target']


# NOT DOING CROSS VALIDATION HERE
# withholding a test set for the API
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size = 0.10, random_state = 42)

#export the test data
M_test = X_test.merge(y_test, left_index = True, right_index = True)
M_test.to_csv("data/Mtestdata.csv", index=False)
X_test.to_csv("data/Xtestdata.csv", index=False)

#Create pipeline the inlcudes data preprocessing steps and model
# Don't have any pre-preprocessing steps
pipeline = Pipeline([
    ('model', tree.DecisionTreeClassifier())
])

#train the pipeline
pipeline.fit(X_train, y_train)

#save the pipeline
# Use 'with' as a context manager
with open('model/irisdecisiontree.joblib', 'wb') as file:
    joblib.dump(pipeline, file)

print("model saved")
#Load the pipeline back in (would use in seperate file)
#loaded_pipeline = joblib.load('FILE PATH')
#predictions = loaded_pipeline.predict(new_data)

"""
# train the model
# how many layers will this have by default?
clf = tree.DecisionTreeClassifier()
clf  = clf.fit(X_train,y_train)
"""
