
# """1. Luke Skywalker has family and friends. Help him remind them who is who. 
# Given a string with a name, return the relation of that person to Luke.
# Person  Relation
# Darth Vader father
# Leia    sister
# Han brother in law
# R2D2    droid
# Examples
# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."""

def relation(name):
    if name == "Darth Vader":
        return "Luke, I am your father."
    elif name == "Leia":
        return "Luke, I am your sister."
    elif name == "Han":
        return "Luke, I am your brother in law."
    else: return "I dont know who are you"
print(relation("Aspram"))

# 2. Create a function that takes damage and speed (attacks per second) 
# and returns the amount of damage after a given time.
# Examples
# damage(40, 5, "second") ➞ 200
# damage(100, 1, "minute") ➞ 6000
# damage(2, 100, "hour") ➞ 720000
# Notes# Return "invalid" if damage or speed is negative.
def damage(a, b , operator): 
    if a <0 or b<0 or operator== "" or (operator != "second" and  operator !="minute" and  operator != "hour"):
         return "invalid"

    second_per_minute= 60
    second_per_hour= 3600
    initial_damage= a*b


    if operator== "minute":
     return initial_damage* second_per_minute
    elif operator== "hour":
     return initial_damage * second_per_hour
  
    return initial_damage

print(damage(100, 1, "hour"))


# 3. Create a function that takes a list of strings and integers,
# and filters out the list so that it returns a list of integers only.
# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
# filter_list(["Nothing", "here"]) ➞ []

def mix_list_to_integers(list):
  my_list= []
  for x in list: 
    if type(x)== int:
     my_list.append(x)
  return my_list
print(mix_list_to_integers([1, 2, 3, "a", "b", 4]))

# 4. Create a function that takes a number as an argument and returns 
# True or False depending on whether the number is symmetrical or not. 
# A number is symmetrical when it is the same as its reverse.
# Examples
# is_symmetrical(7227) ➞ True
# is_symmetrical(12567) ➞ False
# is_symmetrical(44444444) ➞ True
# is_symmetrical(9939) ➞ False
# is_symmetrical(1112111) ➞ True
def symmetrical(num):
    string= str(num)
    return string == string [::-1]

print(symmetrical(9939))



# 5. Create a function that changes all the elements in a list as follows:
# Add 1 to all even integers, nothing to odd integers.
# Concatenates "!" to all strings and make the first letter of the word a capital letter.
# Changes all boolean values to its opposite.
# Examples
# change_types(["a", 12, True]) ➞ ["A!", 13, False]
# change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
# change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
# Notes
# There won't be any float values.
# You won't get strings with both numbers and letters in them.
# Although the task may be easy, try keeping your code as clean and as readable as possible!
def edited_list(lst):
    result = []
    for x in lst:
        if isinstance(x, int) and x % 2 == 0:
            result.append(x + 1)
        elif isinstance(x, str):
            result.append(x.capitalize() + "!")
        elif isinstance(x, bool):
            result.append(not x)
        else:
            result.append(x)
    return result
print(edited_list(["False", "False", "true"]))

# 6. Create a function that takes a string s and returns a list of two-paired characters.
# If the string has an odd number of characters, add an asterisk * in the final pair.
# See the below examples for a better understanding:
# Examples
# string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
# string_pairs("edabit") ➞ ["ed", "ab", "it"]
# string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
# Notes
# Return [] if the given string is empty.
def string(word):
    if not word:
        return []
    pairs = [word[i:i+2] for i in range(0, len(word),2)]
    if len(word) % 2 == 1:
        pairs[-1] += "*"
    return pairs
print(string("airforces"))


# 7. Create a function that takes two parameters and, 
# if both parameters are strings, add them as if they were integers or if the two parameters are integers,
# concatenate them.
# Examples
# stupid_addition(1, 2) ➞ "12"
# stupid_addition("1", "2") ➞ 3
# stupid_addition("1", 2) ➞ None
# Notes
# If the two parameters are different data types, return None.
# All parameters will either be strings or integers.
def parametrs(par1, par2):
    if isinstance(par1, str) and isinstance(par2, str):
        return (int(par1) + int(par2))
    elif isinstance(par1, int) and isinstance(par2, int):
        return str(par1) + str(par2)
    else:
        return None
print(parametrs(1,2))

# 8. Write a function that does the following operations:
# adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. 
# Of course, the variables have to be defined, but in this challenge the variables will be defined for you.
# All you have to do is look at the variables, do some string to integer conversions, use some if conditionals,
# and combine them based on the operation.
# The numbers and operation will be given as strings, and you should return the value as a string as well.
# Examples
# operation("1", "2", "add" ) ➞ "3"
# operation("4", "5", "subtract") ➞ "-1"
# operation("6", "3", "divide") ➞ "2"
# Notes
# The numbers and operation will be given as strings, and you should also return the value as a string.
# If the answer is "undefined", return "undefined" (e.g. dividing by zero).
# For divide, go ahead and round down to an integer.
def operation(num1, num2, operator):
  number1= int(num1)
  number2=int(num2)
  if operator== "/" and number2==0:
    return "undefined" 
  if operator == "+":
    return str(number1 + number2) 
  elif operator == "-":
    return str(number1 - number2) 
  elif operator == "/":
        return str(((number1 / number2)) // 1)
  else:
      return("Error")
print(operation("5", "3", "*"))


# 9. Check if the given string consists of only letters and spaces and if every letter is in lower case.
# Examples
# letters_only("PYTHON") ➞ False
# letters_only("python") ➞ True
# letters_only("12321313") ➞ False
# letters_only("i have spaces") ➞ True
# letters_only("i have numbers(1-10)") ➞ False
# letters_only("") ➞ False
# Notes 
# Empty arguments will always return False.
# Input values will be mixed (symbols, letters, numbers).
def string(input_word):
    if input_word.isalpha() and input_word.islower():
        return True
    elif " " in input_word:
        return True
    elif input_word == "":
       return False
    else: return False
print(string("i have spaces"))

# 10. Write a function that takes a list and determines whether
# it's strictly increasing, strictly decreasing, or neither.
# Examples
# check([1, 2, 3]) ➞ "increasing"
# check([3, 2, 1]) ➞ "decreasing"
# check([1, 2, 1]) ➞ "neither"
# check([1, 1, 2]) ➞ "neither"
# Notes
# The last example does NOT count as strictly increasing, 
# since 1-indexed 1 is not strictly greater than the 0-indexed 1.
# Input lists have a minimum length of 2.""
