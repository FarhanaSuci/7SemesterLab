artist(bistri).
artist(habiba).
artist(fatema).
artist(sweety).
artist(taharima).
genre(rock).
genre(pop).
genre(country).
genre(rap).
like(suci,bistri,rock).
like(suci,bistri,rap).
like(suci,bistri,country).
like(ajmir,taharima,rock).
like(ajmir,fatema,country).
like(ajmir,habiba,rap).
like(ajmir,bistri,country).
like(sumi,bistri,rock).
like(sumi,habiba,pop).
like(sumi,sweety,country).
like(sumi,taharima,rap).
like(sruti,bistri,rock).
like(sruti,fatema,country).
like(sruti,taharima,pop).
like(sruti,sweety,rap).
like(sruti,bistri,country).
recommend(User,Artist):-
    like(User,_,Genre),
    artist(Artist),
    genre(Genre),
    like(User,Artist,Genre).
% writeln() means oi line er pore new line nibe not from writeln
recommend_report(User):-
    write('Recommendations for '),writeln(User),writeln(-------------------------------),
    recommend(User,Artist),
    write(Artist),
    writeln(' Recommended'),fail.
    