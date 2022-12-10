#PART I
#Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
#What is the sum of these six signal strengths?

#noop takes 1 cycle to complete and does nothing
#addx takes 2 cycles to complete (nothing happens during first cycle)
#signal strength is x * current cycle

#example answer is 13140

with open('puzzle_input.txt') as f:
    data_txt = f.readlines()

instructions = []
for x in data_txt:
    if x.split()[0] == 'noop':
        instructions.append('noop')
    else:
        instructions.append(int(x.split()[-1]))

x = [1]
for cycle in instructions:
    if cycle == 'noop':
        x.append(x[-1])
    else:
        x.append(x[-1])
        x.append(x[-1]+cycle)

def calc_signal_strength(x: list, cycle: int):
    signal_strength = x[cycle-1] * cycle
    return signal_strength 

sum_signal_strengths = 0
for i in range(20,260,40):
    sum_signal_strengths += calc_signal_strength(x, i)       

print(sum_signal_strengths)

#PART II
#x is the horizontal position of the center pixel of a 3 pixel-wide a sprite. 
#there is no such thing as "vertical position"
#if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn

#You count the pixels on the CRT: 40 wide and 6 high. 
#This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. 
#The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.
#the CRT draws a single pixel during each cycle
#i.e.:
#Sprite starting position: x = 1 (center in second position)
#Start cycle 1: begin executing addx 15
#During cycle 1: CRT draws pixel in position 0

#Render the image given by your program. What eight capital letters appear on your CRT?

crt = '#'
for cycle in range(1,241):
    if abs(x[cycle]-cycle%40) <= 1 :
        crt += '#'
    else:
        crt += '.'

for i in range(0,len(crt)-1,40):
    print(crt[i:i+40])



