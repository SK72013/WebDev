#Class #Object

class Car:
    Engine = True
    Seat = 6
    Gate = 4
    Batteries =  5
    ACC = True

    def Run(self):
      print("The car is running.")

class Human:
    Legs = 2
    eye = 2
    nose = 1
    mouth = 1
    Hands = 2
    can_walk = True

    def Sleep(self):
       print("Sleeping....")
    def Walk(Self):
       print("Walking...")



BMW = Car()
Rahul = Human()

BMW.Run()
Rahul.Sleep()
Rahul.Walk()

# Ferrari = Car()

# print(BMW.Gate)
# print(BMW.ACC)
# print(BMW.Seat)
# print(Ferrari.Batteries)

# Rahul = Human()
# Rohit = Human()
# Shomopriyo = Human()

# print(Rahul.Legs)
# print(Rohit.can_walk)
# print(Shomopriyo.mouth)


class Animal:
   legs = True
   Nose = 1
   life = True
   ear = 2
   mouth = 1
   eye = 2
   can_walk = True

class Plant:
   life = True
   can_walk = False
   have_leaf = True
   have_branch = True
   need_water = True
   

Lion = Animal()
Rose_Tree = Plant()

print(Lion.eye)
print(Lion.can_walk)
print(Lion.life)
print(Lion.Nose)
print(Lion.legs)

print(Rose_Tree.life)
print(Rose_Tree.have_leaf)
print(Rose_Tree.have_branch)
print(Rose_Tree.need_water)
print(Rose_Tree.can_walk)




