# Comparison Operators:
x = 2
print(x == 2)
print(x != 2)
print(x == 3)
print(x < 3)
print(x <= 3)
print(x > 4)
print(x >= 4)

# Logical/Boolean Operators: Used to combine multiple conditions.
# The "and" and "or" boolean operators allow building complex boolean expressions, for example:

name = "Sagar"
age = 25
if name == "Sagar" and age == 25:
    print("Your name is Sagar, and your are 25 year old.")
elif name == "Kaustubh" and age == 24:
    print("Your name is Kaustubh and your are 24 years old.")
else: 
    print("Both the conditions are not matched")


name = "Damayant"
if name == "Sagar" or name == "Damayant":
    print("Your name is either Sagar or Damayant.")

# Membership Operators: Used to check membersship in sequence like list tuples, strings.

name = "Sagar"
if name in ["Damayant", "Kaustubh"]:
    print("Your name is either Damayant or Kaustubh.")
else:
    print("Your name is neither Damayant nor kaustubh.")

Statement = False
another_statement = True
if Statement is True:
    print("Statement is True. Performing the first action.")
elif another_statement is True:
    print("Another Statement is True. Performing the second action.")
else:
    print("Neither statement is True. Performing the defualt action")

# Identity Operators: Used to compare the memory locations of two objects.
# `is`: True if bothh variables point to the same objects.

x = [1,2,3]
y = [1,2,3]
print(x == y) # print out True
print(x is y) # print out False

# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.

# `not`: True if the condition is false, in other words Using "not" before a boolean expression inverts it.

print(not False) # prints out True
print(not False == (False)) # print out False

# Exercise: Change the variables in the first section, so that each if statement resolves as true.

number = 20
# Changed from 10 to 20 to satisfy the condition number > 15
second_number = 10  
# This variable is not used in any condition
first_array = [1, 2, 3] 
# Changed from an empty list to a list with two elements to make it truthy and to satisfy the length condition
second_array = [1, 2] 
# Changed from [1, 2, 3] to [1, 2] to satisfy the length condition and element condition

if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and second_array[0] == 1:
    print("5")
if not second_array:
    print("6")

# Explanation of the changes:

# number is set to 20 to ensure it is greater than 15.
# first_array is changed to [1, 2, 3] to make it non-empty (truthy).
# second_array is changed to [1, 2] to ensure its length is 2.
# The lengths of first_array and second_array now add up to 5.
# second_array still has 1 as its first element.
# Since second_array is not empty, the last condition if not second_array: will not print anything, which is correct as we don't want it to print "6".