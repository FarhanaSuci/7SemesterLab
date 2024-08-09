goodBye:-
    write('Good Bye! ').
user:-
    write('Enter your Name:'),
    read(Name),
     goodBye,
    format('~w',[Name]).