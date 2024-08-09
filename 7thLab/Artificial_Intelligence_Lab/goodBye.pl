good_bye:-
write('Good Bye ').
user:-
write('Enter your name: '),
read(Name),
good_bye,
format('~w',[Name]).