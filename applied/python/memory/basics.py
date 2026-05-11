a = 5
b = a # this is a reference by default
id(a) == id(b) # => this is true

d = {'a':1, 'b':2, 'c': 3}
c = d.copy() # This is shallow copy of d which means id(d['a']) is equalt to id(c['a']) that is it just copies pointers/references

id(c) != id(d) # this will be true

# for deep copy
import copy
d_copy = copy.deepcopy(d) # this will create a deep copy of the dictionary
id(d_copy) != id(d) # this will be true


def fun(d_arg:dict): # by default everything is passed as reference in args
    global d
    # if we pass d to the fun it will be passed as reference
    id(d) == id(d_arg) # this will be true
