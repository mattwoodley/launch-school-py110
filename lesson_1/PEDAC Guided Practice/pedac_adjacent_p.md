# Sort by Most Adjacent Consonants

## Understand the Problem

Given a list of strings, return a new list where the strings are sorted based
on the highest number of adjacent consonants a string contains. If two strings
contain the same highest number of adjacent consonants, they should retain
their original order in relation to each other. Consonants are considered
adjacent if they are next to each other in the same word or if there is a space
between two consonants in adjacent words.

Tasks

You are provided with the problem description above.
Your tasks for this step are:

    Make notes of your mental model for the problem, including:
        - inputs and outputs.
        - explicit and implicit rules.
    Write a list of clarifying questions for anything that isn't clear.

input: list of strings

output: a new list where the strings are sorted based on the highest number
    of adjacent consonants a string contains

rules:
    Explicit:
        - If two strings contain the same highest number of adjacent
          consonants, they should retain their original order
          in relation to each other.
        - Consonants are considered adjacent if:
            - They are next to each other in the same word
            - There is a space between two consonants in adjacent words
    Implicit:
        - Strings may contain single or multiple words
        *update after doing examples/test cases*
        - Strings may not be empty
        - Strings may have no adjacent consonants
        - Strings should be sorted in descending order
        - Case is not relevant
        - Single consonants in a string do not affect sort order in comparison
          to strings with no consonants, only adjacent consonants do

Questions:
    - Always given a list of strings?
    - How should I handle punctuation characters?
    - Do I include whitespace within strings?
    - What is considered a consonant and what isn't?
    - Are strings in multiple languages?

Launch School Questions:
    - Do strings always contain multiple words?
        - Can strings contain a single word?
        - Can strings be empty?
    - Is it possible for a string to contain no adjacent consonants?
    - What is meant by "a space between two consonants in adjacent
    words"?
    - Should the strings be sorted in ascending or descending order?
    - Is case important?

## Examples/Test Cases

    ```python
    my_list = ['aa', 'baa', 'ccaa', 'dddaa']
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
    ```

- The tests show that we should sort in descending order.
- Test 1 shows that strings not containing consonants are equal to strings that
  contain 0 adjacent consonants, even if they do contain some consonants.
- The tests show that we do not include spaces as part of the adjacent count
- Test 2 "can can" shows that consonants are considered to be adjacent if they
  are at the end of one word and the beginning of the next.
- How do we handle punctuation characters other than whitespaces?
- How do we handle empty strings?

## Data Structures

Could use a dictionary to store the string as a key and the adjacent consonants
as the value

    ```python
    {
        'aa': 0,
        'baa': 0,
        'ccaa': 2,
        'dddaa': 3,
    }
    ```

## Algorithm

1. Start with:
    - The "number of adjacent consonants" is equal to 0.
    - The "string and adjacent consonants" is an empty dictionary.
    - Store "valid consonants" in a frozen set.

2. Check the list of strings for adjacent consonants:
    1. Take the first string
        2. Check the characters for if they're a "valid consonant" until no
        characters remain.
            - If they are not a consonant, move to the next character
            - If they are a consonant, check if the next character is also a
            consonant.
                - If they are both consonants, increment "number of adjacent
                consonants" by 1
                - If not then skip to the next character
        3. Once all characters are checked, add the "string and adjacent
          consonants" with the string as the key and the "number of adjacent
          consonants" as the value.
        4. Reset the "number of adjacent consonants" to 0
    - Take the next string and go to step 1 until all strings are checked.

3. Create a result list with the value of the "string and adjacent consonants"
   sorted by their values. If any values are equal to one another then retain
   the order that they were inserted.

4. Return the result

**Launch School's Answer**

High Level Algorithm

1. For each string in the input list, determine the highest number
   of adjacent consonants within that string.
2. Sort the input list based on the calculated highest number of
   consonants from step 1.
3. Return the sorted list.

We'll need much more detail than this before we move to our implementation step, but this high-level outline can help us determine where we should focus our efforts. For example, returning the sorted list is a trivial step and not something we need to really think about. If we've solved a number of sorting type problems before, we probably know we can use the list.sort method here. However, we don't want to be thinking too far ahead to the implementation at this stage. Nevertheless, familiarity with certain types of problems can help when abstracting out certain parts of the problem at the algorithm stage.

The first step currently seems to be the one that we need to think about most, so let's dive in a little further there.

    For each string in the input list, determine the highest number of adjacent consonants within that string

This seems to suggest a repeatable action that needs to be performed on each string in the list. We may already be thinking about extracting this logic to a helper function. Again, we don't want to think too far ahead to the implementation, but certainly in terms of algorithm it might make sense to define a specific algorithm just for this step, whether that ends up being a helper function or not.

When defining this type of "sub-algorithm" as part of a larger algorithm, it's important to be clear on the requirements for the specific step. Essentially, we want to treat it as a separate problem. Let's do that now:

    Given a string, return a count of the highest number of adjacent consonants anywhere in that string.

We could also define input and output for our sub-problem:
Count Consonants: Inputs and Outputs

Input: a string
Output: an integer representing a count of the highest number of
        adjacent consonants in the string

The rules and general mental model have already been defined as part of the overall problem. However, we might want to create some test cases.
Count Consonants: Test Cases

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4

Thinking about this sub-problem, what we essentially want to do is go through the string letter by letter. We only need to count consonants, so if the letter is vowel we can continue to the next letter. If the letter is a consonant, we can store it in a temporary string. If the next letter is also a consonant, we can also add that to the temporary string, and so on. When we hit another vowel we can determine the length of the temporary string and update a maximum count.

There are two other things we need to think about based on our initial analysis:

    We need to manipulate the input string to remove any spaces.
    We don't want to update the count if the temporary string contains only one consonant.

Our algorithm might look something like this:
Count Consonants: Algorithm

- Remove the spaces from the "input string".
- Initialize a "maximum consonants count" to zero.
- Initialize an "adjacent consonants string" to an empty string.
- For each "letter" in the "input string":
    - If the "letter" is a consonant:
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".

Notice once again how careful we are about identifying the things we are discussing. In particular, we're no longer thinking in terms of a temporary string, but an "adjacent consonants string" instead.

At this stage, we're probably ready to implement the solution to our "sub-problem". We can always return to the algorithm step if necessary if we need to add more detail to the overall algorithm.

## Code

