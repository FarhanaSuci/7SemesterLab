%employee, shift,day,available,work
employee(rahim).
employee(karim).
employee(suci).
employee(sruti).
employee(ajmir).
employee(sumi).

shift(morning).
shift(afternoon).
shift(night).
day(sunday).
day(monday).
day(tuesday).
day(thrusday).

available(rahim,sunday,morning).
available(rahim,monday,night).
available(rahim,thrusday,afternoon).

available(karim,monday,morning).
available(karim,sunday,night).
available(karim,thrusday,afternoon).

available(sruti,sunday,morning).
available(sruti,monday,night).
available(sruti,thrusday,afternoon).

available(ajmir,tuesday,morning).
available(ajmir,sunday,night).
available(ajmir,thrusday,afternoon).

available(sumi,tuesday,morning).
available(sumi,sunday,night).
available(sumi,thrusday,afternoon).

work(morning,2).
work(afternoon,3).
work(night,2).

schedule(Employee,Day,Shift):-
    findall(Employee,available(Employee,Day,Shift),List),
    %write(List),
    employee(Employee),
    day(Day),
    shift(Shift),
    available(Employee,Day,Shift),
    length(List,Num),
    work(Shift,Require),
    Num>=Require.
schedule_report(Day):-
    day(Day),
    writeln('     '),
     writeln(Day),
    writeln('---------------------'),
    schedule(Employee,Day,Shift),
    write(Employee),
    write('->'),
    writeln(Shift),fail.
    