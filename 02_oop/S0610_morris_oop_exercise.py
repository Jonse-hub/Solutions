"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""



class Miner():
    def __init__(self, sleepiness, thirst, hunger, whisky, gold, done = "mine"):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.done = done
    def __repr__(self):
        return f"gold={self.gold}, sleepiness={self.sleepiness}, thirst={self.thirst}, hunger={self.hunger}, whisky={self.whisky}."
    def option(self, option):
        #self.option = option
        if option == "sleep":
            self._sleep_()
            self.done = "slept"
        elif option == "mine":
            self._mine_()
            self.done = "mined"
        elif option == "eat":
            self._eat_()
            self.done = "ate"
        elif option == "buy_whisky":
            self._buy_whisky()
            self.done = "bought whisky"
        elif option == "drink":
            self._drink_()
            self.done = "drank"


    # protected methods:
    def _sleep_(self):
        self.sleepiness-=10; self.thirst+=1;  self.hunger+=1
    def _mine_(self):
        self.sleepiness+=5;  self.thirst+=5;  self.hunger+=5; self.gold+=5
    def _eat_(self):
        self.sleepiness+=5;  self.thirst-=5;  self.hunger-=20; self.gold-=2
    def _buy_whisky(self):
        self.sleepiness+=5;  self.thirst+=1;  self.hunger+=1;  self.whisky+=1; self.gold-=1
    def _drink_(self):
        self.sleepiness+=5;  self.thirst-=15; self.hunger-=1;  self.whisky-=1

class Morris_The_Miner_Game():
    
    def __init__(self, turn=1):
        self.turn = turn
    #def __repr__(self):
    #    return "turn " + str(self.turn) +": " + Morris.option
    
    def Start(self, strat):
        
        self.turn = 1
        Morris = Miner(0, 0, 0, 0, 0)
        print("""sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0""")
        while self.turn <= 1000 :
            #print("turn: " + str(turn))
            #Morris.option("mine")
            

            if strat == "Most_gold": # strategy
                if self.turn >= 999:
                    Morris.option("mine")
                elif Morris.sleepiness >= 90:
                    Morris.option("sleep")
                elif Morris.hunger >=  95:
                    Morris.option("eat")
                elif Morris.gold >= 1 and Morris.whisky < 1:
                    Morris.option("buy_whisky")
                elif Morris.thirst >= 95:
                    Morris.option("drink")
                else:
                    Morris.option("mine")
            elif strat == "mine_on":
                Morris.option ("mine")
            elif strat == "manual":
                user_input = input("Pick: 1. mine. 2. sleep. 3. eat. 4. buy_whisky, 5. drink: ")
                if user_input == "1":
                    Morris.option("mine")
                elif user_input == "2":
                    Morris.option("sleep")
                elif user_input == "3":
                    Morris.option("eat")
                elif user_input == "4":
                    Morris.option("buy_whisky")
                elif user_input == "5":
                    Morris.option("drink")
                else:
                    print("wrong input, try again")
                


            #region ingen kan komme under 0:
            if Morris.gold < 0:
                Morris.gold = 0
            if Morris.sleepiness < 0:
                Morris.sleepiness = 0
            if Morris.thirst < 0:
                Morris.thirst = 0
            if Morris.hunger < 0:
                Morris.hunger = 0
            if Morris.whisky < 0:
                Morris.whisky = 0
            #  Whisky kan ikke komme over 10
            if Morris.whisky > 10:
                Morris.whisky = 10
            
            #endregion

            print("turn " + str(self.turn) +": " + Morris.done)
            print(Morris)

            # sleepiness, thirst eller hunger kommer over 100, dør Morris.
            if Morris.sleepiness > 100 or Morris.thirst > 100 or Morris.hunger > 100:
                self._Dead()
                break
            self.turn += 1
        print("Game is over!")

    def _Dead():
        print("Morris is dead!")
        
        

Firstgame = Morris_The_Miner_Game()
# Most_gold, mine_on, manual
Firstgame.Start("manual")



#switch kommer i version 3.10
"""match option:
    case "sleep":
        print("")
    case "mine":
        print("")
    case "eat":
        print("")
    case "buy_whisky":
        print("")
    case "drink":
        print("")
        """

