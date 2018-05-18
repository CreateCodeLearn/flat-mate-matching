#!/usr/bin/env python

import cgi
#from Algorithm import myAlg

#get the output of the form.
form = cgi.FieldStorage()


#get an input filed from the form callled 'name'
#and assign it's value to a local variable called v_name
v_gender = form.getvalue('Gender')
v_area = form.getvalue('Area')
v_age = form.getvalue('myAge')
v_budget = form.getvalue('myBudget')

#send an html response.
print ("""
<html>
<body>
<h1>
Gender: %s <br>
Area: %s <br>
Age: %s <br>
Budget: %s
</h1>
</body>
</html>
""" % (v_gender,v_area,v_age,v_budget
))
