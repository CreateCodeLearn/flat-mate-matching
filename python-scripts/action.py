#!/usr/bin/env python

import cgi
#from Algorithm import myAlg


#get the output of the form.
form = cgi.FieldStorage()#

import pickle
#import pickle to be able to read the binariy file
data = pickle.load(open("data/fake_dict_data.p","rb"))
#get output from the file and name it as "data"

#C:\Users\Admin\Documents\flat-mate-matching\python-scripts>python action.py
#C:\Users\Admin\Documents\flat-mate-matching\python-scripts

#get an input filed from the form callled 'name'
#and assign it's value to a local variable called v_name
v_gender = form.getvalue('Gender')
v_area = form.getvalue('Area')
v_age = form.getvalue('myAge')
v_budget = form.getvalue('myBudget')


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
""" %(v_gender,v_area,v_age,v_budget)

items = []
for item in flatorder:
    items.append(flatsupplier.get(item))
    Location = flatsupplier.get(item).get("Location")
    Rent = flatsupplier.get(item).get("Rent")

    BODY_TEXT += """
Location: %s<br>
""" %(Rent,Location)


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
