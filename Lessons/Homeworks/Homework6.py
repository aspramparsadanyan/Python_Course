# EXTRA Knowledge
# 1. Given three lists of integers: lst1, lst2, lst3, 
# return the sum of integers which are common in all three lists.
# Examples
# sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
# // 2 & 3 are common in all 3 lists.
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
# // 2, 2 & 3 are common in all 3 lists.
# sum_common([1], [1], [2]) ➞ 0

list1=[1, 2, 3]
list2= [5, 3, 2]
list3=[7, 3, 2]
num=0
for x in list1:
 if x in list2 and x in list3:
   num=num+x


# """"EXTRA Knowledge
# 2. Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# [1, 2, 3, 4, 5, 6] ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# [-1, -2, -3, -4, -5, -6] ➞ [-12, -9]
# [0, 0] ➞ [0, 0]
# Notes
# Count 0 as an even number.
list= [-1, -2, -3, -4, -5, -6]
zujg_tveri_gumar= 0
kent_tveri_gumar=0
for x in list:
  if x % 2==0:
    zujg_tveri_gumar= zujg_tveri_gumar+x
  else: kent_tveri_gumar= kent_tveri_gumar+x
print([zujg_tveri_gumar, kent_tveri_gumar])

# 3. Create a function that takes a dictionary of objects like 
# { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like
# { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }

dict= {"name": "Zygmund", "notes": [1, 2, 3] }
new_dict= {"name": dict["name" ], "Top note" : max(dict["notes"])}



# 5. You work for a manufacturer, and have been asked to calculate the total 
# profit made on the sales of a product. You are given a dictionary containing the cost price 
# per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total 
# profit made, rounded to the nearest dollar.
# Examples
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796
# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }) ➞ 32411
# profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }) ➞ 44030

dict= {"cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500}
profit= int(round((dict["sell_price"]- dict["cost_price"])* dict["inventory"], 2))


# 6. A number is said to be Harshad if it's exactly divisible by t
#he sum of its digits. Create a function that determines whether a number is a Harshad or not.
# Examples
# is_harshad(75) ➞ False
# # 7 + 5 = 12
# # 75 is not exactly divisible by 12

 
# is_harshad(171) ➞ True
# # 1 + 7 + 1 = 9
# # 9 exactly divides 171
 
# is_harshad(481) ➞ True
# is_harshad(89) ➞ False
# is_harshad(516) ➞ True
# is_harshad(200) ➞ True

number= str(89)
tveri_gumar=0
for x in number:
  tveri_gumar= int(x)+ tveri_gumar

print(int(number) % tveri_gumar==0)

# EXTRA Knowledge
# 7. Given an input string, reverse the string word by word.
# Examples
# "the sky is blue" ➞ "blue is sky the"
# "  hello world!  " ➞ "world! hello"
# "a good   example" ➞ "example good a"
# Notes
# A word is defined as a sequence of non-space characters.
# The input string may contain leading or trailing spaces. 
# However, your reversed string should not contain leading or trailing spaces.
# Try to solve this in linear time.
sentance= "a good example"
lower= sentance.lower()
list= lower.split()
string=" "
for x in reversed(list):
    string= string+x + " "
    
# Extra Knowledge
# 8. Create a function that builds a word from the scrambled 
# letters contained in the first list. Use the second list to establish each position of 
# the letters in the first list. Return a string from the unscrambled letters (that made-up the word).
# Examples
# word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"
# word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"
# word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit"

letter= ["b", "e", "t", "i", "d", "a"]
indexes= [1, 4, 5, 0, 3, 2]
txt= ""

for x in indexes:
    txt= txt + letter[x]



# 9. Create a function to test if a string is a valid pin or not.
# A valid pin has:
# Exactly 4 or 6 characters.
# Only numerical characters (0-9).
# No whitespace.
# Examples
# valid("1234") ➞ True
# valid("45135") ➞ False
# valid("89abc1") ➞ False
# valid("900876") ➞ True
# valid(" 4983") ➞ False
# Notes
# Empty strings should return False when tested.
numbers= "1234"
len= len(numbers)
print((len==4 or len==6) and numbers.isnumeric() and " " not in numbers)
    
# 10. Return a new set of identical items from two sets
# Given:
# set1 = {10, 20, 30, 40, 50}
# print(set1)
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}
set1= {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

intersection = set1.intersection(set2)


# 11. Write a Python program to return a new set with unique items from both sets by removing duplicates.
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 40, 10, 50, 20, 60, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2)


# 12. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
# Given:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:
set1 {10, 30}
set1 = {10, 20, 30,}
set2 = {20, 40, 50}
difference= set1.difference(set2)


# EXTRA Knowledge
# 13. Given an input string, reverse the string word by word (reversed word also).
# Examples
# "the sky is blue" ➞ "eulb si yks eht"
# Notes
# A word is defined as a sequence of non-space characters.
# The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# Try to solve this in linear time."""
sentence= "the sky is blue"
list= sentence.split()
reversed_text= reversed(list)
string= " "
for x in reversed_text:
    txt= x[:: -1]
    string= string + txt + " "
    

