class Osoba:

    def __init__(self,imie, nazwisko):
        self.imie = imie
        self.naziwsko = nazwisko
        self.poziom_szczescia = 0
        #self.suma_dystansow = 0


class Biegacz:

    def __init__(self,imie, nazwisko):
        self.imie = imie
        self.naziwsko = nazwisko
        #self.poziom_szczescia = 0
        #self.suma_dystansow = 0

    def przedstaw_sie(self):
        return f"{self.imie} {self.naziwsko}"

    def zrob_przebiezke(self, dystans):
        if self.poprzedni_dystans is not None and dystans > self.poprzedni_dystans:
            self.poziom_szczescia += 1
        #self.poprzedni_dystans = dystans

        #ile_pelnych_dziesiatek_poprzednio = self.suma_dystasow // 10
class Strongman:

    def __init__(self,imie, nazwisko):
        super.__init__(imie, nazwisko)
        self.poziom_szczescia = 0
        #self.suma_dystansow = 0

    def przedstaw_sie(self):
        return f"{self.imie} {self.naziwsko}"

    def podnies_ciezar(self, ciezar):
        if ciezar > 100:
            self.poziom_szczescia += 1

    def przedstaw_sie1(self):
        return f'{self.imie} {self.naziwsko} Jestem skomplikowany'


x = Strongman()
przedstaw_sie.x