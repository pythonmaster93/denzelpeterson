#!/usr/bin/env python
# coding: utf-8

# [ ] get input for input_test variable
print("Enter food eaten in last 24 hours: ")
input_test = input().lower()

# [ ] print "True" message if "dairy" is in the input or False message if not
print("It is",'dairy' in input_test, "that", input_test, 'contains "dairy"')

# [ ] print True message if "nuts" is in the input or False if not
print("'nuts' in input = ", 'nuts' in input_test)

# [ ] Challenge: Check if "seafood" is in the input - print message
print("'seafood' in input = ", 'seafood' in input_test)

# [ ] Challenge: Check if "chocolate" is in the input - print message
print("'chocolate' in input = ", 'chocolate' in input_test)