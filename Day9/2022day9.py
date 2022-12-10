#PART I
#Simulate your complete hypothetical series of motions. 
#How many positions does the tail of the rope visit at least once?

#PART II
#Simulate your complete series of motions on a larger rope with ten knots. 
#How many positions does the tail of the rope visit at least once?


with open('puzzle_input.txt') as f:
    data_txt = f.read()

#do some data parsing to get move_sequence, which is a nested list where each sublist is of the form [direction, distance]
move_sequence = []
for x in data_txt.splitlines():
    move_sequence.append([x.split()[0], int(x.split()[-1])])

knots = 10
knot_coords = []
for knot in range(knots):
    knot_coords.append([0,0])

def isAdjacent(coord_1: list, coord_2: list):
    if abs(coord_1[0] - coord_2[0]) <= 1 and abs(coord_1[1] - coord_2[1]) <= 1:
        return True
    else:
        return False

def move_H(H_coord: list, direction: str):
    if direction == 'L':
        H_coord[0] -= 1
    elif direction == 'R':
        H_coord[0] += 1
    elif direction == 'U':
        H_coord[1] += 1
    elif direction == 'D':
        H_coord[1] -= 1
    return H_coord
    
def move_T(T_coord, H_coord):
    if H_coord[0] - T_coord[0] > 0:
        T_coord[0] += 1
    elif H_coord[0] - T_coord[0] < 0:
        T_coord[0] -= 1
    if H_coord[1] - T_coord[1] > 0:
        T_coord[1] += 1
    elif H_coord[1] - T_coord[1] < 0:
        T_coord[1] -= 1
    return T_coord

# print('H:',H_coord)
# print('T:',T_coord)
# print(isAdjacent(T_coord,H_coord))
all_T_coords = set(knot_coords[-1])
for move in move_sequence:
    step = 0
    direction = move[0]
    distance = move[1]
    while step < distance:
        new_H_coord = move_H(knot_coords[0], direction)
        knot_coords[0] = new_H_coord
        # print('H:',H_coord)
        # print('T:',T_coord)
        # print(isAdjacent(T_coord,H_coord))
        for knot in range(1,knots):
            while not isAdjacent(knot_coords[knot], knot_coords[knot-1]):
                new_T_coord = move_T(knot_coords[knot], knot_coords[knot-1])
                knot_coords[knot] = new_T_coord
                if knot == knots-1:
                    all_T_coords.add(tuple(new_T_coord))
                # print('T:',T_coord)
        step += 1

print('The tail of the rope visited', len(all_T_coords), 'positions')