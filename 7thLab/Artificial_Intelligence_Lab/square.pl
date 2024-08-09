square(Number,Square):-
    write('Enter the number '),
    read(Number),
    Square is Number*Number,
    format('Square is ~w',Square).