import random
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self, hero):
        for hero in self.heroes:
            self.heroes.append(hero)
    def stats(self):
        for hero in self.heroes:
            kd = hero.skills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random.choice(hero.name)

