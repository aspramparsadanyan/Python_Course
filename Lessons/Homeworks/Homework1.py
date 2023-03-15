# '''1. For this challenge, you are supposed to find the stum of the digits of a two-digit number.
# 45 ➞ 9 38 ➞ 11 67 ➞ 13 '''

# input = 45
# sum = (input % 10)+ (input // 10) == 9
# print(sum)


# input = 38
# sum = (input % 10) + (input // 10) == 11
# print(sum)

# input = 67
# sum = (input % 10) + (input // 10) == 13
# print(sum)

# '''Need extra knowledge!! 
# 2. A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
# 44 ➞ True
# 45 ➞ False
# -44 ➞ False'''

# def is_number_repdigit(num):
#      return (num % 10) == (num // 10)
# print(is_number_repdigit(44))
# print(is_number_repdigit(45))
# print(is_number_repdigit(-44))

 
# '''3. Write a function that takes an integer minutes and converts it to seconds.
# 5 ➞ 300
# 2 ➞ 120'''

# def convert_minute_to_second(min):
#     return(min * 60)
# print( convert_minute_to_second(5) )
# print( convert_minute_to_second(2))



# '''4. Create a function that takes the age in years and returns the age in days.
# 65 ➞ 23725
# 0 ➞ 0
# 20 ➞ 7300'''

# def year_in_days(year):
#     return(year * 365)
# print(year_in_days(65))
# print(year_in_days(0))
# print(year_in_days(20))



# '''5. Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
# 1,3 ➞ 3780
# 2,0 ➞ 7200'''

# def hour_in_second(hour,minute):
#     return(hour * 60 * 60) + (minute * 60)
# print(hour_in_second(1, 3))
# print(hour_in_second(2,0))




# '''6. Create a function that accepts a measurement value in inches 
# and returns the equivalent of the measurement value in feet.'''
# def inch_to_feet(inch, one_inch_in_feet):
#     return(inch * one_inch_in_feet) 
# print(inch_to_feet(100, 0.0833333333))


'''7. Create a function that takes a number 
as an argument and returns "even" for even numbers and "odd" for odd numbers.'''

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_or_odd(5))
print(even_or_odd(8))  
print(even_or_odd(1)) 








