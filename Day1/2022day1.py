#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
#The input is a list of all of the calories each elf is carrying 
#Food items are separated by lines
#Elf inventories are separated by blank lines
import numpy as np 

# PART I
with open('puzzle_input.txt') as f:
    data_txt = f.read() #read the txt file as a string
cal_list = data_txt.split('\n\n') #break the string up into a list of each Elf's calories

total_cals = [] #initialize the list of total calories for each Elf
for elves in cal_list: 
    elf_list = elves.split('\n') #break the string of food items into its own list
    for food_item in range(0, len(elf_list)): 
        elf_list[food_item] = int(elf_list[food_item]) #convert each string (calorie value) to an integer
    total_cals.append(sum(elf_list)) #total the calories for that Elf

print('There are',len(cal_list),'Elves')
if total_cals.count(max(total_cals)) == 1:
    print('Only 1 Elf is carrying the most calories!')
    print('The Elf carrying the most calories is Elf #',total_cals.index(max(total_cals))+1)
    print('That Elf is carrying',max(total_cals),'calories')
else:
    values = np.array(total_cals)
    which_elves = np.where(values == max(total_cals))[0]
    print (total_cals.count(max(total_cals)),'Elves are carrying the most calories')
    print('The Elves carrying the most calories are:')
    for elf in range(0,len(which_elves)):
        print('#',which_elves[elf]+1)
    print('Those Elves are carrying',max(total_cals),'calories')

# PART II
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
total_cals.sort(reverse=True)
top_three = []
for i in range(0,3):
    top_three.append(total_cals[i])
top_three_total = sum(top_three)
print('The three Elves carrying the most calories are carrying',top_three_total,'calories total')