g1={
    1:[4],
    2:[4],
    3:[6],
    4:[1,2,8],
    5:[6],
    6:[3,5,8],
    8:[4,6,9],
    9:[8,10],
    10:[9,11,12],
    11:[10,13,14],
    12:[10,15,16],
    13:[11],
    14:[11],
    15:[12],
    16:[16]
}
parent={}
visitedfront={}
visitedback={}
queuefront=[]
queueback=[]
for i in g1:
    visitedfront[i]=False
    visitedback[i]=False
front=1
back=16
queuefront.append(1)
queueback.append(16)
visitedfront[1]=True
visitedback[16]=True
while len(queueback)!=0:
    back=queueback.pop(0)
    if(back==1):
        break
    for j in g1[back]:
        if(visitedback[j]):
            continue
        visitedback[j]=True
        parent[j]=back
        queueback.append(j)
while len(queuefront)!=0:
    front=queuefront.pop(0)
    if(front==16):
        break
    for j in g1[front]:
        if(visitedfront[j]):
            continue
        visitedfront[j]=True
        parent[j]=front
        queuefront.append(j)
for i in g1:
    if(visitedback[i]==1 & visitedfront[i]==1):
        path = []
        path.append(i)
        j = i
         
        while j != 1:
            path.append(parent[j])
            j = parent[j]
             
        path = path[::-1]
        j = i
         
        while j != 16:
            path.append(parent[j])
            j = parent[j]
             
        print("*****Path*****")
        path = list(map(str, path))
         
        print(' '.join(path))