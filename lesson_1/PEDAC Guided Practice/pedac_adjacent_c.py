def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(string):
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    string = ''.join(string.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''
    for letter in string:
        if letter in CONSONANTS:
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)

            adjacent_consonants = ''

    return max_consonant_count


my_list = ['a a', 'dd daa', 'abbbabbaba', 'caccacccacccca', 'acacacacacac']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['aa', 'dddaa', 'ccaa', 'baa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']