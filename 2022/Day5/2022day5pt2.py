#PART II
#JK IT'S THE CRATEMOVER9001
import re

with open('puzzle_input.txt') as f:
    move_crates = f.readlines()

def scale_index(i):
    """ This function scales from a line index to the stack of interest by accounting for whitespace"""
    return int((i+3)/4)

total_stacks = 0
stacks, crates, instructions = [], [], []
for line in move_crates:
    if "[" in line:
        crates.append(re.findall('[A-Z]',line))
        stacks.append([scale_index(match.start()) for match in re.finditer('[A-Z]',line)])
    elif "move" in line:
        instructions.append([int(y) for y in [x.strip() for x in line.split(" ")[1::2]]])
        #this gets rid of all of the extraneous white space and words in the instructions
    elif line != '\n':
        total_stacks = int(line.strip()[-1])

total_crates = 0
for stack in stacks:
    total_crates += len(stack)

new_stacks = []
for i in range(0,total_stacks):
    new_stacks.append([])

for row in range(len(crates),0,-1):
    i = 0 
    while i < len(crates[row-1]):
        new_stacks[stacks[row-1][i]-1].append(crates[row-1][i])
        i += 1

for step in instructions:
    i = 0
    j = 0
    while i < step[0]:
        new_stacks[step[2]-1].append(new_stacks[step[1]-1][-step[0]+i])
        i += 1
    while j < step[0]:
        new_stacks[step[1]-1].pop(-1)
        j += 1
    total_crates = 0
    for stack in new_stacks:
        total_crates += len(stack)

# step[0] #this is how many crates we're moving
# step[1] #this is the stack we're taking from
# step[2] #this is the stack we're moving to

top_crates = ''
for stack in new_stacks:
    top_crates += stack[-1]
print(top_crates)