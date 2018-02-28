#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

from tools.mylib import fit_and_predict

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


clf = SVC()
parameters = {'kernel': ('linear', 'rbf'),
              'C': [10 ** i for i in range(-5, 5)],
              'gamma': [10 ** i for i in range(-5, 5)]
              }
clf = GridSearchCV(clf, parameters)
accuracy = fit_and_predict(clf, features_train, features_test, labels_train, labels_test)
print("SVC {:.3}".format(accuracy))
clf = AdaBoostClassifier(n_estimators=15)
accuracy = fit_and_predict(clf, features_train, features_test, labels_train, labels_test)
print("AdaBoost {:.3}".format(accuracy))
clf = RandomForestClassifier(n_estimators=15)
accuracy = fit_and_predict(clf, features_train, features_test, labels_train, labels_test)
print("RandomForest {:.3}".format(accuracy))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
