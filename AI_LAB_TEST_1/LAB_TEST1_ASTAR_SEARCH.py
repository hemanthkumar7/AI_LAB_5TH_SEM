class Node:
    def __init__(self, data, level, fvalue):
        self.data = data
        self.level = level
        self.fvalue = fvalue

    def spawn_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.close = []

    def accept(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f_value(self, start, goal):
        return self.h_value(start.data, goal) + start.level

    def h_value(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def start_problem(self):
        print("We are using A* search")
        print("Enter the start state")
        start = self.accept()
        print("Enter the goal state")
        goal = self.accept()
        count = 0

        start = Node(start, 0, 0)
        start.fvalue = self.f_value(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            count = count + 1
            print("")
            print("|")
            print("|")
            print("Y")
            print("")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            print("Number of moves:", count)
            if self.h_value(cur.data, goal) == 0:
                break
            for i in cur.spawn_child():
                i.fvalue = self.f_value(i, goal)
                self.open.append(i)
            self.close.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.fvalue, reverse=False)


puz = Puzzle(3)
puz.start_problem()