import numpy as np

# Priority Queue from https://www.geeksforgeeks.org/priority-queue-in-python/
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 

    def isEmpty(self):
        return len(self.queue) == 0
 

    def insert(self, data):
        self.queue.append(data)
 

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()

#Node class from https://www.geeksforgeeks.org/python-program-for-inserting-a-node-in-a-linked-list/
class Node:
 
    # Function to initialize the 
    # node object
    def __init__(self, data):
 
        # Assign data
        if data == None:
            self.data = np.array([[0,0,0], [0,0,0], [0,0,0]])
            self.root = None
            self.h = 0
        else:
            self.data = data
            self.root = None
            self.h = 0
        
        def updateState(self, updateState):
            self.data = np.array(updateState)

        def returnState(self):
            return self.data
 
        # Initialize next as null
        self.next = None 
 
 
if __name__ == '__main__':

    print("Welcome to 862350417's, SID, and SIDs 8 puzzle solver. Enter your puzzle, use a zero to represent the blank")

    rows = 3
    col = 3

    userInput = Node()
    print("entries row-wise:")
    for i in range(3):
        for j in range(3):
            userInput.state[i][j] = int(input())


    print("")
    print("Your matrix is:")
    print("")

    #for i in range(rows):
       # for j in range(col):
            #print(userInput[i][j], end=" ")
       # print()

    print(userInput.returnState())

    print("")
    print("Goal State:")
    print("")

    goalState = Node(np.array([[1,2,3], [4,5,6], [7,8,0]]))
    for i in range(rows):
        for j in range(col):
            print(goalState[i][j], end=" ")

    print(goalState.returnState())

    print("Choose your Algorithm")
    print("1)Uniform Cost Search")
    print("2)A* with the Misplaced Tile heuristic.")
    print("3)A* with the Euclidean distance heuristic")

    algorithmChoice = int(input())

    #H(n)
    def misplacedTile(inputState):
        count = 0
        for i in range(3):
            for j in range(3):
                if(inputState[i][j] != goalState[i][j]):
                    count += 1

        return count
    
    #G(n)
    #Down
    def moveDown(inputState):
        row = 0
        col = 0
        movedTile = 0
        for i in range(3):
            for j in range(3):
                if(inputState[i][j] == 0):
                    row = i
                    col = j
        if(row != 2):
            movedTile = inputState[row + 1][col]
            inputState[row + 1][col] = 0
            inputState[row][col] = movedTile
            return 1
        
    def moveUp(inputState):
        row = 0
        col = 0
        movedTile = 0
        for i in range(3):
            for j in range(3):
                if(inputState[i][j] == 0):
                    row = i
                    col = j
        if(row != 0):
            movedTile = inputState[row - 1][col]
            inputState[row - 1][col] = 0
            inputState[row][col] = movedTile
            return 1
        
    def moveRight(inputState):
        row = 0
        col = 0
        movedTile = 0
        for i in range(3):
            for j in range(3):
                if(inputState[i][j] == 0):
                    row = i
                    col = j
        if(col != 2):
            movedTile = inputState[row][col + 1]
            inputState[row][col+1] = 0
            inputState[row][col] = movedTile
            return 1
        
    def moveLeft(inputState):
        row = 0
        col = 0
        movedTile = 0
        for i in range(3):
            for j in range(3):
                if(inputState[i][j] == 0):
                    row = i
                    col = j
        if(col != 0):
            movedTile = inputState[row][col - 1]
            inputState[row][col-1] = 0
            inputState[row][col] = movedTile
            return 1
        
        


    def graphSearch(problem, userInput):
        

        if problem == 1: #Uniform Cost Search

            bool = False
            frontier = PriorityQueue()
            frontier.insert(userInput)

            exploreSet = PriorityQueue()

            while(bool != True):

                if frontier.isEmpty() == True:
                    print("failure")

                currNode = frontier.delete()

                #psuedoCode for now
                if(currNode.data == goalState.data):
                    print("Solution found!")
                    break
                
                moveDown(currNode)
                moveUp(currNode)
                moveRight(currNode)
                moveLeft(currNode)
                
                exploreSet.insert(currNode)

                #expandNode function for repeated states

                    



        elif problem == 2: #A* Misplaced tile
            return
        elif problem == 3: #A* Euclidean Distance
            return


    graphSearch(algorithmChoice, userInput)
