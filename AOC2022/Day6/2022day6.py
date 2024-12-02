#PART I
#How many characters need to be processed before the first start-of-packet marker is detected?
#Your subroutine needs to identify the first position where the four most recently received characters were all different
#Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker

with open('puzzle_input.txt') as f:
    data_txt = f.read()

start_packet = []
for char in range(len(data_txt)-4):
    if len(set(data_txt[char:char+4])) == 4:
        start_packet.append(char+4)

first_start_packet = start_packet[0]
print('The first start-of-packet marker is at position',first_start_packet)


#PART II
# How many characters need to be processed before the first start-of-message marker is detected?

start_message = []
for char in range(len(data_txt)-14):
    if len(set(data_txt[char:char+14])) == 14:
        start_message.append(char+14)

first_start_message = start_message[0]
print('The first start-of-message marker is at position',first_start_message)
