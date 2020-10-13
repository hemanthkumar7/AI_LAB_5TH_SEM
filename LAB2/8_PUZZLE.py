from copy import deepcopy
import datetime


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def search(src, target):
    path = list()
    start = Node(state=src, parent=None, action=None)
    frontier = QueueFrontier()      # --for BFS
    # frontier = StackFrontier()      --for DFS
    explored = []
    frontier.add(start)
    while True:
        if frontier.empty():
            return None
        node = deepcopy(frontier.remove())
        explored.append(node.state)
        for action, state in possible_moves(node.state):
            if not frontier.contains_state(state) and ( state not in explored ):
                if state == target:
                    path.append((action, state))
                    while node.parent is not None:
                        path.append((node.action, node.state))
                        node = node.parent
                    path.reverse()
                    return path
                ss = Node(state=state, parent=node, action=action)
                frontier.add(ss)
   

def index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def possible_moves(state):
    
    b = index(state, 0)
    
    d = []
    if b[0] < 2:
        d.append('Down')
    if b[0] > 0:
        d.append('Up')
    if b[1] < 2:
        d.append('Right')
    if b[1] > 0:
        d.append('Left')
       pos_moves = []
    for i in d:
        move = gen(state, i, b)
        pos_moves.append((i ,move))
    
    return pos_moves


def gen(state, m, b): # m(move) is direction to slide, b(blank)is index of empty spot
    
    temp = deepcopy(state)
    if m == 'Up':
        temp[b[0]][b[1]] , temp[b[0] - 1][b[1]] = temp[b[0] - 1][b[1]] , temp[b[0]][b[1]]
    elif m == 'Down':
        temp[b[0]][b[1]] , temp[b[0] + 1][b[1]] = temp[b[0] + 1][b[1]] , temp[b[0]][b[1]]
    elif m == 'Left':
        temp[b[0]][b[1]] , temp[b[0]][b[1] - 1] = temp[b[0]][b[1] - 1] , temp[b[0]][b[1]]
    elif m == 'Right':
        temp[b[0]][b[1]] , temp[b[0]][b[1] + 1] = temp[b[0]][b[1] + 1] , temp[b[0]][b[1]]
    
    # return new state with tested move to later check if "src == target"
    return temp


def display(table):
    for r in table:
        for c in r:
            if c == None:
                print(" ", end=" | ")
            else:
                print(c, end=" | ")
        print()


src = []
target = []
print("Enter the Source state : ")
for _ in range(3):
    row = input().split()
    src.append(row)
print("Enter the Target state : ")
for _ in range(3):
    row = input().split()
    target.append(row)
for i in range(3):
    for j in range(3):
        target[i][j] = int(target[i][j])
        src[i][j] = int(src[i][j])
print("Calculating : ")
x = datetime.datetime.now()
path = search(src, target)
if path is None:
    print("It's IMPOSSIBLE reaching the TARGET from the provided SOURCE state..!  :(")
else:
    degrees = len(path)
    print(degrees,"number of operations required to reach target.")
    print()
    path = [(None, src)] + path
    for i in range(degrees):
        print("Stage :", i+1)
        display(path[i][1])
        print("In the above table move 0 to",path[i+1][0])
        print()
    print("The Target is Reached : ")
    display(target)
    print("Success :)")
x = datetime.datetime.now() - x
print("Time Taken :",x)
print("DEPTH FIRST SEARCH METHOD")