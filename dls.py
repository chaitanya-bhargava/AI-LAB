g1={
    'A':['B','C','D'],
    'B':['A','C','E','F'],
    'C':['A','B','F'],
    'D':['A','G'],
    'E':['B','H'],
    'F':['B','C'],
    'G':['D'],
    'H':['E']
}
depthlimit=2
depth={}
stack=[]
visited={}
for i in g1:
    visited[i]=False
    depth[i]=-1
curr='A'
depth['A']=0
stack.append('A')
visited['A']=True
while len(stack)!=0:
    curr=stack.pop()
    print(curr,end=" ")
    for i in g1[curr]:
        if(visited[i]):
            continue
        if(depth[curr]+1>depthlimit):
            continue
        visited[i]=True
        depth[i]=depth[curr]+1
        stack.append(i)