from block_letters import *

name_to_print = [ M, I, S, S, I, S, S, I, P, P, P, I]

# Assume that all letters have the same number of lines, 
# so we can just check the first letter to get the number of lines to print
number_of_lines = len(name_to_print[0])

# For every line to print, go through the corresponding line of each letter
for line in range(number_of_lines):
    for letter in range(len(name_to_print)):
        print(name_to_print[letter][line], end ="  ")
    print()