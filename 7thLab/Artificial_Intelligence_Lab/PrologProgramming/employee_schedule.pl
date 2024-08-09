% Define the available employees
employee(john).
employee(jane).
employee(bob).
employee(sara).

% Define the available shifts
shift(morning).
shift(afternoon).
shift(evening).

% Define the available days
day(monday).
day(tuesday).
day(wednesday).
day(thursday).
day(friday).

% Define the employee availability
available(john, monday, morning).
available(john, tuesday, afternoon).
available(john, wednesday, evening).
available(john, thursday, morning).
available(john, friday, afternoon).
available(jane, monday, morning).
available(jane, tuesday, morning).
available(jane, wednesday, afternoon).
available(jane, thursday, evening).
available(jane, friday, morning).
available(bob, monday, afternoon).
available(bob, tuesday, evening).
available(bob, wednesday, morning).
available(bob, thursday, afternoon).
available(bob, friday, evening).
available(sara, monday, evening).
available(sara, tuesday, morning).
available(sara, wednesday, afternoon).
available(sara, thursday, evening).
available(sara, friday, morning).
available(sara, friday, afternoon).

% Define the work requirements
work(morning, 2).
work(afternoon, 3).
work(evening, 2).

% Define the schedule predicate
schedule(Employee, Day, Shift) :-
     
    findall(Employee, available(Employee, Day, Shift),Number),
    employee(Employee),
    day(Day),
    shift(Shift),
    available(Employee, Day, Shift),
    length(Number, NumberCount),
    work(Shift, RequiredShifts),
    NumberCount >= RequiredShifts.

% Define the schedule report predicate
schedule_report(Day) :-
    day(Day),
    write('--- Schedule for '), write(Day), writeln(' ---'),
    schedule(Employee, Day, Shift),
    %day(Day),
    write(Employee), write(' - '), write(Shift), writeln(' shift'),
    fail.