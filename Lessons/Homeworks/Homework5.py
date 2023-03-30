# # # """1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).
# # # Check the examples for a better understanding.
# # # Examples
# # # [1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
# # # [6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
# # # [20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]"""

# # list=[20, 15, 26, 8, 4]
# # rotated_list = list[-1:] + list[:-1]
# # print(rotated_list)

# # # """2. Create a function that inverts the rgb values of a given tuple.
# # # Examples
# # # color_invert((255, 255, 255)) ➞ (0, 0, 0)
# # # # (255, 255, 255) is the color white.
# # # # The opposite is (0, 0, 0), which is black.
# # # color_invert((0, 0, 0)) ➞ (255, 255, 255)
# # # color_invert((165, 170, 221)) ➞ (90, 85, 34)
# # # Notes
# # # Must return a tuple.
# # # 255 is the max value of a single color channel."""

# a,b,c = (0, 0, 0)
# rgb_const= 255
# inverted_tuple= abs(255-a), abs(255-b), abs(c-255)
# print(inverted_tuple)


# # 3. Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
# # Examples
# # find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
# # find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
# # find_bob(["Jimmy", "Layla", "James"]) ➞ -1
# # Notes
# # Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").

# # my_list = ["Jimmy", "Layla", "James"]
# # name = "Bob"
# # if name in my_list:
# #     index = my_list.index(name)
# # else:
# #     index = -1
# # print(index)



# # EXTRA Knowledge
# # 4. Given a list of numbers, write a function that returns a list that...
# # Has all duplicate elements removed.
# # Is sorted from least to greatest value.
# # Examples
# # unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# # unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
# # unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
# # EXTRA Knowledge
# # numbers= [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
# # unique_numbers = set(numbers)
# # sorted_numbers = sorted(unique_numbers)
# # print(sorted_numbers)

# # 5. Given two strings, create a function that returns the total number of unique characters from the combined string.
# # Examples
# # count_unique("apple", "play") ➞ 5
# # # "appleplay" has 5 unique characters:
# # # "a", "e", "l", "p", "y"
# # "sore", "zebra" ➞ 7
# # "a", "soup" ➞ 5

# # a, b = "apple", "play"
# # new_string= a+b
# # chars = len(set(new_string))
# # print(chars)

# # 6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
# # Examples
# # {
# #   "Student 1" : "Ani",
# #   "Student 2" : "J",
# #   "Student 3" : "John"
# # } ➞ ["Becky", "John", "Steve"]

# # students = {"Student 1": "Ani", "Student 2": "Beck", "Student 3": "Luis"}
# # sorted_names = sorted(students.values())
# # print(sorted_names)



# # 7. Create a function that returns a list of strings sorted by length in ascending order.
# # Examples
# # sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
# # sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
# # sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
# # sort_by_length([]) ➞ []
# # Notes
# # Strings will have unique lengths, so don't worry about comparing two strings with identical length.
# # Return an empty array if the input array is empty
# # strings = ["may", "april", "september", "august"]
# # sorted_strings = sorted(strings, key= len )
# # print(sorted_strings)



# # 8. Write a function that converts a dictionary into a list of keys-values tuples.
# # Examples
# # dict_to_list({
# #   "D": 1,
# #   "B": 2,
# #   "C": 3
# # }) ➞ [("B", 2), ("C", 3), ("D", 1)]
# # dict_to_list({
# #   "likes": 2,
# #   "dislikes": 3,
# #   "followers": 10
# # }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

# dictionary = {'Likes': '2', 'Dislike': '3','Followers': '10'}
# tuples_list = (dictionary.items())
# print(tuples_list)



# # 9. Print the value of key ‘history’ from the below dict
# # sampleDict = 
# #     "class": {
# #         "student": {
# #             "name": "Mike",
# #             "marks": {
# #                 "physics": 70,
# #                 "history": 80
# #             }
# #         }
# #     }
# Dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(Dict['class']['student']['marks']['history'])


# # 10. Rename key of a dictionary
# # Write a program to rename a key city to a location in the following dictionary.
# # Given:
# # sample_dict = {
# #   "name": "Kelly",
# #   "age":25,
# #   "salary": 8000,
# #   "city": "New york"
# # }
# # Expected output:
# # {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

# dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# dict["location"] = dict.pop("city")

# print(dict)