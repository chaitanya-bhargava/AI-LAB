s(0,1).
s(0,3).
s(1,0).
s(1,2).
s(1,3).
s(1,5).
s(1,6).
s(2,1).
s(2,3).
s(2,4).
s(2,5).
s(3,0).
s(3,1).
s(3,2).
s(3,4).
s(4,2).
s(4,3).
s(4,6).
s(5,1).
s(5,2).
s(6,1).
s(6,4).
goal(5).
member(X,[X|_]).
member(X,[_|Tail]):-member(X,Tail).

solve(Node,Solution):-
    depthfirst([],Node,Solution).

depthfirst(Path,Node,[Node|Path]):-
    goal(Node).

depthfirst(Path,Node,Sol):-
    s(Node,Node1),
    not(member(Node1,Path)),
    depthfirst([Node|Path],Node1,Sol).

