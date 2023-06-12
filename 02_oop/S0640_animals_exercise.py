"""
Opgave "Animals"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop- og rpg1-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random

rndnum = random.randrange(2) # 0-1

class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"Animal: {self.name=} {self.sound=} {self.height=} {self.weight=} {self.legs=} {self.female=}" 
    def make_noise(self):
        print(self.sound)
class Dog(Animal):
    def wag_tail(self):
        print(f"Hunden {self.name} vifter med sin {str(self.height/4)} lange hale")

    @staticmethod
    def mate(mother, father):
        if mother.female and not father.female:
            rndnum = random.randrange(2)
            female = rndnum == 1
            child = Dog(mother.name+" & "+father.name+" child", father.sound, (father.height+mother.height)/2, (mother.weight+father.weight)/2, father.legs, female)
            print(child)



    
animal1 = Animal("George", "sound", 15, 16, 4, True)

print(animal1)

hund1 = Dog("Bobby", "wuff", 50, 44, 4, False)
hund2 = Dog("Sanne", "wuff", 25, 20, 4, True)
print(hund1)
hund1.wag_tail()




hund1.mate(hund2, hund1)

print(rndnum)



