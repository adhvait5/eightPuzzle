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
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min_val]:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()


#Node class from https://www.geeksforgeeks.org/python-program-for-inserting-a-node-in-a-linked-list/
#https://www.geeksforgeeks.org/python-__lt__-magic-method/


class Node:
 
    # Function to initialize the 
    # node object
    def __init__(self, data):
 
        # Assign data
        self.data = data
        self.root = None
        self.hN = 0
        self.gN = 0
        #self.fN = self.gN + self.hN

        self.down = None
        self.up = None
        self.right = None
        self.left = None
        

    def __lt__(self, o):
        return self.hN + self.gN < o.gN + o.hN
    
    def __gt__(self, o):
        return self.fN > o.fN
    
    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.data[i][j], end=" ")
            print()
        print()

 
 
 
if __name__ == '__main__':

    print("Welcome to 862350417's 8 puzzle solver!")
    print("Choose a puzzle:")
    print("1)Trivial")
    print("2)Easy")
    print("3)Very Easy")
    print("4)Doable")
    print("5)Oh Boy")
    print("6)Impossible")
    print("7)Enter your own Puzzle")
    print("")
    puzzleChoice = int(input())

    #rows = 3
    #col = 3
    
    if puzzleChoice == 1:
        userInput = np.array([[1,2,3], [4,5,6], [7,8,0]])
    if puzzleChoice == 2:
        userInput = np.array([[1,2,0], [4,5,3], [7,8,6]])
    if puzzleChoice == 3:
        userInput = np.array([[1,2,3], [4,5,6], [7,0,8]])
    if puzzleChoice == 4:
        userInput = np.array([[0,1,2], [4,5,3], [7,8,6]])
    if puzzleChoice == 5:
        userInput = np.array([[8,7,1], [6,0,2], [5,4,3]])
    if puzzleChoice == 6:
        userInput = np.array([[1,2,3], [4,5,6], [8,7,0]])
    if puzzleChoice == 7:
        userInput = np.array([[0,0,0], [0,0,0], [0,0,0]])
        
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter your puzzle row-wise:")
        for i in range(3):
            for j in range(3):
                userInput[i][j] = int(input())


    print("")
    print("Your matrix is:")
    print("")

    for i in range(3):
       for j in range(3):
            print(userInput[i][j], end=" ")
       print()


    print("")
    print("Goal State:")
    print("")

    goalState = np.array([[1,2,3], [4,5,6], [7,8,0]])
    for i in range(3):
        for j in range(3):
            print(goalState[i][j], end=" ")
        print()

    print("")
    print("Choose your Algorithm:")
    print("1)Uniform Cost Search")
    print("2)A* with the Misplaced Tile heuristic.")
    print("3)A* with the Euclidean distance heuristic")

    algorithmChoice = int(input())

    #H(n)
    def misplacedTile(inputState, goalState):
        count = 0
        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] != 0):
                    if(inputState.data[i][j] != goalState[i][j]):
                        count += 1

        return count
    
    def euclideanDist(inputState,goalState):
        count = 0

        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] != 0):
                    if(inputState.data[i][j] != goalState[i][j]):
                        indexVal = inputState.data[i][j]
                        for k in range(3):
                            for l in range(3):
                                if(goalState[k][l] == indexVal):
                                    count += np.sqrt(np.square(k-i) + np.square(l-j))

      
        return count
    

    #G(n)
    #Down
    def moveDown(inputState):
        row = 0
        col = 0
        movedTile = 0
        copyInput = Node(np.copy(inputState.data))
        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] == 0):
                    row = i
                    col = j
        if(row != 2):
            movedTile = inputState.data[row + 1][col]
            copyInput.data[row + 1][col] = 0
            copyInput.data[row][col] = movedTile
            inputState.down = copyInput
            inputState.down.root = inputState
            
            inputState.down.gN = inputState.gN + 1
        
    def moveUp(inputState):
        row = 0
        col = 0
        movedTile = 0
        copyInput = Node(np.copy(inputState.data))
        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] == 0):
                    row = i
                    col = j
        if(row != 0):
            movedTile = inputState.data[row - 1][col]
            copyInput.data[row - 1][col] = 0
            copyInput.data[row][col] = movedTile
            inputState.up = copyInput
            inputState.up.root = inputState
            
            inputState.up.gN = inputState.gN + 1
        
    def moveRight(inputState):
        row = 0
        col = 0
        movedTile = 0
        copyInput = Node(np.copy(inputState.data))
        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] == 0):
                    row = i
                    col = j
        if(col != 2):
            movedTile = inputState.data[row][col + 1]
            copyInput.data[row][col+1] = 0
            copyInput.data[row][col] = movedTile
            inputState.right= copyInput
            inputState.right.root = inputState
            
            inputState.right.gN = inputState.gN + 1
        
    def moveLeft(inputState):
        row = 0
        col = 0
        movedTile = 0
        copyInput = Node(np.copy(inputState.data))
        for i in range(3):
            for j in range(3):
                if(inputState.data[i][j] == 0):
                    row = i
                    col = j
        if(col != 0):
            movedTile = inputState.data[row][col - 1]
            copyInput.data[row][col-1] = 0
            copyInput.data[row][col] = movedTile
            inputState.left = copyInput
            inputState.left.root = inputState
            
            inputState.left.gN = inputState.gN + 1
        
        


    def graphSearch(problem, userInput):
        

        if problem == 1: #Uniform Cost Search

            bool = False
            userInputNode = Node(userInput)
            frontier = PriorityQueue()
            frontier.insert(userInputNode)
            maxQueueSize = 0

            exploreSet = set()

            while(bool != True):

                if frontier.isEmpty() == True:
                    print("failure")
                    return
                
                if len(frontier.queue) > maxQueueSize:
                    maxQueueSize = len(frontier.queue)

                currNode = frontier.delete()

                #frontier.delete()

                currTuple = []
                for i in currNode.data:
                    currTuple.append(tuple(i))

                exploreNode = tuple(currTuple)
                exploreSet.add(exploreNode)


                #Goal Check
                goalFound = 0
                for i in range(3):
                    for j in range(3):
                        if(currNode.data[i][j] == goalState[i][j]):
                            goalFound += 1
                if goalFound == 9:
                    print("Solution found!")
                    print("")
                    print("Cost:")
                    print(currNode.gN)
                    print("Maximum size of the queue: ")
                    print(maxQueueSize)
                    break
                else:
                    goalFound = 0
                    
                    currNode.print()
                    
                    
                    

                    
                    moveDown(currNode)
                    moveUp(currNode)
                    moveRight(currNode)
                    moveLeft(currNode)
                    
                    if currNode.right != None:
                        currTuple = []
                        for i in currNode.right.data:
                            currTuple.append(tuple(i))

                        exploreNodeRight = tuple(currTuple)

                        frontierBool = True
                        for i in frontier.queue:
                            if (np.array_equal(currNode.right.data, i.data)):
                                frontierBool = False
                                break

                        if frontierBool and exploreNodeRight not in exploreSet:
                            frontier.insert(currNode.right)

                    if currNode.down != None:
                        currTuple = []
                        for i in currNode.down.data:
                            currTuple.append(tuple(i))

                        exploreNodeDown = tuple(currTuple)

                        frontierBool = True
                        for i in frontier.queue:
                            if (np.array_equal(currNode.down.data, i.data)):
                                frontierBool = False
                                break

                        if frontierBool and exploreNodeDown not in exploreSet:
                            frontier.insert(currNode.down)

                    if currNode.up != None:
                        currTuple = []
                        for i in currNode.up.data:
                            currTuple.append(tuple(i))

                        exploreNodeUp = tuple(currTuple)

                        frontierBool = True
                        for i in frontier.queue:
                            if (np.array_equal(currNode.up.data, i.data)):
                                frontierBool = False
                                break

                        if frontierBool and exploreNodeUp not in exploreSet:
                            frontier.insert(currNode.up)

                    if currNode.left != None:
                        currTuple = []
                        for i in currNode.left.data:
                            currTuple.append(tuple(i))

                        exploreNodeLeft = tuple(currTuple)

                        frontierBool = True
                        for i in frontier.queue:
                            if (np.array_equal(currNode.left.data,i.data)):
                                frontierBool = False
                                break

                        if frontierBool and exploreNodeLeft not in exploreSet:
                            frontier.insert(currNode.left)
                        
                    


                    



        elif problem == 2: #A* Misplaced tile
            bool = False
            userInputNode = Node(userInput)
            userInputNode.hN = misplacedTile(userInputNode, goalState)
            frontier = PriorityQueue()
            frontier.insert(userInputNode)
            maxQueueSize = 0

            #return print(userInputNode.hN)

            exploreSet = set()

            while(bool != True):

                if frontier.isEmpty() == True:
                    print("failure")
                    return
                
                if len(frontier.queue) > maxQueueSize:
                    maxQueueSize = len(frontier.queue)

                currNode = frontier.delete()

                currTuple = []
                for i in currNode.data:
                    currTuple.append(tuple(i))

                exploreNode = tuple(currTuple)
                currTuple = []


                #Goal Check
                goalFound = 0
                for i in range(3):
                    for j in range(3):
                        if(currNode.data[i][j] == goalState[i][j]):
                            goalFound += 1
                if goalFound == 9:
                    print("Solution found!")
                    print("")
                    print("Cost:")
                    print(currNode.gN + currNode. hN)
                    print("Maximum size of the queue: ")
                    print(maxQueueSize)
                    print("")
                    break
                else:
                    goalFound = 0
                    
      
                    currNode.print()
                    exploreSet.add(exploreNode)


                    moveDown(currNode)
                    moveUp(currNode)
                    moveRight(currNode)
                    moveLeft(currNode)
                        

                    if currNode.down != None:
                        currTuple = []
                        for i in currNode.down.data:
                            currTuple.append(tuple(i))

                        exploreNodeDown = tuple(currTuple)

                        if currNode.down not in frontier.queue or exploreNodeDown not in exploreSet:
                            currNode.down.hN = misplacedTile(currNode.down, goalState)
                            frontier.insert(currNode.down)

                    if currNode.up != None:
                        currTuple = []
                        for i in currNode.up.data:
                            currTuple.append(tuple(i))

                        exploreNodeUp = tuple(currTuple)
                        if currNode.up not in frontier.queue or exploreNodeUp not in exploreSet:
                            currNode.up.hN = misplacedTile(currNode.up, goalState)
                            frontier.insert(currNode.up)

                    if currNode.left != None:
                        currTuple = []
                        for i in currNode.left.data:
                            currTuple.append(tuple(i))

                        exploreNodeLeft = tuple(currTuple)
                        if currNode.left not in frontier.queue or exploreNodeLeft not in exploreSet:
                            currNode.left.hN = misplacedTile(currNode.left, goalState)
                            frontier.insert(currNode.left)
                        
                    if currNode.right != None:
                        currTuple = []
                        for i in currNode.right.data:
                            currTuple.append(tuple(i))

                        exploreNodeRight = tuple(currTuple)
                        if currNode.right not in frontier.queue or exploreNodeRight not in exploreSet:
                            currNode.right.hN = misplacedTile(currNode.right, goalState)
                            frontier.insert(currNode.right)



        elif problem == 3: #A* Euclidean Distance
            bool = False
            userInputNode = Node(userInput)
            userInputNode.hN = euclideanDist(userInputNode, goalState)
            frontier = PriorityQueue()
            frontier.insert(userInputNode)
            maxQueueSize = 0

            #return print(userInputNode.hN)

            exploreSet = set()

            while(bool != True):

                if frontier.isEmpty() == True:
                    print("failure")
                    return
                
                if len(frontier.queue) > maxQueueSize:
                    maxQueueSize = len(frontier.queue)

                currNode = frontier.delete()

                currTuple = []
                for i in currNode.data:
                    currTuple.append(tuple(i))

                exploreNode = tuple(currTuple)
                currTuple = []


                #Goal Check
                goalFound = 0
                for i in range(3):
                    for j in range(3):
                        if(currNode.data[i][j] == goalState[i][j]):
                            goalFound += 1
                if goalFound == 9:
                    print("Solution found!")
                    print("")
                    print("Cost:")
                    print(currNode.gN + currNode. hN)
                    print("Maximum size of the queue: ")
                    print(maxQueueSize)
                    break
                else:
                    goalFound = 0
                    
      
                    currNode.print()
                    exploreSet.add(exploreNode)


                    moveDown(currNode)
                    moveUp(currNode)
                    moveRight(currNode)
                    moveLeft(currNode)
                        

                    if currNode.down != None:
                        currTuple = []
                        for i in currNode.down.data:
                            currTuple.append(tuple(i))

                        exploreNodeDown = tuple(currTuple)

                        if currNode.down not in frontier.queue or exploreNodeDown not in exploreSet:
                            currNode.down.hN = euclideanDist(currNode.down, goalState)
                            frontier.insert(currNode.down)

                    if currNode.up != None:
                        currTuple = []
                        for i in currNode.up.data:
                            currTuple.append(tuple(i))

                        exploreNodeUp = tuple(currTuple)
                        if currNode.up not in frontier.queue or exploreNodeUp not in exploreSet:
                            currNode.up.hN = euclideanDist(currNode.up, goalState)
                            frontier.insert(currNode.up)

                    if currNode.left != None:
                        currTuple = []
                        for i in currNode.left.data:
                            currTuple.append(tuple(i))

                        exploreNodeLeft = tuple(currTuple)
                        if currNode.left not in frontier.queue or exploreNodeLeft not in exploreSet:
                            currNode.left.hN = euclideanDist(currNode.left, goalState)
                            frontier.insert(currNode.left)
                        
                    if currNode.right != None:
                        currTuple = []
                        for i in currNode.right.data:
                            currTuple.append(tuple(i))

                        exploreNodeRight = tuple(currTuple)
                        if currNode.right not in frontier.queue or exploreNodeRight not in exploreSet:
                            currNode.right.hN = euclideanDist(currNode.right, goalState)
                            frontier.insert(currNode.right)



    #Run code
    graphSearch(algorithmChoice, userInput)
