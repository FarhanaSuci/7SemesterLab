
0 is X mod 4,
\+ 0 is X mod 100,
write(X),
write(' is Leap Year').
leapYear(X):-
0 is X mod 400,
write(X),
write(' is Leap Year').
leapYear(X):-
write(X),
write(' is not a Leap Year').
leapYear(X):-