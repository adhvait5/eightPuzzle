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


if __name__ == '__main__':

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


    def graphSearch(problem, userInput):
        

        if problem == 1:
            bool = False
            
            while(bool != True):
                #check
                rows = 3
                col = 3
                frontier = PriorityQueue()
                exploreSet = PriorityQueue()
                for i in range(rows):
                    for j in range(col):
                        frontier.insert(userInput[i][j])
                        
                while bool != True:

                    if frontier.isEmpty() == True:
                        print("failure")

                    #psuedoCode 
                    if(node == goalState)
                        return corresponding solution
                    
                    exploreSet = node.insert()

                    #expandNode function

                    



        elif problem == 2:
            return
        elif problem == 3:
            return


    graphSearch(algorithmChoice, userInput)
