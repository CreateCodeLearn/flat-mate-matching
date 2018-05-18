#!/Users/mieter/miniconda3/bin/python

import cgi
#from Algorithm import myAlg

#get the output of the form.
form = cgi.FieldStorage()


#get an input filed from the form callled 'name'
#and assign it's value to a local variable called v_name
v_name = form.getvalue('Gender')
v_age = int(form.getvalue('Age'))
v_area = form.getvalue('Area')
v_budget = form.getvalue('demoRange')


#send an html response.
print ("""
<html>
<body>
<p>
Thanks, %s
age: %s
city: %s
</p>
</body>
</html>
""" % (v_name, v_age, v_area, v_budget))
