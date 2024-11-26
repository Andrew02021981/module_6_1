class Animal:
    alive = True
    fed = False
    name = None

    def __init__(self, name):
        self.name = name

    # def eat(self, food):
    #     self.food = food
    #     if self.food is Fruit:
    #         print(f'{self.name} съел {food.name}', Animal.fed == True)
    #     elif self.food is Flower:
    #         print(f'{self.name} не стал есть {food.name}', Animal.alive == False)

class Plant:
    edible = False
    name = None
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        self.food = food
        if self.food is Fruit:
            print(f'{self.name} съел {food.name}', Animal.fed == True)
        elif self.food is Flower:
            print(f'{self.name} не стал есть {food.name}', Animal.alive == False)

class Predator(Animal):
    def eat(self, food):
        self.food = food
        if self.food is Fruit:
            print(f'{self.name} съел {food.name}', Animal.fed == True)
        elif self.food is Flower:
            print(f'{self.name} не стал есть {food.name}', Animal.alive == False)

class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)