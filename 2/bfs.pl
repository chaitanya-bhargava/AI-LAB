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

solve(Start,Solution):-
    breadthfirst([[Start]],Solution).

breadthfirst([[Node|Path]|_],[Node|Path]):-
    goal(Node).

breadthfirst([Path|Paths],Solution):-
    extend(Path,NewPaths),conc(Paths,NewPaths,Paths1),breadthfirst(Paths1,Solution).

extend([Node|Path],NewPaths):-
    bagof([NewNode,Node|Path],(s(Node,NewNode),not(member(NewNode,[Node|Path]))),NewPaths),!.

extend(_,[]).

conc([],L,L).
conc([X|L1],L2,[X|L3]) :-
    conc(L1,L2,L3).

