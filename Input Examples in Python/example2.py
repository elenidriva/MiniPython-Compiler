#! /usr/bin/env python
#A miniPython example

#! /usr/bin/env python
#A miniPython example

# Testing function definition, function call, assignment with function call + exp
# printing with function_call and comma_expression.
def add(e,f):
    return e + f
#b = add(1,2) + 2 
#print b
#print add(1,2), b

# Testing what happens with floats. Testing if one argument is another function_call.
def multFloat (e, f):
    return e * f
    
z = multFloat(2.0, 3.0) + 1.0 * 2.0
y = multFloat(2.0, add(1,2)) + 1.0