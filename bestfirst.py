def bestFirstAlgo(start_node):
    open_set = set(start_node)
    closed_set = set()             
    parents = {}        
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or heuristic(v) < heuristic(n):
                n = v
        if heuristic(n)==0 or Graph_nodes[n] == None:
            pass
        else:
            for m in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
        if n == None:
            print('Path does not exist!')
            return None
        if heuristic(n)==0:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 17,
        'B': 14,
        'C': 21,
        'D': 100,
        'E': 12,
        'F': 8,
        'G': 51,
        'I': 4,
        'L': 0,
        'N': 44,
        'O': 7,
        'P': 15,
        'R': 20,
        'S': 50,
        'T': 5,
        'Z': 0
    }
    return H_dist[n]

Graph_nodes = {
    'A': ['B'],
    'B': ['A','C','R'],
    'C': ['B','E','O','P','T'],
    'D': ['P'],
    'E': ['C','G'],
    'F': ['P'],
    'G': ['E'],
    'I': ['O','Z'],
    'L': ['P'],
    'N': ['O'],
    'O': ['C','I','N'],
    'P': ['C','D','F','L'],
    'R': ['B'],
    'S': ['B'],
    'T': ['C'],
    'Z': ['I']
}

bestFirstAlgo('C')