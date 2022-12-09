#PART I 
#Consider your map; how many trees are visible from outside the grid?

#A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
#Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

#PART II
#Consider each tree on your map. What is the highest scenic score possible for any tree?

#A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 
#To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
#stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
#(If a tree is right on the edge, at least one of its viewing distances will be zero.)

with open('puzzle_input.txt') as f:
    trees_txt = f.read().splitlines()

#establish size of forest
rows = len(trees_txt)
columns = len(trees_txt[0])

def isOnEdge(row, column):
    """ This function tells you if a given tree is on the edge of the forest or not """
    if row == 0 or column == 0 or row == rows-1 or column == columns-1:
        return True
    else:
        return False

#assume no trees are visible
visible = []
for row in range(rows):
    visible.append([])
    for column in range(columns):
        visible[row].append(False)
        
#make edge trees visible
for row in range(rows):
    for column in range(columns):
        if isOnEdge(row,column):
            visible[row][column] = True

#initialize scenic score
scenic_score = []
for row in range(rows):
    scenic_score.append([])
    for column in range(columns):
        scenic_score[row].append(0)

#check all non-edge trees
for row in range(1,rows-1): 
    for column in range(1,columns-1): 
        # print('checking (',row,',',column,') =',trees_txt[row][column])
        #check to the left
            # print('check to the left')
            if all(trees_txt[row][column] > trees_txt[row][l] for l in range(0,column)):
                visible[row][column] = True
            v_d = 1
            for l in range(column-1,-1,-1):
                while (trees_txt[row][column] > trees_txt[row][l]) and (isOnEdge(row, l) == False):
                    v_d += 1
                    break
                if trees_txt[row][column] <= trees_txt[row][l]:
                    break            
            scenic_score[row][column] += v_d
        #check to the right   
            # print('check to the right')
            if all(trees_txt[row][column] > trees_txt[row][r] for r in range(column+1,columns)):
                visible[row][column] = True
            v_d = 1
            for r in range(column+1,columns):
                while (trees_txt[row][column] > trees_txt[row][r]) and (isOnEdge(row, r) == False):
                    v_d += 1
                    break
                if trees_txt[row][column] <= trees_txt[row][r]:
                    break
            scenic_score[row][column] *= v_d
        #check to the top   
            # print('check to the top')
            if all(trees_txt[row][column] > trees_txt[t][column] for t in range(0,row)):
                visible[row][column] = True
            v_d = 1
            for t in range(row-1,-1,-1):
                while (trees_txt[row][column] > trees_txt[t][column]) and (isOnEdge(t, column) == False):
                    v_d += 1
                    break
                if trees_txt[row][column] <= trees_txt[t][column]:
                    break
            scenic_score[row][column] *= v_d
        #check to the bottom   
            # print('check to the bottom')
            if all(trees_txt[row][column] > trees_txt[b][column] for b in range(row+1,rows)):
                visible[row][column] = True
            v_d = 1
            for b in range(row+1,rows):
                while (trees_txt[row][column] > trees_txt[b][column]) and (isOnEdge(b, column) == False):
                    v_d += 1
                    break
                if trees_txt[row][column] <= trees_txt[b][column]:
                    break
            scenic_score[row][column] *= v_d

max_scenic_score = max([x for sublist in scenic_score for x in sublist])
visible_trees = sum(x.count(True) for x in visible)
print('There are',visible_trees,'visible trees')
print('The highest possible scenic score is',max_scenic_score)



