#What would your total score be if everything goes exactly according to your strategy guide?

#PART I

#Assumptions:
# A = Rock = X = 1pt
# B = Paper = Y = 2pt
# C = Scissors = Z = 3pt
# Loss = 0pt
# Draw = 3pt
# Win = 6pt

with open('puzzle_input.txt') as f:
    data_txt = f.read() #read the txt file as a string
opponent_pick = data_txt[0::4]
my_pick = data_txt[2::4]

shape_points = 0
for matchup in range(0, len(my_pick)):
    if my_pick[matchup] == "X":
        shape_points += 1
    elif my_pick[matchup] == "Y":
        shape_points += 2
    elif my_pick[matchup] == "Z":
        shape_points += 3
    else:
        print("Something is wrong with your strategy guide")

matchup_points = 0
for matchup in range(0, len(my_pick)):
    if (opponent_pick[matchup] == "A" and my_pick[matchup] == "Z" or
        opponent_pick[matchup] == "B" and my_pick[matchup] == "X" or
        opponent_pick[matchup] == "C" and my_pick[matchup] == "Y"): 
        pass
    elif (opponent_pick[matchup] == "A" and my_pick[matchup] == "X" or 
          opponent_pick[matchup] == "B" and my_pick[matchup] == "Y" or 
          opponent_pick[matchup] == "C" and my_pick[matchup] == "Z"):
        matchup_points += 3
    elif (opponent_pick[matchup] == "A" and my_pick[matchup] == "Y" or 
          opponent_pick[matchup] == "B" and my_pick[matchup] == "Z" or 
          opponent_pick[matchup] == "C" and my_pick[matchup] == "X"):
        matchup_points += 6
    else:
        print("Something is wrong with your strategy guide")

total_points = shape_points + matchup_points
print("Your total score if you follow how your initial interpretation of the strategy guide would be",
      total_points,"points")

#PART II

#Assumptions:
# A = Rock = 1pt
# B = Paper = 2pt
# C = Scissors = 3pt
# Loss = X = 0pt
# Draw = Y = 3pt
# Win = Z = 6pt

shape_points = 0
for matchup in range(0, len(my_pick)):
    if (my_pick[matchup] == "X" and opponent_pick[matchup] == "B" or
        my_pick[matchup] == "Y" and opponent_pick[matchup] == "A" or
        my_pick[matchup] == "Z" and opponent_pick[matchup] == "C"):
        shape_points += 1
    elif (my_pick[matchup] == "X" and opponent_pick[matchup] == "C" or
        my_pick[matchup] == "Y" and opponent_pick[matchup] == "B" or
        my_pick[matchup] == "Z" and opponent_pick[matchup] == "A"):
        shape_points += 2
    elif (my_pick[matchup] == "X" and opponent_pick[matchup] == "A" or
        my_pick[matchup] == "Y" and opponent_pick[matchup] == "C" or
        my_pick[matchup] == "Z" and opponent_pick[matchup] == "B"):
        shape_points += 3
    else:
        print("Something is wrong with your strategy guide")

matchup_points = 0
for matchup in range(0, len(my_pick)):
    if my_pick[matchup] == "X": 
        pass
    elif my_pick[matchup] == "Y":
        matchup_points += 3
    elif my_pick[matchup] == "Z":
        matchup_points += 6
    else:
        print("Something is wrong with your strategy guide")

total_points = shape_points + matchup_points
print("Your total score if you follow the ULTRA TOP SECRET strategy guide would be",total_points,"points")