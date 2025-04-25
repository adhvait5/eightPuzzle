import numpy as np



print("Welcome to 862350417's, SID, and SIDs 8 puzzle solver. Enter your puzzle, use a zero to represent the blank")

rows = 3
col = 3

userInput = np.array([[0,0,0], [0,0,0], [0,0,0]])
print("entries row-wise:")
for i in range(3):
    for j in range(3):
        userInput[i][j] = int(input())


print("")
print("Your matrix is:")
print("")

for i in range(rows):
    for j in range(col):
        print(userInput[i][j], end=" ")
    print()

print("")
print("Goal State:")
print("")

goalState = np.array([[1,2,3], [4,5,6], [7,8,0]])
for i in range(rows):
    for j in range(col):
        print(goalState[i][j], end=" ")
    print()

print("Choose your Algorithm")
print("1)Uniform Cost Search")
print("2)A* with the Misplaced Tile heuristic.")
print("3)A* with the Euclidean distance heuristic")

algorithmChoice = int(input())

#print(algorithmChoice)



def graphSearch(problem):
    

    if problem == 1:
        bool = True
        
        #check
        rows = 3
        col = 3
        for i in range(rows):
            for j in range(col):
                if userInput[i][j] != goalState[i][j]:
                    bool = False
        


        if bool == True:
            print("Reached Goal State!!!")




    elif problem == 2:
        return
    elif problem == 3:
        return

graphSearch(algorithmChoice)
