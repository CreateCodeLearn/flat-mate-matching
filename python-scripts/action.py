#!/usr/bin/env python

import cgi
#from Algorithm import myAlg


#get the output of the form.
form = cgi.FieldStorage()#

import pickle
#import pickle to be able to read the binariy file
#data = pickle.load(open("data/fake_dict_data.p","rb"))
#get output from the file and name it as "data"

##Algorithm from J
def flat_match (v_location,v_gender,v_rent,v_lowerage,v_upperage, filepath):
    '''
    Provides the dataset in CSV and based on input data uses booleans
    to subset the data to give the flats ranked according rent with cheapest
    showing first
    '''
    import pandas as pd

    def transform_data(dataframe):
        dd = dict()
        index = dataframe.sort_values("rent").index.tolist()
        for i in index:
            dd[i] = dataframe.loc[i].to_dict()
        return dd, index

    data = pd.read_csv(filepath, index_col=0)

    boolean_location = data["location"] == v_location
    boolean_gender = data["gender"] == v_gender
    boolean_rent = data["rent"] <= v_rent
    boolean_lowerage = data["lowerage"] >= v_lowerage
    boolean_upperage = data["upperage"] <= v_upperage

    user_constraints = boolean_location & boolean_gender & boolean_rent #& boolean_lowerage & boolean_upperage
    results = data.loc[user_constraints]

    return transform_data(results)

#C:\Users\Admin\Documents\flat-mate-matching\python-scripts>python action.py
#C:\Users\Admin\Documents\flat-mate-matching\python-scripts

#get an input filed from the form callled 'name'
#and assign it's value to a local variable called v_name
v_gender = "female"#form.getvalue('Gender')
v_area = "Mitte"#form.getvalue('Area')
v_age = 40#form.getvalue('myAge')
v_budget = 400#int(form.getvalue('myBudget'))

print(v_age)
data= flat_match(v_location=v_area,v_gender=v_gender,v_rent=v_budget,v_lowerage=v_age-5,v_upperage=v_age+5, filepath="data/large_supply_data.csv")

print(data)
import os
print(os.getcwd())

#extracting data from the tuple
flatsupplier = data[0]

flatorder = data[1]

print (flatorder)
# output [3, 19, 11, 2, 18, 15, 8, 5]

print (flatorder[0])
#best fit, as the 1st position on flatorder
#output 3

BODY_TEXT="""
Gender: %s <br>
Area: %s <br>
Age: %s <br>
Budget: %s<br>
""" %(v_gender,v_area,str(v_age),str(v_budget))

items = []
for item in flatorder:
    items.append(flatsupplier.get(item))
    Location = flatsupplier.get(item).get("Location")

    BODY_TEXT += """
Location: %s<br>
""" %(Location)


#extract from dict file the key for flatorder 0
bestfit = flatsupplier.get(flatorder[0])
print (bestfit)
#output {'Location': 'Neukolln', 'Gender': 'Male', 'Rent': 300, 'lowerage': 21, 'upperage': 32}

Location = bestfit.get("Location")
print (Location)
#output Neukolln



OPENING= """
<html>
<body>
<h1>
"""
CLOSING="""
</h1>
</body>
</html>
"""

print(OPENING+BODY_TEXT+CLOSING)
