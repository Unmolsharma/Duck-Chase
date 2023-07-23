import Duck

myDuck = Duck.Duck("Donald", 2, "Mallard")
myDuck.quack()
print (myDuck.name + "quacked")
print(myDuck.weight, myDuck.species)
myDuck.quack(5)

anotherDuck = Duck.Duck("Daisy", 1.5, "Marble")
print (anotherDuck.name, anotherDuck.weight, anotherDuck.species)


