#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from sklearn.tree import DecisionTreeClassifier


sys.path.append("../tools/")
from email_preprocess import preprocess
from mylib import fit_and_predict


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


def task1(features_train=features_train, features_test=features_test,
          labels_train=labels_train, labels_test=labels_test):
    """
    Part 1: Get the Decision Tree Running
        Get the decision tree up and running as a classifier, setting min_samples_split=40.
        It will probably take a while to train.  What’s the accuracy?
    :return: accuracy
    """
    clf = DecisionTreeClassifier(min_samples_split=40)
    accuracy = fit_and_predict(clf, features_train, features_test, labels_train, labels_test)
    print("Tree {:.3}".format(accuracy))
    return accuracy


def task2(features_train=features_train):
    """
    What's the number of features in your data?
        (Hint: the data is organized into a numpy array where the number of rows
        is the number of data points and the number of columns is the number of features;
        so to extract this number, use a line of code like len(features_train[0]).)
    :return: number of features
    """
    result = len(features_train[0])
    print(result)
    return result


task1()
task2()
