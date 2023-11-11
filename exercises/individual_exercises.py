

### PART I - Python programming

#1getting_started.py

# 1. Syntax

# 1.1 Insert the missing indentation to make the code correct:
# HINT: https://www.w3schools.com/python/python_syntax.asp

# TODO: update the code below
if 4 ==2 :
print("Four is equal to two!")


# 1.2 Variables
# HINT: https://www.w3schools.com/python/python_variables.asp

#1.2.1 Create a variable named fruit and assign the value Apple to it.
# TODO: Write your code below



# 1.2.2 Create a variable called z, assign x + y to it, and display the result.

x = 10
y= 20

# TODO: Wrtie your code below



# 1.2.3 Remove the illegal characters in the variable name:

# TODO: Update the code below
2city-name = "London"

# 1.2.4 Insert the correct keyword to make the variable x belong to the global scope.
# HINT: https://www.w3schools.com/python/python_variables_global.asp

# TODO: Update the code below
def myfunc():
  _______ x
  x = "fantastic"



# 1.2.5 write a program that switches the values stored in variables a and b.

a = 5
b = 4

# TODO: Write your code below



print('a : ',a)
print('b : ',b)


# 1.3. Data Types
# casting, numbers, booleans
# HINT: https://www.w3schools.com/python/python_datatypes.asp

# 1.3.1 Write a program that add the digits in a two digit number input.
# eg. if the input is 45. The the output should be 4+5=9

number= input()

# TODO: Wrtie your code below



#2string.py

# 2.1 Strings
# HINT: https://www.w3schools.com/python/python_strings.asp

txt = "Merry Christmas"


# 2.1.1 print the length of the string
# TODO: Write your code below



# 2.1.2 Print the first character of the string txt.
# TODO: Write your code below



# 2.1.3 Get the characters from index 1 to index 3 (ell).
# TODO: Write your code below



# 2.1.4 Convert the value of txt to upper case and print it.
# TODO: Write your code below


# 2.1.5 Convert the value of txt to lower case and print it.
# TODO: Write your code below


# 2.1.6 Return the string without any whitespace at the beginning or the end.
x = " Hello World "
# TODO: Write your code below



# 2.1.7 Replace the character H with a J and print the result
y = "Hello"
# TODO: Write your code below


# 2.1.8 Insert the correct syntax to add a placeholder for the name parameter.
# TODO: Update the code below
name = 'John'
txt = "My name is __"
print(txt.format(name))



#3operators.py

# 3.1 Operators

# 3.1.1 Multiply 4 with 8, and print the result.
# TODO: Write your code below



# 3.1.2 Divide 30 by 6, and print the result.
# TODO: Write your code below



#4collections.py

# 4.1 PYTHON Lists

fruits = ["kiwi", "pineapple", "apple"]

# 4.1.1 Print the second item in the fruits list.
# TODO: Write your code below



# 4.1.2 Change the value from "kiwi" to "orange", in the fruits list.
# TODO: Write your code below



# 4.1.3 Use the insert method to add "lemon" as the second item in the fruits list.
# TODO: Write your code below



# 4.1.4 Use the remove method to remove "pineapple" from the fruits list.
# TODO: Write your code below



# 4.1.5 Use negative indexing to print the last item in the list.
# TODO: Write your code below


# 4.1.6 Use a range of indexes to print the third, fourth, and fifth item in the list fruits2.

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# TODO: Write your code below


# 4.1.7 Use the correct syntax to print the number of items in the list fruits
# TODO: Write your code below



# 4.1.8 TODO: Write a program that add the average of numbers in a list scores.
# you are not allowed to use the sum() or len() functions.

scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below


# 4.1.9 TODO: Write a program that calculates the highest number in a list scores
# you are not allowed to use the max or min functions.
scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below



# 4.2. PYTHON Dictionaries

car =	{
  "brand": "Renault",
  "model": "Clio",
  "year": 2018
}

# 4.2.1 Use the get method to print the value of the "model" key of the car dictionary.
# TODO: Write your code below



# 4.2.2 Change the "year" value from 2018 to 2020 in the car dictionary.
# TODO: Write your code below



# 4.2.3 TODO: Add the key/value pair "color" : "blue" to the car dictionary.
# TODO: Write your code below



# 4.2.4 Use the pop method to remove "model" from the car dictionary.
# TODO: Write your code below



# 4.2.5 Use the clear method to empty the car dictionary.
# TODO: Write your code below




# 5conditoins.py

# 5.1 If ... else

a = 20
b = 40

c=10
d=40

# 5.1.1 Print "Yes" if a is equal to b, otherwise print "No".
# TODO: Write your code below




# 5.1.2 Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# TODO: Write your code below




# 5.1.3 Print "Hello" if a is equal to b, and c is equal to d.
# TODO: Write your code below




# 5.1.4 Print "Hello" if a is equal to b, or if c is equal to d.
# TODO: Write your code below




# 5.2 Write a program that checks whether an input number is odd or even. Print whether the input number is odd or even
# HINT:
# even numbers can be divided by 2 with no remainder. when odd numbers are divided by 2 there is a remainder.
# eg. 42 is even because 42/2 = 21 and has no remainder
# eg. example, 33 is odd because 33/3 = 16.5 is not a whole number.
# we can use the module operator (%) in python to get the remainder after a division.
# eg. 5%2 = 1 since 5 divided by 2 has a remainder 1. So 5 is odd
# eg. 6%2 = 0 since 6 divided by 2 has a remainder 0. So 6 is even.

#number to check
number = int(input('Enter a number'))

# TODO: write your code below




# 6loops.py

# 6.1 For Loops

fruits = ["kiwi", "banana", "cherry"]

# 6.1.1 Use a for loop to loop through the items in the fruits list and print each item.
# TODO: Write your code below




# 6.1.2 In the for loop to loop through the items in the fruits list,  when the item value is "banana", jump directly to the next item.
# TODO: Write your code below




# 6.1.3 In the for loop to loop through the items in the fruits list, exit the loop when the item is "banana".
# TODO: Write your code below




# 6.1.4 Using the Python range() function, create a sequence of numbers from 0 to 5, and print each item in the sequence in a new line:
# HINT: https://www.w3schools.com/python/ref_func_range.asp
# TODO: Write your code below



# 7functions.py

# 7.1 Functions

# 7.1.1 Create a function named function1 that prints this string "Hello World"
# TODO: Write your code below





# 7.1.2 Execute the functon function1
# TODO: Write your code below





# 7.1.3 Create a function named function2 that takes in one integer parameter number1. The function adds 5 to the input number1, adds 5 to it and prints the result
# TODO: Write your code below





# 7.1.4 Create a function named function2 that takes in one integer parameter number1. The function adds 5 to the input number1, adds 5 to it and prints the result
# TODO: Write your code below





# 7.1.5 Create a function named compare_numbers() with two arguments. If the first argument is greater than the second, print "first number is greater".
# If the second number is greater than the first, print "first number is smaller". Is the numbers are equal, print "equal numbers"
# TODO: Write your code below






# 7.2 Create a lambda function that takes one parameter (a) and returns it.
# TODO: Write your code below





### 7.3 Python built-in functions : https://www.w3schools.com/python/python_ref_functions.asp

nums = [11,33,14,2,58,65,34]

# 7.3.1 Using Python's built in sum() function, print the sum of the numbers in the list nums
# TODO: Write your code below





# 7.3.2 Using Python's built in min() function, print the minimum of the numbers in the list nums
# TODO: Write your code below





# 7.3.3 Using Python's built in abs() function, print the absolute value of -6.
# TODO: Write your code below




# 7.3.4 Using Python's built in round() function, round the number 4.67888 to two decomal places.
# TODO: Write your code below





# 7.4 Python Modules
# HINT: https://www.w3schools.com/python/python_modules.asp
# HINT: https://realpython.com/python-modules-packages/
# HINT: https://docs.python.org/3/tutorial/modules.html


# 7.4.1 Create a python module mod.
# In mod.py, create a function psum(number1, number2) that takes two arguments and prints the sum of them.
# In mod.py, create a function pmultiply(number1, number2) that takes two arguments and prints the product of them.


# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions fromthe module mod.


# 7.4.3 In main.py, also import Python's built in module platform. Then list the functions and variables in the platform module using the dir() function.








# 8pandas.ipynb

### Part2 - applications

# 13 Pandas
# import data, clean data, filter data, aggregate data, plot data
# reference: https://www.w3schools.com/python/pandas/default.asp

# 8.1 import the csb file Credit.csv into a pandas dataframe Credit using the read_csv() function in the pandas package
# TODO: Write your code below



# 8.2 print the top 10 rows in Credit using the head() function of pandas
# TODO: Write your code below



# 8.3 print information about Credit using the info() function of pandas.
# TODO: Write your code below



# 8.4 using the shape attribute of pandas, print the number of rows and columns in Credit
# HINT: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# TODO: Write your code below




# 8.5 if any, drop rows with missing values from the Credit dataframe
# TODO: Write your code below




# 8.6 Calculate correlation coefficients between the numeric columns in Credit using the corr() function in pandas
# TODO: Write your code below




# 8.7 Grouped by student, calculate the sum of Balance and average of Balance
# HINT: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# TODO: Write your code below




# 8.8 Using the plot() function in pandas, plot a histogram of Balance
# HINT: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# TODO: Write your code below




# 8.9 Using the plot() function in pandas, draw a scatterplot of Income vs. Balance
# HINT: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# TODO: Write your code below
