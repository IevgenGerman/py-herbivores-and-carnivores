class Animal:
    alive = []

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
            self.health += delta_health
            if self.health <= 0:
                Animal.alive.remove(self)

    def __iadd__(self, other: int) -> "Animal":
        if isinstance(other, int):
            self.change_health(other)
            return self

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.change_health(-50)

    def __isub__(self, other: int) -> "Animal":
        if isinstance(other, int):
            self.change_health(-other)
            return self



snake = Carnivore("snake")

cat = Carnivore("cat")
rabbit = Herbivore("rabbit")
print(rabbit.hidden)
rabbit.hide()
print(rabbit.hidden)
print("alive now:", Animal.alive)
print(rabbit.health)
snake.bite(rabbit)

print(rabbit.health)
