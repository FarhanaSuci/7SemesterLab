% Define destinations and their corresponding costs
destination(paris, 1000).
destination(london, 1200).
destination(tokyo, 1500).
destination(new_york, 1300).
destination(los_angeles, 1100).
destination(sydney, 1400).

% Define activities and their corresponding costs
activity(sightseeing, 50).
activity(shopping, 100).
activity(food_tasting, 75).
activity(beach, 25).
activity(hiking, 30).
activity(museum, 40).

% Define the budget predicate

% Define the recommend predicate
recommend(Destination, Activity) :-
    destination(Destination, Cost),
    activity(Activity, ActivityCost),
    TotalCost is Cost + ActivityCost,
    write('Enter your budget: '),
    read(Budget),
    TotalCost =< Budget.
