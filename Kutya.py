import random


class Kutya:    # osztály

    def __init__(self, nev, nem, faj, mar_mag, suly):   # osztály konstruktora
        self.nev = nev  # osztály saját változói = adattagok
        self.nem = nem  # publikus adattagok
        self.faj = faj
        self.mar_mag = mar_mag
        self.suly = suly

    # Ez a metódus hívódik meg a print utasításra. Itt írhatunk ki infokat az osztálypéldányról.
    def __str__(self):
        return f"{self.nev} ({self.nem}, {self.faj}, {self.mar_mag}, {self.suly})"

    def tev(self):
        x = int(random.random() * 3)
        if x == 0:
            x = "A kutya ugat."
        elif x == 1:
            x = "A kutya alszik."
        else:
            x = "A kutya játszik."
        return x


"""
        harap(x)


    def harap(x):
        if x == "A kutya ugat.":
            print("A kutya harap")
"""
