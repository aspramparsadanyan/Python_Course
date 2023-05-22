# 1. # """You need to create two functions to substitute str() and int().
# A function called int_to_str() that converts integers into strings and a function called str_to_int()
# that converts strings into integers."""

# def convert(value):
#     if isinstance(value, int):
#         return str(value)
#     elif isinstance(value, str):
#             return int(value)
#     else:
#        return "Error"

# 2.Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. 
# Is it gone?!

# Given a dictionary of the stolen items and a string in lowercase representing 
# the name of the pet (e.g. "rambo"), return:

# "Rambo is gone..." if the name is on the list.
# "Rambo is here!" if the name is not on the list.
# Note that the first letter of the name in the return statement is capitalized.

# def pets_list(dict, name):
#     if not dict:
#         return name.capitalize() + " is here!"
#     elif name in dict:
#         return name.capitalize() + " is gone..."
#     else:
#         return name.capitalize() + " is here!"
# print(pets_list(dict, "timmy"))
        

# 3. For each challenge of this series you do not need to submit a function. Instead, 
# you need to submit a template string that can formatted in order to get a certain outcome.

# Write a template string according to the following example. 
# Notice that the template will be formatted twice:

# def area_of_country(name, area):
#     total_area = 148940000 
#     proportion = (area / total_area) * 100
#     proportion_rounded = round(proportion,2 )
#     return name + " is " + str(proportion_rounded) + "% of the total world's landmass"
# print(area_of_country("Russia", 17098242))
# "My best friend is Joe."

#4 template = "My best friend is {{}} "
# a="John"
# b="Joe"
# print('My best friend is {{1}}'.format(1).format(a, b))


# String hard

# 1.
# def arithmetic_operation(n):
#     n = n.split()
#     n[0], n[2] = int(n[0]), int(n[2])

#     if n[1] == "+":
#         result = n[0] + n[2]
#     elif n[1] == "-":
#         result = n[0] - n[2]
#     elif n[1] == "*":
#         result = n[0] * n[2]
#     elif n[1] == "//":
#         if n[2] == 0:
#             result = -1
#         else:
#             result = n[0] // n[2]
#     return result

# print(arithmetic_operation("12 + 12"))

# 2.
# def disarium(n):
#     n= str(n)
#     summery=0
#     for i in range(len(n)):
#         summery += int(n[i])**(i+1)
#     if int(n)== summery:
#      return True
#     else:
#         return False
# print(disarium(75))

# 3
# def scores(s):
#     key= {"#":5,"O":3,"X":1, "!":-1,"!!":-3,"!!!":-5,}
#     output=0
#     for x in range(len(s)):
#         for symbol in s[x]:
#             if symbol in key.keys():
#                 output += key[symbol]
#     return output
# print(scores([
#   ["#", "!"],
#   ["!!", "X"]
# ]))

#4
# def convert_to_hax(txt):
#     list=[]
#     for i in txt:
#         list.append(i.encode("utf-8").hex())
#     return " ".join(list)
# print(convert_to_hax("hello world"))


#5
# def uncensor(txt,vowels):
#     for i in vowels:
#         txt =  txt.replace("*",i,1)
#     return txt
# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))

#6
# def tidy_link(url, name, hover_text = None):
#     if (hover_text):
#         new_link= f"([{name}]([{url}* {hover_text}]"
#     else:
#         new_link= f"([{name}]([{url}"
#     return new_link
# print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))

#7
# def remove_letters(lst, word):
#     for letter in word:
#         if letter in lst:
#             lst.remove(letter)
#     return lst
# result = remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string")
# print(result) 

#8
# def pluralize(words):
#     word_count = {}
#     plural_words = set()

#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     for word, count in word_count.items():
#         if count > 1:
#             plural_word = word + 's'
#             plural_words.add(plural_word)
#         else:
#             plural_words.add(word)

#     return plural_words

# print(pluralize(["cow", "pig", "cow", "cow"]))

#9
# def censor_string(txt, lst, char):
#     words = txt.split()
#     censored_words = []

#     for word in words:
#         if word in lst:
#             censored_words.append(char * len(word))
#         else:
#             censored_words.append(word)

#     censored_txt = ' '.join(censored_words)
#     return censored_txt
# print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))

#10
# def parse_code(encoded_string):
#     keys = ["first_name", "last_name", "id"]
#     values = encoded_string.split("000")
#     result = {}
#     for i in range(len(keys)):
#         result[keys[i]] = values[i]
#     return result
# print(parse_code("John000Doe000123"))

#11
# def loves_me(petals):
#     phrases = ["Loves me", "Loves me not"]
#     result = []
#     for i in range(petals):
#         phrase = phrases[i % 2]
#         result.append(phrase)
#     result[-1] = result[-1].upper()
#     return ", ".join(result)
# print(loves_me(3))


# Hard array

# 1.
# def interview(times, total_time):
#     max_times = [5, 5, 10, 10, 15, 15, 20, 20]
#     max_total_time = sum(max_times) + 20

#     if times == max_times and total_time <= max_total_time:
#         return "qualified"
#     else:
#         return "disqualified"
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))

# 2.

# def rep_set(n):
#     if n == 0:
#         return []
#     else:
#         prev_set = rep_set(n - 1)
#         return prev_set + [prev_set]
# print(rep_set(0))


# 3
# def arithmetic_operation(s):
#     num1, operator, num2 = s.split()
#     num1 = int(num1)
#     num2 = int(num2)


#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "//":
#         if num2 == 0:
#             return -1
#         else:
#             return num1 // num2

# print(arithmetic_operation("12 + 12"))

# 4
# def encode_morse(s):
#     char_to_dots = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#         '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#         ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#         '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }
    
#     encoded = ''
#     for char in s:
#         if char.upper() in char_to_dots:
#             encoded += char_to_dots[char.upper()] + ' '
    
#     return encoded.strip()
