#! /usr/bin/env python
#A miniPython example

#! /usr/bin/env python
#A miniPython example

# Testing lessc comparison, printing complicated expression (power, remainder included)
# prefix and postfix increment and decrement are functional. Applied on expression
# += and -= are functional.
# function within function with increment is functional.
# List definition and assert are functional.

if x <3+2:
	print 3+2**3*4%2

def funct(x,y):
    return x + y
while  x != funct(1,2):
    x = funct(1,2)**funct(2,1)
b = b++
b = (++b)%2
b = (funct(1,2) + b)++
b = (funct(1,2))++

c += 2
c-= (++b)%c

a = [1,2,3]
assert 2, 3

for x in a:
    print x, x++, (x%(x+1))++
    print funct(funct(x,x++), x++) - 2