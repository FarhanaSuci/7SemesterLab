recommend(Budget):-
    Budget >= 1000,
    write('You have to choose Chittagong').
recommend(Budget):-
    Budget >= 2000,
    write('You have to choose Dhaka').
recommend(Budget):-
    Budget >= 3000,
    write('You have to choose Noakhali').
recommend(Budget):-
    Budget >= 4000,
    write('You have to choose Barishal').
    