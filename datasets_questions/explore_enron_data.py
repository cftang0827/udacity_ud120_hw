#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import operator


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


print(sorted(enron_data.keys()))
print(enron_data['PRENTICE JAMES'].keys())
print(len(enron_data))
print(len(next(iter(enron_data.values()))))
print(len([x for x in enron_data.values() if x["poi"] == True]))
print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
# get max payments value and owner of them. list is 0-indexed
print(max(enumerate((enron_data['FASTOW ANDREW S']['total_payments'],
          enron_data['SKILLING JEFFREY K']['total_payments'],
          enron_data['LAY KENNETH L']['total_payments'])), key=operator.itemgetter(1)))
print(enron_data['PRENTICE JAMES'])
print(len([x for x in enron_data.values() if x['salary'] != 'NaN']))
print(len([x for x in enron_data.values() if x['email_address'] != 'NaN']))

