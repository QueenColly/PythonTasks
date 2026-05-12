#Exercise4.3 Sporting the error in the code

#The function cube(x) calculates the value but does not "return" it. In #Python, if a function doesn't have a return statement, it returns None by #default.

#Correction of the code

def cube(x):
    return x ** 3

print('The cube of 2 is', cube(2))
