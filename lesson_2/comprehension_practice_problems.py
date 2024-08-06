# 1

# Consider the following nested dictionary:

# munsters = { 'Herman':  {'age': 32,  'gender': 'male'}, 'Lily':    {'age':
#     30,  'gender': 'female'}, 'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'}, 'Marilyn': {'age': 23,
#     'gender': 'female'}, }

# # Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

# # The result should be 444.

# result = 0

# for name, (age, gender) in munsters.items(): if munsters[name][gender] ==
#     'male': result += munsters[name][age]

# print(result)

# # launch school answer - easier to read as I unpacked too much in my answer.
# total_male_age = 0 for member in munsters.values(): if member['gender'] ==
# 'male': total_male_age += member['age']

# print(total_male_age)         # 444


# result = sum([munsters[name][age] for name, (age, gender) in munsters.items()
#                                   if munsters[name][gender] == 'male'])

# print(result)

# # launch school answer - easier to read as I unpacked too much in my answer.
# all_male_ages = [member['age'] for member in munsters.values() if
#                                member['gender'] == 'male']

# print(sum(all_male_ages))     # 444



# 2

# Given the following data structure, return a new list with the same
# structure, but with the values in each sublist ordered in ascending order.
# Use a comprehension if you can. (Try using a for loop first.)

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # Expected result

# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# The string values should be sorted as strings, while the numeric values
# should be sorted as numbers.

# sorted_sublists = []

# for sublist in lst: sorted_sublists.append(sorted(sublist))

# print(sorted_sublists)

# sorted_sublists = [sorted(sublist) for sublist in lst]

# print(sorted_sublists)



# 3

# Given the following data structure, return a new list with the same
# structure, but with the values in each sublist ordered in ascending order as
# strings (that is, the numbers should be treated as strings). Use a
# comprehension if you can. (Try using a for loop first.)

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # Expected result

# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

# new_lst = []

# for sublist in lst: new_lst.append(sorted(sublist, key=str)) print(new_lst)

# new_lst = [sorted(sublist, key=str) for sublist in lst] print(new_lst)



# 4

# Given the following data structure, write some code that defines a dictionary
# where the key is the first item in each sublist, and the value is the second.

# lst = [ ['a', 1], ['b', 'two'], ['sea', {'c': 3}], ['D', ['a', 'b', 'c']] ]

# # Expected result

# # Pretty printed for clarity
# # {
# #     'a': 1,
# #     'b': 'two',
# #     'sea': {c: 3},
# #     'D': ['a', 'b', 'c']
# # }

# dictionary = {key: value for key, value in lst}

# print(dictionary)



# 5

# Given the following data structure, sort the list so that the sub-lists are
# ordered based on the sum of the odd numbers that they contain. You shouldn't
# mutate the original list.

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# # Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:
# # Expected result

# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

# # Try to use a comprehension in your solution.

# def sum_odd_numbers(sublist): odd_numbers = [number for number in sublist if
#     number % 2 != 0] return sum(odd_numbers)

# sorted_list = sorted(lst, key=sum_odd_numbers)

# print(sorted_list)



# 6

# Given the following data structure, return a new list identical in structure
# to the original but, with each number incremented by 1. Do not modify the
# original data structure. Use a comprehension.

# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# # Expected result

# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# def add_one(dictionary): return {key: value + 1 for key, value in
#     dictionary.items()}

# lst_plus_one = [add_one(dictionary) for dictionary in lst]

# print(lst, lst_plus_one, sep='\n')



# 7

# Given the following data structure return a new list identical in structure
# to the original, but containing only the numbers that are multiples of 3.

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# # The returned list should look like this:
# # Expected result

# [[], [3, 12], [9], [15, 18]]

# # Try to use a comprehension for this. However, we recommend first trying it without comprehensions.

# # new_list = []

# # for sublist in lst:
# #     multiples_of_3 = []
# #     for num in sublist:
# #         if num % 3 == 0:
# #             multiples_of_3.append(num)
# #     new_list.append(multiples_of_3)

# # print(new_list)

# def multiples_of_3(lst): return [num for num in lst if num % 3 == 0]

# new_list = [multiples_of_3(sublist) for sublist in lst]

# print(new_list)

# # launch school's nested comprehension (not readable, not worth doing)
# new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
# print(new_list)



# 8

# Given the following data structure, write some code to return a list that
# contains the colors of the fruits and the sizes of the vegetables. The sizes
# should be uppercase, and the colors should be capitalized.

# dict1 = { 'grape': { 'type': 'fruit', 'colors': ['red', 'green'], 'size':
#     'small', }, 'carrot': { 'type': 'vegetable', 'colors': ['orange'],
#         'size': 'medium', }, 'apricot': { 'type': 'fruit', 'colors':
#         ['orange'], 'size': 'medium', }, 'marrow': { 'type': 'vegetable',
#         'colors': ['green'], 'size': 'large', }, }

# def capitalize_or_uppercase(value): if value['type'] == 'fruit': return
#     [color.capitalize() for color in value['colors']]

#     if value['type'] == 'vegetable': return value['size'].upper()

# new_list = [capitalize_or_uppercase(value) for value in dict1.values()]

# print(new_list)

# The return value should look like this: Expected result

# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# new_list = []

# for name, values in dict1.items(): for key, value in values.items(): if
#     values[key] == 'fruit': capitalized = [] for color in values['colors']:
#         capitalized.append(color.capitalize()) new_list.append(capitalized)
#             if values[key] == 'vegetable':
#             new_list.append(values['size'].upper())

# print(new_list) print(new_list == [["Red", "Green"], "MEDIUM", ["Orange"],
# "LARGE"]) # True



# 9

# This problem may prove challenging. Try it, but don't stress about it. If you
# don't solve it in 20 minutes, you can look at the answer.

# Given the following data structure, write some code to return a list that
# contains only the dictionaries where all the numbers are even.

# lst = [ {'a': [1, 2, 3]}, {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]}, {'e': [8],
#     'f': [6, 10]}, ]

# Expected result

# [{e: [8], f: [6, 10]}]

# def is_even(dictionary): for list_numbers in dictionary.values(): even_or_odd
#     = all(num % 2 == 0 for num in list_numbers) if not even_or_odd: return
#         False

#     return True

# new_list = [dictionary for dictionary in lst if is_even(dictionary)]

# print(new_list) print(new_list == [{'e': [8], 'f': [6, 10]}]) # True

# new_list = [] for dictionary in lst: is_even = True for key, list_numbers in
# dictionary.items(): if is_even: for num in list_numbers: if num % 2 != 0:
#     is_even = False break if is_even: new_list.append(dictionary)

# print(new_list) print(new_list == [{'e': [8], 'f': [6, 10]}]) # True



# 10

# A UUID (Universally Unique Identifier) is a type of identifier often used to
# uniquely identify items, even when some of those items were created on a
# different server or by a different application. That is, without any
# synchronization, two or more computer systems can create new items and label
# them with a UUID with no significant risk of stepping on each other's toes.
# It accomplishes this feat through massive randomization. The number of
# possible UUID values is approximately 3.4 X 10E38, which is a huge number.
# The chance of a conflict, a "collision", is vanishingly small with such a
# large number of possible values.

# Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the
# letters a-f) represented as a string. The value is typically broken into 5
# sections in an 8-4-4-4-12 pattern, e.g.,
# 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

# Note that our description of UUIDs is a simplified description of how UUIDs
# are formed. There are several UUID versions, each with some non-random
# characteristics in some of the bits. These different versions can play a part
# in certain applications.

# Write a function that takes no arguments and returns a string that contains a
# UUID.

# import random
# HEXIDECIMAL_CHARACTERS = "0123456789abcdef"

# def create_uuid():
#     uuid = ""
#     sections = (8, 13, 18, 23)

#     while len(uuid) < 32:
#         if len(uuid) in sections:
#             uuid += "-"
#         uuid += random.choice(HEXIDECIMAL_CHARACTERS)

#     return uuid

# print(create_uuid())



# 11

# The following dictionary has list values that contains strings. Write some
# code to create a list of every vowel (a, e, i, o, u) that appears in the
# contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

# VOWELS = "aeiou"

# def list_of_vowels(dictionary):
#     vowels = []

#     for lsts in dictionary.values():
#         for lst in lsts:
#             for letter in lst:
#                 if letter in VOWELS:
#                     vowels.append(letter)

#     return vowels

# print(list_of_vowels(dict1))
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Start by trying to write this using nested loops.

# Extra Challenge: Once your nested loop code works, try to refactor the code
# so it uses a single list comprehension. (You can print the resulting list
# outside of the comprehension.)

# VOWELS = "aeiou"

# def list_of_vowels(dictionary):
#     vowels = [letter for lsts in dictionary.values()
#                      for lst in lsts
#                      for letter in lst if letter in VOWELS]

#     return vowels

# print(list_of_vowels(dict1))
