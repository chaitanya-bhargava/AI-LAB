start_state = {'farmer': 'left','lion':'left', 'goat': 'left', 'grass': 'left'}
goal_state = {'farmer': 'right','lion':'right', 'goat': 'right', 'grass': 'right'}

# define a function to check if a state is valid
def is_valid(state):
   if (state['goat'] == state['grass'] and state['goat'] != state['farmer']) or (state['lion'] == state['goat'] and state['lion'] != state['farmer']):
       return False
   return True

# define a function to get the valid neighbor states
def get_neighbors(state):
   neighbors = []
   # check if the farmer is on the left or right bank
   if state['farmer'] == 'left':
       # move farmer and goat to right bank
       new_state = {'farmer': 'right','lion':state['lion'], 'goat': 'right', 'grass': state['grass']}
       if is_valid(new_state):
           neighbors.append(new_state)
       # move farmer and grass to right bank
       new_state = {'farmer': 'right','lion':state['lion'], 'goat': state['goat'], 'grass': 'right'}
       if is_valid(new_state):
           neighbors.append(new_state)
       # move farmer and lion to right bank
       new_state = {'farmer': 'right','lion':'right','goat': state['goat'], 'grass':state['grass']}
       if is_valid(new_state):
           neighbors.append(new_state)
   else:
       # move farmer to left bank alone
       new_state = {'farmer': 'left','lion':state['lion'],'goat': state['goat'], 'grass': state['grass']}
       if is_valid(new_state):
           neighbors.append(new_state)
       # move farmer and goat to left bank
       new_state = {'farmer': 'left','lion':state['lion'], 'goat': 'left', 'grass': state['grass']}
       if is_valid(new_state):
           neighbors.append(new_state)
       # move farmer and grass to left bank
       new_state = {'farmer': 'left','lion':state['lion'], 'goat': state['goat'], 'grass': 'left'}
       if is_valid(new_state):
           neighbors.append(new_state)
       # move farmer and lion to left bank
       new_state = {'farmer': 'left','lion': 'left', 'goat': state['goat'], 'grass': state['grass']}
       if is_valid(new_state):
           neighbors.append(new_state)
   return neighbors

# define a function to perform a breadth-first search
def bfs(start, goal):
   queue = [[start]]
   visited = set([str(start)])
   while queue:
       path = queue.pop(0)
       state = path[-1]
       if state == goal:
           return path
       for neighbor in get_neighbors(state):
           if str(neighbor) not in visited:
               visited.add(str(neighbor))
               new_path = path + [neighbor]
               queue.append(new_path)
   return None

# get user input for starting state
start_state = {}
print("Enter starting state:")
start_state['farmer'] = input("Farmer's location (left or right): ")
start_state['lion'] = input("Lion's location (left or right): ")
start_state['goat'] = input("Goat's location (left or right): ")
start_state['grass'] = input("Grass's location (left or right): ")

# check if starting state is valid
if not is_valid(start_state):
   print("Starting state is invalid.")
else:
   # find solution using breadth-first search
   solution = bfs(start_state, goal_state)
   if solution:
       print("Solution found:")
       for state in solution:
           print(state)
   else:
       print("No solution found.")
