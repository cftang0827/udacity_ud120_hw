#!/usr/bin/python

from operator import itemgetter


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    PART_TO_BE_REMOVED = 0.1
    cleaned_data = [(age[0], worth[0], (worth[0] - pred[0])**2)
                    for pred, age, worth in zip(predictions, ages, net_worths)]
    cleaned_data = sorted(cleaned_data, key=itemgetter(2))
    size = len(cleaned_data)
    cleaned_data = cleaned_data[0:int(size * (1 - PART_TO_BE_REMOVED))]
    return cleaned_data

