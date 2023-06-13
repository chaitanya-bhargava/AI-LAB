from queue import PriorityQueue
g1={
    'A':{'B':4,'C':7},
    'B':{'D':3,'E':6},
    'C':{'F':2},
    'D':{'G':4,'H':2},
    'E':{},
    'F':{'I':4,'J':7},
    'G':{},
    'H':{'L':6},
    'I':{},
    'J':{'K':8},
    'K':{},
    'L':{},
}
parent={}
q=PriorityQueue()
visited={}
distance={}
for i in g1:
    visited[i]=False
    distance[i]=-1
distance['A']=0
curr='A'
q.put((0,'A'))
visited['A']=True
path=[]
while q.qsize()!=0:
    curr=q.get()[1]
    if(curr=='G'):
        print(distance['G'])
        j='G'
        path.append('G')
        while(j!='A'):
            j=parent[j]
            path.append(j)
        path.reverse()
        print(path)
    for i in g1[curr]:
        if(visited[i]):
            continue
        visited[i]=True
        parent[i]=curr
        distance[i]=distance[curr]+g1[curr][i]
        q.put((distance[i],i))