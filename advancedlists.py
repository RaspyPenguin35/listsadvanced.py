storage=[["Piplup","Pikachu","Lucario","Garchomp","Charizard","Rayquaza"],["Mewtwo","Eevee","Alakazam","Venusaur","Arcanine","Groudon"],["Blastoise","Golem","Pidgeot","Electrabuzz","Muk","Kyogre"]]
print(len(storage))
print(storage[0][1])
print(storage[2][4])
for i in range(0,len(storage)):
    for j in range(0,len(storage[0])):
        print(storage[i][j],end=" ")
    print("\n")