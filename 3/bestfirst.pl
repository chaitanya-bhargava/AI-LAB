% Define the graph
graph(a, [(b, 4), (c, 2)]).
graph(b, [(d, 5), (e, 12)]).
graph(c, [(d, 2), (f, 3)]).
graph(d, [(e, 3), (g, 6)]).
graph(e, [(g, 7)]).
graph(f, [(g, 3)]).

% Define the heuristic function
heuristic(a, 14).
heuristic(b, 12).
heuristic(c, 11).
heuristic(d, 7).
heuristic(e, 4).
heuristic(f, 11).
heuristic(g, 0).

% Define the Best-First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search_helper([(0, [(Start, 0)])], Goal, RevPath),
    reverse(RevPath, Path).

best_first_search_helper([(_, [(Goal, Cost) | Path]) | _], Goal, [(Goal, Cost) | Path]).
best_first_search_helper([(_, [(Current, CurrentCost) | Path]) | Queue], Goal, FinalPath) :-
    findall((NewH, [(Next, Cost), (Current, CurrentCost) | Path]),
            (graph(Current, Edges), member((Next, Cost), Edges),
            heuristic(Next, NewH)),
            Children),
    append(Queue, Children, NewQueue),
    sort(NewQueue, SortedQueue),
    best_first_search_helper(SortedQueue, Goal, FinalPath).