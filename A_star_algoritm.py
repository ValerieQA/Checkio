from Queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0, solver = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.parent = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass
    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in xrange(len(self.goal)-1):
                val = self.value
                val = val[:1] + val[i+1] + val[1] + val[i+2]
                child = State_String(val, self)
                self.children.append(child)

class Astar_Solver:
    def __init__(self, start, goal):
        self.path = []