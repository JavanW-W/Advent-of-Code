#PART I
#Count the total number of times each monkey inspects items over 20 rounds
#In the example, the two most active monkeys inspected items 101 and 105 times
#The level of monkey business in this situation can be found by multiplying these together: 10605

#Figure out which monkeys to chase by counting how many items they inspect over 20 rounds
#What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

#PART II
#Worry levels are no longer divided by three after each item is inspected; 
#Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

import re, math, time
start_time = time.time()

with open('example_input.txt') as f:
    data_txt = f.read()

monkey_list = data_txt.split('\n\n') #give each monkey its own item in the list

#Let's learn how to make a dictionary!

for index, monkey in enumerate(monkey_list):
    monkey_list[index] = monkey.split('\n')
    for line in monkey_list[index]:
        if 'Starting items:' in line:    
            n = re.findall('\d+', line)
            items = [int(x) for x in n]
        if 'Operation:' in line:
            operation = line.replace('Operation: new = ','').strip()
        if 'Test:' in line:
            test = line.replace('Test: divisible by ','%').strip()
        if 'If true:' in line:
            n = re.findall('\d+', line)
            success = int(n[0])
        if 'If false:' in line:
            n = re.findall('\d+', line)
            failure = int(n[0])
    monkey_list[index] = {
            'Monkey': index,
            'Items': items,
            'Operation': operation,
            'Test': test,
            'Success': success,
            'Failure': failure,
            'Inspections': 0
        }

for rounds in range(20):
    for monkey in monkey_list:
        #Inspect items
        for item in monkey['Items'].copy():
            #Monkey inspect item
                monkey['Inspections'] += 1
            #Worry about item
                old = item
                new_item = eval(monkey['Operation'])
            #Uncomment for PART I
            #Monkey get bored
                new_item = math.floor(new_item / 3)
                monkey['Items'][0] = new_item

            #Uncomment for PART II
            # #Deal with my worry
            # But HOW?
            
            #Monkey test / Monkey throw
                if eval(str(new_item)+monkey['Test']) == 0:
                    x = monkey['Items'].pop(0)
                    monkey_list[monkey['Success']]['Items'].append(x)
                else:
                    x = monkey['Items'].pop(0)
                    monkey_list[monkey['Failure']]['Items'].append(x)

inspections = []
for monkey in monkey_list:
    print(monkey['Monkey'],':',monkey['Inspections'])
    inspections.append(monkey['Inspections'])
inspections.sort(reverse=True)

monkey_business = (inspections[0]*inspections[1])

print('Level of Monkey Business:',monkey_business)
print('This program took', time.time() - start_time, 's to run')