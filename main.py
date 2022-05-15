  class Library(object):
    def __init__(self):
        self.ksiazki = []
        self.egzemplarze=[]
        self.czytelnicy= {}
        self.tytuly=[]
        self.komunikaty=[]

    def addKsiazka(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def addEgzemplarz(self,egzemplarz):
        egzemplarz1 = list(egzemplarz)
        if egzemplarz1[1:3] in self.ksiazki:
            self.egzemplarze.append(egzemplarz1[1:3])
            self.tytuly.append(egzemplarz1[1])
            self.komunikaty.append('True')
        else:
            library.addKsiazka(egzemplarz1[1:3])
            self.egzemplarze.append(egzemplarz1[1:3])
            self.tytuly.append(egzemplarz1[1])
            self.komunikaty.append('True')

    def liczenie(self):
        listafinal=[]
        listasort=[]
        for ksiazka in self.ksiazki:
            a = self.egzemplarze.count(ksiazka)
            ksiazka1 = [ksiazka[0], ksiazka[1], a]
            listafinal.append(ksiazka1)
        listasort = sorted(listafinal, key=lambda x: x[0])
        for element in listasort:
            element1 = (element[0], element[1], element[2])
            print(element1)

    def czytelnik(self, nazwisko, tytul):
        if nazwisko in self.czytelnicy:
            if len(self.czytelnicy[nazwisko]) < 3 and tytul not in self.czytelnicy[nazwisko]:
                self.czytelnicy[nazwisko].append(tytul)
                self.tytuly.remove(tytul)
                self.komunikaty.append('True')
            else:
                self.komunikaty.append('False')
        else:
            self.czytelnicy[nazwisko]=[]
            self.czytelnicy[nazwisko].append(tytul)
            self.tytuly.remove(tytul)
            self.komunikaty.append('True')

    def wypozycz(self,nazwisko,tytul):
        if tytul in self.tytuly:
            self.czytelnik(nazwisko,tytul)
        else:
            self.komunikaty.append('False')

    def oddaj(self,nazwisko,tytul):
        if nazwisko in self.czytelnicy:
            if tytul in self.czytelnicy[nazwisko]:
                self.czytelnicy[nazwisko].remove(tytul)
                self.tytuly.append(tytul)
                self.komunikaty.append('True')
            else:
                self.komunikaty.append('False')

        else:
            self.komunikaty.append('False')

    def drukuj(self):
        for komunikat in self.komunikaty:
            print(komunikat)

library = Library()

k = int(input())

for i in range(0, k):
    wejscie = eval(input())
    if wejscie[0] == "dodaj":
        library.addEgzemplarz(wejscie)
    elif wejscie[0] == "wypozycz":
        library.wypozycz(wejscie[1],wejscie[2])
    elif wejscie[0] == "oddaj":
        library.oddaj(wejscie[1],wejscie[2])

library.drukuj()

