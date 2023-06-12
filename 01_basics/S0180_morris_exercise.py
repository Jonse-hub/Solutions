"""
Opgave "Morris the Miner":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

sleepiness = 0
thirst = 0
hunger = 0
whisky = 0
gold = 0

turn = 1

while turn <= 1000 :
    #print("turn: " + str(turn))
    option = "mine"
    if turn >= 999:
        option = "mine"
    elif sleepiness >= 90:
        option = "sleep"
    elif hunger >=  95:
        option = "eat"
    elif gold >= 1 and whisky < 1:
        option = "buy_whisky"
    elif thirst >= 95:
        option = "drink"
    else:
        option = "mine"

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
            print("")"""

    if option == "sleep":
        sleepiness-=10; thirst+=1;  hunger+=1
        print("turn " + str(turn) +": slept")
    elif option == "mine":
        sleepiness+=5;  thirst+=5;  hunger+=5; gold+=5
        print("turn " + str(turn) +": mined")
    elif option == "eat":
        sleepiness+=5;  thirst-=5;  hunger-=20; gold-=2
        print("turn " + str(turn) +": ate")
    elif option == "buy_whisky":
        sleepiness+=5;  thirst+=1;  hunger+=1;  whisky+=1; gold-=1
        print("turn " + str(turn) +": bought whisky")
    elif option == "drink":
        sleepiness+=5;  thirst-=15; hunger-=1;  whisky-=1
        print("turn " + str(turn) +": drank")
    #ingen kan komme under 0:
    if gold < 0:
        gold = 0
    if sleepiness < 0:
        sleepiness = 0
    if thirst < 0:
        thirst = 0
    if hunger < 0:
        hunger = 0
    if whisky < 0:
        whisky = 0
    #  Whisky kan ikke komme over 10
    if whisky > 10:
        whisky = 10

    print(f"gold={gold}, sleepiness={sleepiness}, thirst={thirst}, hunger={hunger}, whisky={whisky}.")

    # sleepiness, thirst eller hunger kommer over 100, dør Morris.
    if sleepiness > 100 or thirst > 100 or hunger > 100:
        print("Morris is dead!")
        break
    
    turn += 1

