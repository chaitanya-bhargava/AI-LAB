other_bank(e, w).
other_bank(w,e).

% farmer, lion, goat, grass
move([X, X, Goat, Grass], lion, [Y,Y, Goat, Grass]):- other_bank(X,Y).
move([X, Lion,X, Grass], goat, [Y, Lion, Y, Grass]):- other_bank(X,Y).
move([X, Lion, Goat, X], grass, [Y, Lion, Goat, Y]):- other_bank(X,Y).
move([X, Lion, Goat, Grass], nothing, [Y, Lion, Goat, Grass]):- other_bank(X, Y).

safety_check(X, X,_).
safety_check(X,_,X).
safe_status([Farmer, Lion, Goat, Grass]):-
	safety_check(Farmer, Goat, Lion),
	safety_check(Farmer, Goat, Grass).

solution([e,e,e,e], []).
solution(Config, [Move|OtherMoves]):-
	move(Config, Move, NextConfig),
	safe_status(NextConfig),
	solution(NextConfig, OtherMoves).

% length(X,7), solution([w,w,w,w],X).