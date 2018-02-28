#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
from operator import itemgetter

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)  # quiz 17
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

print(max([(k, x['salary']) for (k, x) in zip(data_dict.keys(), data_dict.values())
           if x['salary'] != 'NaN'], key=itemgetter(1)))  # quiz 15

a = [(k, v['salary'], v['bonus']) for (k, v) in zip(data_dict.keys(), data_dict.values())
       if v['salary'] != 'NaN' and v['salary'] >= 10 ** 6
       and v['bonus'] != 'NaN' and v['bonus'] >= 5 * 10 ** 6]
print(a)
# two more for better analyzing
names = [a[0] for a in a]
names.append('PRENTICE JAMES')
names.append('COLWELL WESLEY')
print("\n".join([str(data_dict[name]) for name in names]))
