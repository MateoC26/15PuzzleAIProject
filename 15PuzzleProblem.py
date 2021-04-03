from queue import PriorityQueue
import copy

# state: 2D array (str)
# parent: Node
# action: int representing action (1-8)
# path_cost: Cost from root to node n (int)
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        self_mag = sumOfChessboardDistances(self.state) + self.path_cost
        other_mag = sumOfChessboardDistances(other.state) + other.path_cost
        return self_mag < other_mag


class Problem:
    def __init__(self, initial, goal, actions):
        self.initial = initial
        self.goal = goal
        self.actions = actions

    def isGoal(self, state):
        return state == goal

    # Returns new_state resulting from doing action on state
    # Could probably cut down
    def result(self, state, action):
        new_state = copy.deepcopy(state)

        blank_row = -1
        blank_col = -1

        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                if(new_state[i][j] == '0'):
                    blank_row = i
                    blank_col = j

        if(action == 1):
            if(blank_col == 0):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col - 1]
            new_state[blank_row][blank_col - 1] = '0'
        elif(action == 2):
            if(blank_row == 0 or blank_col == 0):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row - 1][blank_col - 1]
            new_state[blank_row - 1][blank_col - 1] = '0'
        elif(action == 3):
            if (blank_row == 0):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row - 1][blank_col]
            new_state[blank_row - 1][blank_col] = '0'
        elif(action == 4):
            if (blank_row == 0 or blank_col == 3):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row - 1][blank_col + 1]
            new_state[blank_row - 1][blank_col + 1] = '0'
        elif(action == 5):
            if (blank_col == 3):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col + 1]
            new_state[blank_row][blank_col + 1] = '0'
        elif (action == 6):
            if (blank_row == 3 or blank_col == 3):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row + 1][blank_col + 1]
            new_state[blank_row + 1][blank_col + 1] = '0'
        elif (action == 7):
            if (blank_row == 3):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row + 1][blank_col]
            new_state[blank_row + 1][blank_col] = '0'
        elif (action == 8):
            if (blank_row == 3 or blank_col == 0):
                return new_state
            new_state[blank_row][blank_col] = new_state[blank_row + 1][blank_col - 1]
            new_state[blank_row + 1][blank_col - 1] = '0'

        return new_state

    # ActionCost will always be 1 (just for comprehension in Expand function - can delete when done)
    def actionCost(self, state, action, new_state):
        return 1


# A* Algorithm
def bestFirstSearch(prob):
    node = Node(prob.initial)

    # Priority Queue
    # f(n) = h(n) + g(n)
    frontier = PriorityQueue()
    frontier.put(node)

    # Lookup table
    # Using str of list as key
    reached = {}
    reached[str(prob.initial)] = node

    num_nodes = 0

    while not frontier.empty():
        node = frontier.get()

        if(prob.isGoal(node.state)):
            return (node, num_nodes)

        for child in expand(prob, node):
            curr_state = child.state

            # Is num_nodes updated here
            num_nodes += 1

            if(str(curr_state) not in reached or child.path_cost < reached[str(curr_state)].path_cost):
                # Or is num_nodes updated here
                #num_nodes += 1
                reached[str(curr_state)] = child
                frontier.put(child)

    return None


# Expands a node
def expand(problem, node):
    curr_state = node.state
    ret = []
    for action in problem.actions:
        new_state = problem.result(curr_state, action)
        cost = node.path_cost + problem.actionCost(curr_state, action, new_state)
        ret.append(Node(new_state, node, action,cost))
        yield Node(new_state, node, action, cost)


# Could cut down (or one line)
# Uses dictionary, could use a goal state parameter instead
def chessboardDistance(tile, row, col):
    goal_row = goal_dict[tile][0]
    goal_col = goal_dict[tile][1]

    row_dist = abs(goal_row - row)
    col_dist = abs(goal_col - col)

    return max(row_dist, col_dist)


# Heuristic Function
def sumOfChessboardDistances(curr_state):
    sum = 0

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            if(curr_state[i][j] != "0"):
                curr_dist = chessboardDistance(curr_state[i][j], i, j)
                sum += curr_dist

    return sum

# ----------------------------------------------- Main ------------------------------------------------------------

# Ask for file name
print("Please enter the input file name (ex. fileName.txt)")
file_name = input();

input_file = open(file_name)

initial = []
goal = []

input_str = input_file.read()

# Splits with each new line
split_input = input_str.split('\n')
switch = False

# Splits with each space
# Appends to initial if swtich = False
# else appends to goal
for arr in split_input:
    if arr == '':
        switch = True
        continue

    if not switch:
        initial.append(arr.split(" "))
    else:
        goal.append(arr.split(" "))


# Dictionary for chessboard distance
goal_dict = {}
for row in range(0, 4, 1):
    for col in range(0, 4, 1):
        if goal[row][col] != "0":
            goal_dict[goal[row][col]] = (row, col)

# Solving the problem
p = Problem(initial, goal, [1, 2, 3, 4, 5, 6, 7, 8])
sol = bestFirstSearch(p)
node = sol[0]
num_of_nodes = sol[1]

# Actions and f values
# d number of actions
# d + 1 number of f values
acts = []
fs = []
while True:
    if(node.parent == None):
        fs.insert(0, sumOfChessboardDistances(node.state))
        break
    acts.insert(0, node.action)
    fs.insert(0, sumOfChessboardDistances(node.state))
    node = node.parent

depth = len(acts)

print("---------------OUTPUT-----------------")
# Prints the initial and goal states
for row in range(0, 4, 1):
    for col in range(0, 4, 1):
        print(initial[row][col], end = " ") # n
    print()

print()

for row in range(0, 4, 1):
    for col in range(0, 4, 1):
        print(goal[row][col], end = " ") # m
    print()

print()

# Can just print this instead of initial and goal separately
# print(input_str)

# d
print(depth)

# N
print(num_of_nodes)

# A
for a in acts:
    print(a, end=" ")

print()

# F
for f in fs:
    print(f, end=" ")

print()

# Checks if the solution node has the goal state
#for row in range(0, 4, 1):
#    for col in range(0, 4, 1):
#        (sol[0].state[row][col], end=" ")
#    print()
#print()

input_file.close()

#--------------------------------------------TO DO---------------------------------------
# Where to update number of nodes in bestFirstSearch
# Is it possible to get depth inside of bestFirstSearch
# Get it to output to a text file
# Get 3 output txt files for input files
# Clean up the file (Change some names for clarity, cut down unnecessary code, add comments, etc.)
# Create PDF w/ instructions
# Could make the prompt for filename better (ask to re-enter if file doesn't exist)
# Maybe more...