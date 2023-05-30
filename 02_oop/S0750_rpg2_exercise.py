"""opgave: Objektorienteret rollespil, del 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af del 1.

Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
Dine nye klasser skal have deres egne ekstra metoder og/eller attributter. Måske overskriver de også metoder eller attributter fra klassen Character.

Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Opgradering 1:
Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Opgradering 2:
Lad dine figurer kæmpe mod hinanden 100 gange.
Hold styr på resultaterne.
Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

from colorama import Fore
import random

class Character:
    def __init__(self, name, isdead, max_health, _current_health, power):
        self.name = name
        self.isdead = isdead
        self.max_health = max_health
        self._current_health = _current_health
        self.power = power
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, attackpower = {self.power}"
    def hit(self, Character):
        if self.isdead == True:
            print(Fore.BLUE+ "Can't attack. " +self.name+ " is Dead.")
        elif self.isdead == False:
            Character._current_health -= self.power
            print(Fore.BLUE+ f"hit {Character.name}: {self.power}")
            if Character._current_health <= 0:
                Character.isdead = True
                print(f"{Character.name} died.")


    def get_hit(self, Character):
        self._current_health -= Character.power
        print(Fore.RED+ f"{Character.name} hit {self.name} by : {Character.power}")
        if self._current_health <= 0:
            self.isdead = True
            print(f"{self.name} died.")

class Healer(Character):
    
    def __init__(self, name, isdead, max_health, _current_health, power):
        super().__init__(name, isdead, max_health, _current_health, power)
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, Healpower = {self.power}"
    def heal(self, Character):
        if self.isdead == True:
            print(Fore.BLUE+ "Can't heal. Healer is Dead.")
        else:
            if Character._current_health <= 0:
                Character.isdead = False
                print(Fore.YELLOW+"Revived " +Character.name+"!")
            Character._current_health += self.power

            # can't go above max health
            if Character._current_health > Character.max_health:
                Character._current_health = Character.max_health
        
        print(Fore.GREEN+ f"Healed {Character.name}: {self.power}")

class Hunter(Character):
    def __init__(self, name, isdead, max_health, _current_health, power):
        super().__init__(name, isdead, max_health, _current_health, power)
        self.power = power
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, trap = {self.power}"
    def get_hit(self, Character):
        if self.power == True:
            Character._current_health -= Character.power
            print(Fore.RED+ f"{Character.name} walked into {self.name} trap! And was hit by : {Character.power}")
            self.power = False

        elif self.power == False:
            self._current_health -= Character.power
            print(Fore.RED+ f"{Character.name} hit {self.name} by : {Character.power}")
            if self._current_health <= 0:
                self.isdead = True
                print(f"{self.name} died.")
        
    def trap(self):
        self.power = True
        print(Fore.GREEN+ f"{self.name} activated trap")

class Warlock(Character):
    def __init__(self, name, isdead, max_health, _current_health, power):
        super().__init__(name, isdead, max_health, _current_health, power)
    def __repr__(self):
        return f"{self.name}: health = {self.max_health}/{self._current_health}, darkpower = {self.power}"
    def darkpower(self, Character):
        if self.isdead == True:
            print(Fore.BLUE+ "Can't attack. " +self.name+ " is Dead.")
        elif self.isdead == False:
            self._current_health -= self.power/2
            Character._current_health -= self.power
            print(Fore.BLUE+ f"hit {Character.name}: {self.power}, and himself: {self.power/2}")
            if Character._current_health <= 0:
                Character.isdead = True
                print(f"{Character.name} died.")

        
    
Good_characters = []
you = Character("you", False, 100, 100, 25)
Good_characters.append(you)
Healer = Healer("healer", False, 100, 100, 60)
Good_characters.append(Healer)
Hunter = Hunter("hunter", False, 100, 100, False)
Good_characters.append(Hunter)
Warlock = Warlock("warklock", False, 100, 100, 50)
Good_characters.append(Warlock)

enemy_characters = []
enemy1 = Character("enemy1", False,  100, 100, 15)
enemy_characters.append(enemy1)
enemy2 = Character("enemy2", False,  200, 200, 30)
enemy_characters.append(enemy2)



print("Welcome to RPG Game.")
## def choseenemyattack(): # how to?
allcharacterdead = False
allenemydead = False
while not allcharacterdead:
    deadcharacters = 0
    for Character in Good_characters:
        print(Fore.GREEN + str(Character))
        if Character.isdead:
            deadcharacters += 1
    if deadcharacters == len(Good_characters):
        allcharacterdead = True
        break

    deadcharacters = 0
    for Character in enemy_characters:
        print(Fore.RED + str(Character))
        if Character.isdead:
            deadcharacters += 1
    
    #print("enemy dead: "+str(deadcharacters))
    #print("enemys: "+str(len(enemy_characters)))
    if deadcharacters == len(enemy_characters):
        break
    

    CharacterWrong = True
    while CharacterWrong:
        user_input = input(Fore.WHITE+"1. for Hit Enemy, 2. for Heal Character, 3. for hunter trap, 4. for Warlock darkpower: ")
    
        CharacterWrong = False
        if user_input == "1":
            string = ""
            num = 0
            for Character in enemy_characters:
                string += f"{str(num)}. {Character.name} "
                num += 1
            print(string+": ")
            loop = True
            while loop:

                try:
                    user_input = int(input("who to attack?: "))
                except:
                    print("give falid input")
                else:
                    if user_input < enemy_characters.__len__():
                        loop = False
                    else:
                        print("too large")

                finally:
                    print("The 'try except' is finished")
            you.hit(enemy_characters[int(user_input)])
        elif user_input == "2":
            string = ""
            num = 0
            for Character in Good_characters:
                string += f"{str(num)}. {Character.name} "
                num += 1
            print(string+": ")
            loop = True
            while loop:

                try:
                    user_input = int(input("who to heal?: "))
                except:
                    print("give falid input")
                else:
                    if user_input < Good_characters.__len__():
                        loop = False
                    else:
                        print("too large")

                finally:
                    print("The 'try except' is finished")

            Healer.heal(Good_characters[int(user_input)])

        elif user_input == "3":
            Hunter.trap()
        elif user_input == "4":
            num = 0
            string = ""
            for Character in enemy_characters:
                string += f"{str(num)}. {Character.name} "
                num += 1
            print(string+": ")

            loop = True
            while loop:

                try:
                    user_input = int(input("who to attack?: "))
                except:
                    print("give falid input")
                else:
                    if user_input < enemy_characters.__len__():
                        loop = False
                    else:
                        print("too large")

                finally:
                    print("The 'try except' is finished")

            Warlock.darkpower(enemy_characters[int(user_input)])

        else:
            CharacterWrong = True
            print("try again")
        
    """
    if Healer.isdead == True:
        you.get_hit(enemy1)
    elif you.isdead == True:
        Healer.get_hit(enemy1)
    else:
        rndnum = random.randint(0, 1)
        if rndnum == 0:
            you.get_hit(enemy1)
        elif rndnum == 1:
            Healer.get_hit(enemy1)
    if Healer.isdead and you.isdead:
        bothdead = True
    """
    for Character in enemy_characters:

        if Character.isdead:
            continue
        else:
            rndnum = random.randint(0, len(Good_characters)-1)
            """ 
            if deadcharacters.__contains__(rndnum):
                continue
            else: """
            Good_characters[rndnum].get_hit(Character)
    
if allcharacterdead == False:
    print(Fore.YELLOW+ "You WON!")
elif allcharacterdead == True:
    print(Fore.BLUE+ "You LOST!")
else: 
    print("TIE")
    


