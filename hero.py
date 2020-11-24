import random
from ability import Ability
from armor import Armor
from weapon import Weapon
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        # self.attack = attack
        self.abilities = list()
        self.armor = list()
        self.death = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
        
    def add_armor(self, armor):
        self.armor.append(armor)
    
    def defend(self, damage_amt):
        total_block = 0
        for blocke in self.armor:
            total_block += blocke.block()
        return total_block
        # Might  not be right
    def take_damage(self, damage):
        if self.defend(damage) < damage:
            real_damage = damage - self.defend(damage)
            self.current_health -= real_damage
            print(f"Damage recieved: {real_damage}.")
        elif self.defend(damage) >= damage:
            real_damage = 0
    def is_alive(self):
        if self.current_health <= 0:
            return False
        elif self.current_health > 0:
            return True
    #Come back to
    def add_weapon(self, weapon):
        total_damage = 0
        for weapon in self.abilities:
            total_damage += weapon.attack()
        return total_damage
    def add_kill(self, num_kills):
        self.kills += num_kills
    def add_death(self, num_deaths):
        self.death += num_deaths

            

    # def fight(self, opponent):
    #     print("The battle with your opponent has started! \nGuess the right number, you hit. Guess wrong, you get hit ")
    #     pick_either = [1,2]
    #     while self.current_health > 0 and opponent.current_health > 0:
    #         random_num = random.choice(pick_either)
    #         choosen_number = int(input("Choose either 1 or 2"))
    #         if choosen_number == random_num:
    #             opponent.current_health -= self.attack
    #             print(f"{opponent.name}'s health is  {opponent.current_health}. Good guess!")
    #         elif choosen_number != random_num:
    #             self.current_health -= opponent.attack
    #             print(f"{self.name}'s health is {self.current_health}. Not good guess")
    #         if self.current_health <= 0:
    #             print(f"{opponent.name} is the winner!!!") 
    #         elif opponent.current_health <= 0:
                # print(f"{self.name} is the winner!!!")

hero1 = Hero("Stonks Man", 200)
hero2 = Hero("Pikachu", 200)
# hero1.fight(hero2)

# if __name__ == "__main__":
#     # ability = Ability("Smack", 50)
#     # another_ability = Ability("Yeetus", 90)
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.is_alive())
#     hero.take_damage(1000000)
#     print(hero.is_alive())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
