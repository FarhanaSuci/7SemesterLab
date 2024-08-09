even_odd(X):-
    0 is X mod 2,
    write(X),
    write(' is a Even Number'),nl.
even_odd(X):-
    write(X),
    1 is X mod 2,
    write(' is a Odd Number').