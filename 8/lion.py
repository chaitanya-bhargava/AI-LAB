from collections import deque

def bfs(start, goal):
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == goal:
            return path
        elif current not in visited:
            visited.add(current)
            for neighbor in get_neighbors(current):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

def get_neighbors(state):
    neighbors = []
    farmer, lion, goat, grass, side = state
    if farmer == 1:
        if goat == side:
            neighbors.append((1-farmer, lion, 1-goat, grass, 1-side))
        if grass == side:
            neighbors.append((1-farmer, lion, goat, 1-grass, 1-side))
        if lion == side:
            neighbors.append((1-farmer, 1-lion, goat, grass, 1-side))
        neighbors.append((1-farmer, lion, goat, grass, 1-side))
    else:
        if lion != side and grass != side:
            neighbors.append((1-farmer, lion, goat, 1-grass, 1-side))
        if lion != side and goat != side:
            neighbors.append((1-farmer, lion, goat, grass, 1-side))
        if goat != side and grass != side:
            neighbors.append((1-farmer, lion, 1-goat, grass, 1-side))
        neighbors.append((1-farmer, lion, goat, grass, 1-side))
    
    return neighbors

start_state = (1, 1, 1, 1, 1) # (farmer, lion, goat, grass, side)
goal_state = (0, 0, 0, 0, 0)

solution = bfs(start_state, goal_state)

if solution:
    for state in solution:
        print(state)
else:
    print("No solution found.")