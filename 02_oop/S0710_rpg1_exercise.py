"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en privat attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
from colorama import Fore
import random

class Character:
    def __init__(self, name, isdead, max_health, _current_health, attackpower):
        self.name = name
        self.isdead = isdead
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, attackpower = {self.attackpower}"
    def hit(self, Character):
        if self.isdead == True:
            print(Fore.BLUE+ "Can't attack. " +self.name+ " is Dead.")
        elif self.isdead == False:
            Character._current_health -= self.attackpower
            print(Fore.BLUE+ f"hit {Character.name}: {self.attackpower}")
            if Character._current_health <= 0:
                Character.isdead = True
                print(f"{Character.name} died.")


    def get_hit(self, Character):
        self._current_health -= Character.attackpower
        print(Fore.RED+ f"{Character.name} hit {self.name} by : {Character.attackpower}")
        if self._current_health <= 0:
            self.isdead = True
            print(f"{self.name} died.")

class Healer(Character):
    
    def __init__(self, name, isdead, max_health, _current_health, attackpower, healpower):
        super().__init__(name, isdead, max_health, _current_health, attackpower)
        self.healpower = healpower
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, attackpower = {self.attackpower} Healpower = {self.healpower}"
    def heal(self, Character):
        if self.isdead == True:
            print(Fore.BLUE+ "Can't heal. Healer is Dead.")
        else:
            if Character._current_health <= 0:
                Character.isdead = False
                print(Fore.YELLOW+"Revived " +Character.name+"!")
            Character._current_health += self.healpower

            # can't go above max health
            if Character._current_health > Character.max_health:
                Character._current_health = Character.max_health
        
        print(Fore.GREEN+ f"Healed {Character.name}: {self.healpower}")
        
    

you = Character("you", False, 100, 100, 50)
Healer = Healer("healer", False, 100, 100, 25, 30)

enemy = Character("enemy", False,  1000, 1000, 15)

bothdead = False

print("Welcome to RPG Game.")
print(Fore.GREEN+ str(you))
print(Fore.GREEN+ str(Healer))
print(Fore.RED+ str(enemy))

while (not enemy.isdead and not bothdead):
    user_input = input(Fore.WHITE+"1. for Hit Enemy, 2. for Heal You, 3. for heal Healer: ")
    if user_input == "1":
        if you.isdead == True:
            Healer.hit(enemy)
        elif you.isdead == False:
            you.hit(enemy)
    elif user_input == "2":
        Healer.heal(you)
    elif user_input == "3":
        Healer.heal(Healer)
    else:
        print(Fore.RED+ "false input.")
    
    if Healer.isdead == True:
        you.get_hit(enemy)
    elif you.isdead == True:
        Healer.get_hit(enemy)
    else:
        rndnum = random.randint(0, 1)
        if rndnum == 0:
            you.get_hit(enemy)
        elif rndnum == 1:
            Healer.get_hit(enemy)
    if Healer.isdead and you.isdead:
        bothdead = True
    print(Fore.GREEN+ str(you))
    print(Fore.GREEN+ str(Healer))
    print(Fore.RED+ str(enemy))

if enemy.isdead == True:
    print(Fore.YELLOW+ "You WON!")
else: 
    print(Fore.BLUE+ "You LOST!")




