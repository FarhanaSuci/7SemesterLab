number_(N):-
    N>0,
    write(N),
    write(' is positive Number').
number_(N):-
    N<0,
    write(N),
    write(' is negative Number').
number_(N):-
    N=0,
    write(N),
    write(' is equal to zero').