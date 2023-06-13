move(a, b).
move(a, d).
move(a, c).
move(b, e).
move(b, c).
move(b, f).
move(c, f).
move(d, g).
move(e, h).

goal(g).

dls(X,X,[X],L):-
    L > 0, goal(X).

dls(X,Y,[A|P],L):-
    L > 0, goal(Y),
    move(X,Z), % move from X to Z
    L1 is L - 1,
    dls(Z,Y,P,L1). % recursively search from Z to Y with remaining depth limit L1
