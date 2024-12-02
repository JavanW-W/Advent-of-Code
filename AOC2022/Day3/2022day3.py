#Find the item type that appears in both compartments of each rucksack. 
#What is the sum of the priorities of those item types?
import re

#PART I
#Lowercase item types a through z have priorities 1 through 26
#Uppercase item types A through Z have priorities 27 through 52

with open('puzzle_input.txt') as f:
    data_txt = f.read() 
inventory = data_txt.split('\n') #break the string up into a list of each Elf's rucksack contents

priority_sum = 0
for rucksack in inventory:
    comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for item in comp1:
        if re.search(item, comp2):
            duplicate = re.findall(item, comp2)
            priority = ord(duplicate[0])
            if priority >= 97:
                priority -= 96
            else:
                priority -= 38
            priority_sum += priority
            break
        else:
            pass
print("The sum of the priorities of the misplaced item types is",priority_sum)

#PART II
#Find the item type that corresponds to the badges of each three-Elf group. 
#What is the sum of the priorities of those item types?
inv_div = []
for rucksack in range(0, len(inventory), 3):
    inv_div.append(inventory[rucksack:rucksack+3])

badge_priority_sum = 0
for group in inv_div:
    for item in group[0]:
        if re.search(item, group[1]):
            if re.search(item, group[2]):
                badge = re.findall(item, group[2])
                badge_priority = ord(badge[0])
                if badge_priority >= 97:
                    badge_priority -= 96
                else:
                    badge_priority -= 38
                badge_priority_sum += badge_priority
                break
            else:
                pass
        else:
            pass
print("The sum of the priorities of the badge item types is",badge_priority_sum)

