








# 1. Create a function which returns the number of true values there are in an array.
# Examples
# countTrue([true, false, false, true, false]) ➞ 2
# countTrue([false, false, false, false]) ➞ 0
# countTrue([]) ➞ 0
# Notes
# Return 0 if given an empty array.
# All array items are of the type bool (true or false).

def count(words): 
  countTrue = 0
  countFalse = 0
  for x in words:
    if x:
       countTrue += 1
    else:
       countFalse += 1
  return countTrue, countFalse


# 2. Create a function that validates whether a number n is within the bounds of lower and upper. 
# Return false if n is not an integer.
# Examples
# intWithinBounds(3, 1, 9) ➞ true
# intWithinBounds(6, 1, 6) ➞ false
# intWithinBounds(4.5, 3, 8) ➞ false
# Notes
# The term "within bounds" means a number is considered equal or greater than a lower bound and lesser
# (but not equal) to an upper bound, (see example #2).
# Bounds will be always given as integers.
def is_within_bounds(v1, v2, v3):
    if not isinstance(v1, int):
        return False
    if v1<= v2 or v1 >= v3:
        return False
    return True


# 3. Create a function that takes three values:
# h hours
# m minutes
# s seconds
# Return the value that's the longest duration.
# Examples
# longestTime(1, 59, 3598) ➞ 1
# longestTime(2, 300, 15000) ➞ 300
# longestTime(15, 955, 59400) ➞ 59400
def longest_time(h, m, s):
    hour_to_minute = h*60
    second_to_minute = s//60
    
    if hour_to_minute> m and hour_to_minute>second_to_minute:
     return h
    elif second_to_minute>m and second_to_minute>hour_to_minute:
      return s
    elif m > second_to_minute and m>hour_to_minute:
      return m
    else: 
        return False


    
# 4. Create a function that takes the month and year (as integers) and returns the number of days in that month.
# Examples
# days(2, 2018) ➞ 28
# days(4, 654) ➞ 30
# days(2, 200) ➞ 28
# days(2, 1000) ➞ 28
# Notes
# Don't forget about leap years!
dict= {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}
def year_days(month, year):
  if month==2 and year%4==0:
    return 29
  return dict[month]
  
  # 5. Create a function that takes a string and censors words over four characters with *.
# Examples
# censor("The code is fourty") ➞ "The code is ******"
# censor("Two plus three is five") ➞ "Two plus ***** is five"
# censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
# Notes
# Don't censor words with exactly four characters.
# If all words have four characters or less, return the original string.
# The amount of * is the same as the length of the word.
def censor_words(string):
    words = string.split()
    for i, x in enumerate(words):
      if len(x) > 4:
        words[i]='*' * len(x)  
    return ' '.join(words)


# 6. Given a sentence, create a function that replaces every "a" as an article with "an absolute".
# It should return the same string without any change if it doesn't have any "a".
# Examples
# absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
# absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
# absolute("A man with no haters.") ➞ "An absolute man with no haters."
# Notes
# Watch for uppercase letters as shown in example #3.
def replace_a_with_absolute(sentence):
    words = sentence.split()
    for x in range(len(words)):
        if words[x] == 'a':
            words[x] = 'an absolute'
    return ' '.join(words)


# 7. Return an Array of Subarrays
# Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays 
# (e.g. [[], [], []]), each containing y number of item z.
# x Number of subarrays contained within the main array.
# y Number of items contained within each subarray.
# z Item contained within each subarray.
# Examples
# matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
# matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
# matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
# Notes
# The first two arguments will always be integers.
# The third argument is either a string or an integer.
def matrix(x, y, z):
    result = []
    for i in range(x):
        list = [z] * y
        result.append(list)
    return result


# 8. Given a string of numbers separated by a comma and space, return the product of the numbers.
# Examples
# multiplyNums("2, 3") ➞ 6
# multiplyNums("1, 2, 3, 4") ➞ 24
# multiplyNums("54, 75, 453, 0") ➞ 0
# multiplyNums("10, -2") ➞ -20
# Notes
# Bonus: Try to complete this challenge in one line!
def product_of_numbers(numbers):
    nums = numbers.split(',')
    product = 1
    for num in nums:
        product *= int(num)
    return product


# 9. Create a function that takes a string road and returns the car that's in first place. 
# The road will be made of "=", and cars will be represented by letters in the alphabet.
# Examples
# firstPlace("====b===O===e===U=A==") ➞ "A"
# firstPlace("e==B=Fe") ➞ "e"
# firstPlace("proeNeoOJGnfl") ➞ "l"
def firstPlace(string):
  reversed = string[::-1]
  for i in reversed:
    if i.isalpha():
      return i
  return "No car available"    

# Notes
# Return "No car available" if there is no car on the road and "No road available" if there is no road.
# 10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) 
# and returns the missing number.
# Examples
# missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
# missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
# missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
# Notes
# The array of numbers will be unsorted (not in order).
# Only one number will be missing.
def missingNumber(list):
    return sum(range(1, 11)) - sum(list)
