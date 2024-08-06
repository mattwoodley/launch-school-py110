"""
Based on all of your notes and analysis so far, implement a working solution in Python. Your solution should pass all of the test cases provided.
"""

def calculate_leftover_blocks(total_blocks):
    available_blocks = total_blocks
    leftover_blocks = 0
    layer = 1

    while available_blocks > 0:
        if available_blocks - (layer * layer) >= 0:
            available_blocks -= (layer * layer)
            layer += 1
        else:
            leftover_blocks = available_blocks
            break
    return leftover_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True


"""
We're now ready to start thinking about our implementation. Once you have a solid algorithm, it's always tempting to start coding straight away. Our algorithm at this point is still fairly abstract, however, and while we could perhaps translate it to code without too much trouble, it might be useful to first make a few implementation notes.

There are a few different approaches we could take here. We could edit our existing algorithm to include implementation detail, we could write a separate implementation-specific version of the algorithm, or we could make some separate notes about how to approach the implementation.

The exact approach you take will depend on a combination of personal preference and also the problem at hand. In this case, the algorithm is clear and structured programmatically, even though it has no specific implementation detail:

    Step 1 reads as variable initialization.
    Steps 2 through 4 read as actions executed within a loop.
    Step 4 reads as a conditional statement.

Perhaps we don't need to re-write the entire algorithm at an implementation level, but there are some aspects of the algorithm worth exploring and making notes about. For example, how do we want to implement the looping structure?

If we look at our algorithm, there's a clue there. Let's think about the condition being checked on step 4:

    Determine whether the "number of blocks remaining" is greater than or equal to the "number of blocks required in this layer".

When this condition evaluates to True we perform another iteration. Does this suggest that it may be a suitable situation to use a while loop? Let's make a note about it that we can refer to when implementing our solution:
Implementation Notes

- Use a `while` loop?
    - For the condition, check whether "number of blocks
      remaining" is greater than or equal to the "number of
      blocks required".

Something else we might want to make a note about is the calculation for determining the number of blocks required for the next layer. There are two steps here that we can consolidate into a single calculation:

    The number for the next layer is the current layer plus 1.
    The number of blocks for the next layer is that layer's number multiplied by itself. In other words, that layer's number squared. In Python, the ** operator can assist here.

Our implementation notes may now look something like this:
Implementation Notes

- Use a `while` loop?
    - For the condition, check whether "number of blocks
      remaining" is greater than or equal to the "number of
      blocks required".
- Calculating the blocks for the next layer, use `**` operator?
    - For example: `(current_layer + 1)**2`.

Based on our algorithm and our implementation notes, our solution might look something like this:
leftover_blocks.py

def calculate_leftover_blocks(n):
    current_layer = 0
    remaining_blocks = n

    required_blocks = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

Lines 2 and 3 here correspond to Step 1 in our algorithm. Line 5 combines steps 2 and 3. Step 4 encapsulates the remainder of the code, with the while loop combining the conditional check and the iteration and the block for the loop containing the necessary incrementation, decrementation, and the repetition of steps 2 & 3. Finally, line 12 is the else clause from Step 4 for when the condition for our while loop is no longer met.
"""