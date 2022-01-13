class Pet:

    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        print(f"{self.name} loves to go for walks")
        return self

    def sound(self):
        print(f"{self.name} says {self.noise}")


class Ninja:
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.sound()

my_treats = ['Big Bone','Bacon',"Beef"]
my_pet_food = ['Good Dog Food','Dog Food']

Jasmin = Pet("Jasmin","Dog",['jump','play'],"Bark Bark")

Valen = Ninja("Adrien","Dion",my_treats,my_pet_food, Jasmin)

Valen.walk()
Valen.feed()
Valen.bathe()
