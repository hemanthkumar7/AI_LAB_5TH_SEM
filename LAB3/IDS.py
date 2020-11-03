from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):

        if src == target: return True

        if maxDepth <= 0: return False

        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


n = int(input("Enter the number of vertices: "))
g = Graph(n);
e1 = 1
print("Enter the connecting vertices and -1 to stop")
while e1 != -1:
    e1, e2 = input("add edge between: ").split()
    e1 = int(e1)
    e2 = int(e2)
    if e1 == -1:
        break
    g.addEdge(e1, e2)

target = int(input("Enter the target to search: "))
maxDepth = int(input("Enter the maximum depth: "))
src = int(input("Enter the source vertex: "))

if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")