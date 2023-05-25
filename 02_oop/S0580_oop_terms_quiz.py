"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attributå
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building: # class
    def __init__(self, area, floors, value): # constructer
        self.area = area # constructers value
        self.floors = floors
        self._value = value

    def renovate(self): # method of class
        print("Installing an extra bathroom...")
        self._adjust_value(10) # call building method

    def _adjust_value(self, percentage): # hidden/protected method, not to be called outside of class
        self._value *= 1 + (percentage / 100)
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building): # class based on Building

    def renovate(self): # changed renovate method of building to be different on skyscraper
        print("Installing a faster elevator.")
        self._adjust_value(6)


small_house = Building(160, 2, 200000) # call building class with self constructer values
skyscraper = Skyscraper(5000, 25, 10000000)

for building in [small_house, skyscraper]: # for loop for small_house and skyscraper
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.') # output with f-string
    building.renovate() # calls method
