# """1. Create a function that takes a list containing only numbers and return the first element"""
list= [80, 5, 100]
first_number = list[0]

# """"2.  Create a function that takes a list of numbers. Return the largest number in the list.
# Examples
# [4, 5, 1, 3] ➞ 5"""
# 
list= [4, 10, 1, 3]
print(max(list))

# """3. Create a function that takes a list of numbers and returns the smallest number in the list.
# Examples
# [34, 15, 88, 2] ➞ 2"""

list= [0.4356, 0.8795, 0.5435, -0.9999]
print(min(list))

# """4. Create a function that takes a list and returns the difference between the biggest and smallest numbers.
# Examples
# [10, 4, 1, 4, -10, -50, 32, 21] ➞ 82
# # Smallest number is -50, biggest is 32.
# [44, 32, 86, 19] ➞ 67
# # Smallest number is 19, biggest is 86."""

list= [44, 32, 86, 19]
differance= max(list)-  min(list)


# """5. Create a function to concatenate two integer lists.
# Examples
# [1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]"""

list1 = [7, 8] 
list2 = [10, 9, 1, 1, 2]
list1.extend(list2)


# """6. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.
# Examples
# [5, 57] ➞ True"""

list= [5, 100]
sum_less_then_100= sum(list)<100


# """7. Given a list of integers, determine whether the sum of its elements is even or odd.
# The return value should be a string "odd" or "even".
# If the input list is empty, consider it as a list with a zero [0].
# Examples
# [0] ➞ "even"
# [1] ➞ "odd"
# [] ➞ "even"
# [0, 1, 5] ➞ "even"""

list= [1,5,2]
even_odd= (sum(list) % 2== 0) * "Even" or "Odd"
#

# """8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# Examples
# "11/12/2019" ➞ "20191211"
# "12/31/2019" ➞ "20193112"
# "01/15/2019" ➞ "20191501"""

time="11/12/2019"
split= time.split("/")
year= split[2]
day= split[1]
month= split[0]
year_day_month= year+day+month


# # EXTRA Knowledge
# # 9. Create a function that takes two numbers as arguments num, length and returns a list of multiples of num until the list length reaches length.
# # Examples
# # 7, 5 ➞ [7, 14, 21, 28, 35]

number= 7
length= 5
list = list(range(number, number*(length+1), number))



# # "10. Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
# # "Asc" returns a sorted list in ascending order.
# # "Des" returns a sorted list in descending order.
# # "None" returns a list without any modification.
# # Examples
# # [4, 3, 2, 1], "Asc"  ➞ [1, 2, 3, 4]
# # [7, 8, 11, 66], "Des" ➞ [66, 11, 8, 7]
# # [1, 2, 3, 4], "None" ➞ [1, 2, 3, 4]"

list=[7, 8, 11, 66]
s= "qwe"
ordered= True * (s=="Des") or False* (s== "Asc") or "" * (s=="None")
list=((ordered == '') * list or sorted(list, reverse=ordered))
