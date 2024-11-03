check_number(X):-
    X>0,
    write(X),nl,
    write('The number is Positive').
check_number(X):-
    X<0,
    write(X),nl,
     write('The number is Negative').
þ:-
    X=0,
    write(X),nl,
     write('The number is Zero').
