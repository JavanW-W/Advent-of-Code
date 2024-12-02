#In how many assignment pairs does one range fully contain the other?

#PART I
with open('puzzle_input.txt') as f:
    data_txt = f.read()
lines = data_txt.split('\n')
pairs = [i.split(',') for i in lines]

contained = 0
overlapped = 0
for pair in pairs:
    for elf in pair: 
        lo_hi = [int(i) for i in elf.split('-')]
        pair[pair.index(elf)] = set(range(lo_hi[0], lo_hi[1]+1))
    if pair[0].isdisjoint(pair[1]):
        pass
    else:
        overlapped += 1
        if pair[0] <= pair[1] or pair[1] <= pair[0]:
            contained += 1
print(contained)
print(overlapped)