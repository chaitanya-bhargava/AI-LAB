# state represents ([No. of missionaries on the left bank, no. of cannibals on the left bank, boat present or no (1/0)],
#[No. of missionaries on the right bank, no. of cannibals on the right bank, boat present or no (1/0)])
initial_state=([3,3,1],[0,0,0])
goal_state=([0,0,0],[3,3,1])
visited=[]
operations=[(2,0),(1,1),(0,2),(1,0),(0,1)]
def isValid(state):
    return not( state[0][0]<0 or state[1][0]<0 or state[0][0]+state[1][0]>3 or
                state[0][1]<0 or state[1][1]<0 or state[0][1]+state[1][1]>3 or
                (state[0][0]!=0 and state[0][0]<state[0][1]) or (state[1][0]!=0 and state[1][0]<state[1][1]))
def operate(state, operation, move):
    new_state=([],[])
    if move==1:
        new_state[0].append(state[0][0]-operation[0])
        new_state[0].append(state[0][1]-operation[1])
        new_state[0].append(0)
        new_state[1].append(state[1][0]+operation[0])
        new_state[1].append(state[1][1]+operation[1])
        new_state[1].append(1)
    else:
        new_state[0].append(state[0][0]+operation[0])
        new_state[0].append(state[0][1]+operation[1])
        new_state[0].append(1)
        new_state[1].append(state[1][0]-operation[0])
        new_state[1].append(state[1][1]-operation[1])
        new_state[1].append(0)
    return new_state
    
def func(state,move,path):
    path.append(state)
    visited.append(state)
    if state==goal_state:
        return path
    for operation in operations:
        new_state=operate(state,operation,move)
        if new_state in visited or not isValid(new_state):
            continue
        p=func(new_state,-1*move,path)
        if p!=[]:
            return p
        else:
            path.pop()
    return []
for state in func(initial_state,1,[]):
    print(state)
