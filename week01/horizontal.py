from block_letters import *

name_to_print = [ E, L, L, O, O]

number_of_lines = len(name_to_print[0])

# For every line to print, go through the corresponding line of each letter

for line in range(number_of_lines):
    for letter in range(len(name_to_print)):
        print(name_to_print[letter][line], end ="  ")
    print()

