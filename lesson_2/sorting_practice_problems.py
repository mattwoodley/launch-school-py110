# 1

# Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# Expected result

[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# print("Sorted Ascending:", sorted(lst))
# Sorted Ascending: [-16, -6, 7, 8, 9, 10, 11, 50]

# print("Sorted Descending:", sorted(lst, reverse=True))
# Sorted Descending: [50, 11, 10, 9, 8, 7, -6, -16]

# print("Original:", lst)
# Original: [10, 9, -6, 11, 7, -16, 50, 8]

# 2

# Repeat the previous exercise but, this time, perform the sort by mutating the original list.

lst.sort()
# print("Original:", lst) # Original: [-16, -6, 7, 8, 9, 10, 11, 50]

lst.sort(reverse=True)
# print("Original:", lst) # Original: [50, 11, 10, 9, 8, 7, -6, -16]



# 3

# Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst.sort(key=str)
# print(lst) # [-16, -6, 10, 11, 50, 7, 8, 9]

lst.sort(key=str, reverse=True)
# print(lst) # [9, 8, 7, 50, 11, 10, -6, -16]



# 4

# How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]


def get_published_year(books):
    return int(books['published'])

new_list = sorted(books, key=get_published_year)
