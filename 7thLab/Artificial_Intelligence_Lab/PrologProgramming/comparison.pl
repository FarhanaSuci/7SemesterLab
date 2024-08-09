comparison(X,Y):-
    X>Y,
    write(X),
    write(' is greater than '),
    write(Y),
    nl.
comparison(X,Y):-
    X<Y,
    write(X),
    write(' is smaller than  '),
    write(Y),
    nl.
comparison(X,Y):-
    X=Y,
    write(X),
    write(' and '),
    write(Y),
    write(' are Equal'),
    nl.