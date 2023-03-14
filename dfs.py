g1={
    0:[1,3],
    1:[0,2,3,5,6],
    2:[1,3,4,5],
    3:[0,1,2,4],
    4:[2,3,6],
    5:[1,2],
    6:[1,4]
}
stack=[]
visited={}
for i in g1:
    visited[i]=False
curr=0
stack.append(0)
visited[0]=True
while len(stack)!=0:
    curr=stack.pop()
    print(curr,end=" ")
    for i in g1[curr]:
        if(visited[i]):
            continue
        visited[i]=True
        stack.append(i)