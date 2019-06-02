# Project lab-data-vikings
import random

# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name= name

    def receive_damage(self,damage):
        super().receive_damage(damage)
        if (self.health) > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self,damage):
        super().receive_damage(damage)
        if (self.health) > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, viking):
        self.viking_army.append(viking)

    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def vicking_attack(self):
        saxon = random.choice(self.saxon_army)
        viking = random.choice(self.viking_army)
        saxon.receive_damage(viking.attack())
        if self.saxon.health < 0:
            self.saxon_army.remove(saxon)

        return saxon.receive_damage(viking.strength)

    def saxon_attack(self):
        viking = random.choice(self.viking_army)
        saxon = random.choice(self.saxon_army)
        viking.receive_damage(saxon.attack())
        if self.viking.health < 0:
            self.viking_army.remove(viking)

        return viking.receive_damage(saxon.strength)

    def showStatus(self):
        if self.saxon_army.size() == 0:
            return "Vikings have won the war of the century!"
        if self.viking_army.size() == 0:
            return "Saxons have fought for their lives and survive another day..."
        if self.saxon_army.size() == 1 and self.viking_army.size() == 1:
            return "Vikings and Saxons are still in the thick of battle."





















