#q1_sg5_a1_PINATUBO_ESDRELON

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(self.name, "has entered the battle with", self.hp, "HP!")

    def take_damage(self, amount):
        self.hp -= amount
        print(self.name, "took", amount, "damage!")

# Make arthur and morgana
arthur = Hero("Arthur", 67)
morgana = Hero("Morgana", 67)

# Make Arthur take 10 damage
arthur.take_damage(10)

# Print both their HPs
print("Arthur HP:", arthur.hp)
print("Morgana HP:", morgana.hp)