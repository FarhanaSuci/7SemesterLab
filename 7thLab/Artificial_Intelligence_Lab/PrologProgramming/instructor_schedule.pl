course(bangla).
course(english).
course(math).
course(islam).
course(science).
course(generalKnowledge).

timeSlot(sunday,9).
timeSlot(sunday,11).
timeSlot(monday,9).
timeSlot(monday,11).
timeSlot(tuesday,9).
timeSlot(tuesday,11).
timeSlot(thrusday,9).
timeslot(thrusday,11).

instructor(rahim).
instructor(karim).
instructor(suci).
instructor(ajmir).
instructor(sumi).
instructor(sruti).

schedule(Instructor,Course,Day,Time):-
course(Course),
instructor(Instructor),
timeSlot(Day,Time),fail.

