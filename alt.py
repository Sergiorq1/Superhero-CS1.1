"""
Ignore this code, this is hero.py prior to adding armor, abilities, and different mechanics
"""
import random
class Hero:
    def __init__(self, name, starting_health=100, attack=50):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.attack = attack
    def fight(self, opponent):
        print("The battle with your opponent has started! \nGuess the right number, you hit. Guess wrong, you get hit ")
        pick_either = [1,2]
        while self.current_health > 0 and opponent.current_health > 0:
            random_num = random.choice(pick_either)
            choosen_number = int(input("Choose either 1 or 2"))
            if choosen_number == random_num:
                opponent.current_health -= self.attack
                print(f"{opponent.name}'s health is  {opponent.current_health}. Good guess!")
            elif choosen_number != random_num:
                self.current_health -= opponent.attack
                print(f"{self.name}'s health is {self.current_health}. Not good guess")
            if self.current_health <= 0:
                print(f"{opponent.name} is the winner!!!") 
            elif opponent.current_health <= 0:
                print(f"{self.name} is the winner!!!")

hero1 = Hero("Stonks Man", 200)
hero2 = Hero("Pikachu", 200)
# print(my_hero.name)
# print(my_hero.current_health)
hero1.fight(hero2)