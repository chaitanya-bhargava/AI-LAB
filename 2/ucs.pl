uniform_cost_search(Start, Goal, Edges, Path, Cost) :-
    empty_queue(EmptyQueue),
    enqueue([(Start, [])], EmptyQueue, Queue),
    ucs_loop(Goal, Edges, Queue, Path, Cost).

ucs_loop(Goal, _, Queue, Path, Cost) :-
    dequeue([(Current, PathSoFar)|_], Queue, _),
    Current = Goal,
    reverse(PathSoFar, Path),
    cost(Path, Cost).
ucs_loop(Goal, Edges, Queue, Path, Cost) :-
    dequeue([(Current, PathSoFar)|Rest], Queue, _),
    \+ Current = Goal,
    expand(Current, PathSoFar, Edges, NewPaths),
    add_paths_to_queue(NewPaths, Queue, NewQueue),
    ucs_loop(Goal, Edges, NewQueue, Path, Cost).

expand(Node, PathSoFar, Edges, NewPaths) :-
    findall((Next, [Next|PathSoFar]),
            (member((Node, Next, Cost), Edges)),
            NextPaths),
    maplist(add_cost_to_path(Cost), NextPaths, NewPaths).

add_cost_to_path(Cost, (Node, Path), (Node, NewPath)) :-
    cost(Path, OldCost),
    NewCost is OldCost + Cost,
    append(Path, [Node], NewPath),
    cost(NewPath, NewCost).

cost(Path, Cost) :-
    maplist(get_cost, Path, Costs),
    sum_list(Costs, Cost).

get_cost(Node, Cost) :-
    member((_, Node, Cost), Edges).

add_paths_to_queue([], Queue, Queue).
add_paths_to_queue([Path|Paths], Queue, NewQueue) :-
    enqueue([Path], Queue, TempQueue),
    add_paths_to_queue(Paths, TempQueue, NewQueue).
