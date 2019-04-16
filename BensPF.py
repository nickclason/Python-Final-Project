import queue


# Off campus housing map
def createOrigMaze():
    maze = []
    #             0    1    2    3    4    5    6    7    8
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])  # 0
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])  # 1
    maze.append(["#", " ", "#", "#", " ", " ", "#", " ", "#"])  # 2
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])  # 3
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])  # 4
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])  # 5
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])  # 6
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])  # 7
    maze.append(["#", "#", "X", "#", "#", "#", "#", "#", "#"])  # 8

    return maze


def createEmptyMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "X", "#", "#", "#", "#", "#", "#"])

    return maze


# Pass the start location to this function
def fillFirstValue(coordinate):
    mazePaths[coordinate[0]][coordinate[1]] = 0


# This function should only be passed valid, empty coordinates
def fillMazeSpot(origCoordinate, emptyCoordinate):
    mazePaths[emptyCoordinate[0]][emptyCoordinate[1]] = mazePaths[origCoordinate[0]][origCoordinate[1]] + 1


def isEnd(coordinate, neighborCoordinate):
    x = coordinate[0]
    y = coordinate[1]
    neighborX = neighborCoordinate[0]
    neighborY = neighborCoordinate[1]
    end = 0
    # Check for end
    if mazeOrig[x + neighborX][y + neighborY] == "X":
        # Access solutionLocation as a global variable (You get an error if
        # you don't for some reason)
        global solutionLocation
        solutionLocation += [x + neighborX]
        solutionLocation += [y + neighborY]
        end = 1
    return end


def isValid(coordinate, neighborCoordinate):
    x = coordinate[0]
    y = coordinate[1]
    neighborX = neighborCoordinate[0]
    neighborY = neighborCoordinate[1]
    valid = 0

    # Check for out of bounds
    if (x + neighborX < 0) or (y + neighborY < 0) or (x + neighborX > colCount) or (y + neighborY > rowCount):
        # Keep valid at 0, it's out of bounds
        pass

    # Check for wall
    elif mazeOrig[x+neighborX][y+neighborY] == "#":
        # Keep valid at 0, it's a wall
        pass

    # Check if the path maze has already been filled in at this coordinate
    elif mazePaths[x+neighborX][y+neighborY] != " ":
        # Keep valid at 0, it's already been filled in
        pass

    # Anything else should be a blank space that needs filled in
    else:
        valid = 1

    return valid


def findNeighbors(coordinate):
    neighborList = []
    x = coordinate[0]
    y = coordinate[1]

    for neighborRelativeVal in neighborRelativeVals:
        if isEnd(coordinate, neighborRelativeVal):
            solutionLocation = [[x+neighborRelativeVal[0], y+neighborRelativeVal[1]]]
        if isValid(coordinate, neighborRelativeVal):
            neighborList += [[x+neighborRelativeVal[0], y+neighborRelativeVal[1]]]

    return neighborList


def findPath(x, y):
    # Declare variables
    rowCount = 0
    colCount = 0
    mazeOrig = createOrigMaze()
    mazePaths = createEmptyMaze()
    startLocation = []
    solutionLocation = []
    neighborsList = []

    #                        U        D       R       L
    neighborRelativeVals = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    # Find Start Location
    for i, row in enumerate(mazeOrig):
        for j, column in enumerate(mazeOrig[i]):
            if mazeOrig[i][j] == "O":
                startLocation += [i]
                startLocation += [j]

    # Get amount of rows and cols
    for i, row in enumerate(mazeOrig):
        for j, column in enumerate(mazeOrig[i]):
            if i == 0:
                colCount += 1
        rowCount += 1

    # Check if the user did not provide a start location
    if startLocation == []:
        print("The start location was not found. Please put a 'O' somewhere in the maze")
        exit()

    neighborsQ = queue.Queue()
    neighborsQ.put(startLocation)  # enqueue
    fillFirstValue(startLocation)

    while solutionLocation == []:
        tempCoordinate = neighborsQ.get()  # dequeue
        neighborsList = findNeighbors(tempCoordinate)
        for neighbor in neighborsList:
            if solutionLocation != []:
                break
            else:
                fillMazeSpot(tempCoordinate, neighbor)
                neighborsQ.put(neighbor)
                print(neighbor)


print(solutionLocation)
