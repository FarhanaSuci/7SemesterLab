mammal(bear,1000,pagol).
mammal(dolphin,4000,suci).
mammal(dear,678,pagol).
mammal(dog,5675,pagol).
mammal(cat,4000,pagol).
mammal(turtle,4000,suci).
cal(Mammals):-findall(Mammal,mammal(Mammal,4000,suci),Mammals),
              write(Mammals).
