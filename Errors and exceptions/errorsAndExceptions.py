'''
Identify errors in the following code blocks and evaluate them with specific exceptions to avoid uncontrolled errors in our programs. 
Add explanatory messages for the user.

1) Code to be evaluated:
'''
try:
    number = 7/0
except ZeroDivisionError as e:
    print("Error:", type(e).__name__)
    print("Cannot divide by zero, try another number")
else:
    print("Division successfully completed")

'''2) Code to be evaluated: '''

list = [4, 7, 30, 23, 5]

try:
    list[10]
except IndexError as e:
    print(type(e).__name__ + ": A sequence with an index outside the list range cannot be accessed.")
else:
    print("Index read correctly")

'''3) Code to be evaluated: '''
countries = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

try:
    countries["alemania"]
except KeyError as e:
    print(type(e).__name__)
    print("This key does not exist in the dictionary countries")
except ValueError:
    print("You must enter a country")

'''
4) Locate the error in the following code block. Create an exception to prevent the program from crashing and 
also explain in a message to the user the cause and/or solution:
'''
try:
    result = "2" + 10
except TypeError:
    print("Error: Cannot add a number and a string, only number and number.")
finally:
    print("End of try block")

'''
5) Make a function called add_without_repeats() that receives a list and an element. 
The function must add the element at the end of the list with the condition of not repeating any element. 
Also if this element is already in the list it must invoke a ValueError which you must catch and display this message instead:

  Error: Unable to add duplicate elements => [element].
Try adding the elements 7, "Python" and 5 through the function add_without_duplicates() and print the complete list at the end.
'''
elements = [3, 5, 10]

def add_without_repeats(element):
        try:
            if element in elements:
                raise ValueError  # Invocamos un error si el elemento ya se encuentra en la lista
            else:
                elements.append(element)
                print("Element successfully added to the list")
        except ValueError as e:
            print("Error: Unable to add duplicate items => [{}]".format(element))

add_without_repeats(7)
add_without_repeats("Python")
add_without_repeats(5)
print(elements)

'''
6) Look in the documentation for another exception that has not been used so far and perform the following steps:
Cause the error in sample code.
Once you have raised them, control them with try-except.
Show the user the default information provided by the exception. Hint: as
Customise the message provided to the user using all of the above.
'''
try:
    import bson
except ModuleNotFoundError as e: # If the named module is not found, a ModuleNotFoundError is generated.
    print(e)
    print("Error: The module does not exist")
