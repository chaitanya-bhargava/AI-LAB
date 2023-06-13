# Python3 program to implement traveling salesman 
# problem using naive approach. 

from sys import maxsize 

from itertools import permutations

V = 7
 
# implementation of traveling Salesman Problem 

def travellingSalesmanProblem(graph, s): 
 

    # store all vertex apart from source vertex 

    vertex = [] 

    for i in range(V): 

        if i != s: 

            vertex.append(i) 
 

    # store minimum weight Hamiltonian Cycle 

    min_path = maxsize 

    next_permutation=permutations(vertex)

    for i in next_permutation:
 

        # store current Path weight(cost) 

        current_pathweight = 0
 

        # compute current path weight 

        k = s 

        for j in i: 

            current_pathweight += graph[k][j] 

            k = j 

        current_pathweight += graph[k][s] 
 

        # update minimum 

        min_path = min(min_path, current_pathweight) 

         

    return min_path 
 
 
# Driver Code 

if __name__ == "__main__": 
 

    # matrix representation of graph 

    graph = [[0, 12, 10, maxsize,maxsize,maxsize,12], 
            [12, 0, 8, 12,maxsize,maxsize,maxsize], 
            [10, 8, 0, 11,3,maxsize,9], 
            [maxsize, 12, 11, 0,11,10,maxsize], 
            [maxsize, maxsize, 3, 11,0,6,7], 
            [maxsize,maxsize,maxsize,10,6,0,9], 
            [12, maxsize, 9, maxsize,7,9,0]] 

    s = 0

    print(travellingSalesmanProblem(graph, s))