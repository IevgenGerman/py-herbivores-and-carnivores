class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False):
        if len(Animal.alive) > 0 and all(not isinstance(a, Animal) for a in Animal.alive):
            Animal.alive.clear()

        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def change_health(self, delta_health: int) -> None:
            if isinstance(delta_health, int):
                self.health += delta_health
                if self.health <= 0:
                    Animal.alive.remove(self)


    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Animal) and not herbivore.hidden:
            if isinstance(herbivore, Carnivore):
                pass
        herbivore.health -=50

snake = Carnivore("snake")

cat = Carnivore("cat")
rabbit = Herbivore("rabbit")
print(rabbit.hidden)
rabbit.hide()
print(rabbit.hidden)
rabbit.hide()
print("alive now:", Animal.alive)
print(rabbit.health)
snake.bite(rabbit)

print(rabbit.health)
