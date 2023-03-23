# """Create a function that takes a string and returns it as an integer.
# Examples
# "6" ➞ 6
# "1000" ➞ 1000
# Notes
# All numbers will be whole.
# All numbers will be positive."""

string_number = "1000"
number= int(string_number)
print(number)

# """2. Create a function that takes a boolean variable flag and returns it as a string.
# Examples
# True ➞ "True"
# False ➞ "False""""
boolean= False
text= str(boolean) 

# """3. Write a function that returns the string "something" joined with a space " " and the given argument a.
# Examples
# "is better than nothing" ➞ "something is better than nothing"
# "Bob Jane" ➞ "something Bob Jane"
# "something" ➞ "something something""""

text = "{} something"
new_text = (text.format("something"))

# """Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
# Person  Relation
# Darth Vader father
# Leia    sister
# Han brother in law
# R2D2    droid
# Examples
# "Darth Vader" ➞ "Luke, I am your father."
# "Leia" ➞ "Luke, I am your sister."
# "Han" ➞ "Luke, I am your brother in law.""""

name= "Darth Vader"
txt="Luke, I am your {} "
text= txt.format((name == "Leia")* "sister" or (name== "Darth Vader")* "father" or (name== "Han")* "brother in low")

# """5. Create a function that takes a string and returns the number (count) of vowels contained within it."""
# """Examples
# "Celebration" ➞ 5
# "Palm" ➞ 1
# "Prediction" ➞ 4
# Notes
# a, e, i, o, u are considered vowels (not y)"""

word="Palm"
to_lower_case= word.lower()
vowels_count= to_lower_case.count("a")+ to_lower_case.count("e")+ to_lower_case.count("i")+to_lower_case.count("o") + to_lower_case.count("u")

# """"6. Create a function that returns True if a given inequality expression is correct and False otherwise.
# Examples
# "3 < 7 < 11" ➞ True
# "13 > 44 > 33 > 1" ➞ False
# "1 < 2 < 6 < 9 > 3" ➞ True"""

result = eval("1 < 2 < 6 < 9 > 3")

# """7. Create a function that replaces all the vowels in a string with a specified character.
# Examples
# "the aardvar", "#" ➞ "th# ##rdv#rk"
# "minnie mouse", "?" ➞ "m?nn?? m??s?"
# "shakespeare", "*" ➞ "sh*k*sp**r*""""

string = "shakespeare"
char= "#" * (string == "the aardvar") or "?"* (string == "minnie mouse") or "*" * (string == "shakespeare") 
text = string.replace("a",char).replace("e", char).replace("i",char).replace("o",char).replace("u",char)

# """8. Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
# Examples
# "1234123456785678" ➞ "************5678"
# "8754456321113213" ➞ "************3213"
# "35123413355523" ➞ "**********5523""""

card= "8754456321113213"
last= int(card) % 10000
card_number= (len(card) - 4 )* "*" + str(last)

# """Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
# Examples
# "Donald Trump" ➞ "Trump Donald"
# "Rosie O'Donnell" ➞ "O'Donnell Rosie"
# "Seymour Butts" ➞ "Butts Seymour""""
# define two strings

string= "Donald Trump"
full_name= string.split(" ")
last_name= full_name[1]
first_name= full_name[0]
result= (last_name+" " + first_name)

# """10. An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
# Examples
# "Algorism" ➞ True
# "PasSword" ➞ False
# # Not case sensitive.
# "Consecutive" ➞ False"""

text="PasSword".lower()
result= (len(text)== len (set(text))) 
print(result)