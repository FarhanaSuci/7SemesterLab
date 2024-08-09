edge(a,b).
edge(a,c).
edge(b,d).
edge(c,d).
edge(d,e).
edge(c,e).

path(Start,End,Path):-
  dfs(Start,End,[Start],Path).

dfs(Node,End,Visited,Path):-
     Node=End,
     reverse(Visited,Path).
dfs(Node,End,Visited,Path):-
    edge(Node,Next),
    not(member(Next,Visited)),
    dfs(Next,End,[Next|Visited],Path).