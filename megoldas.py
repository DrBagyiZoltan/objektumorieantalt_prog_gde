from abc import ABC
from datetime import datetime, date


class Szoba(ABC):
    def __init__(self):
        self.foglalasok = [Foglalas]

    def foglaltsag_ellenorzes(self, szobaszam, foglalas_datuma):
        for foglalas in self.foglalasok:
            if (foglalas.foglalas_datuma == foglalas_datuma) & (foglalas.szobaszam == szobaszam):
                return False
            return True

    def foglal(self, szobaszam, foglalas_datuma):
        if self.foglaltsag_ellenorzes(szobaszam, foglalas_datuma):
            self.foglalasok.append(Foglalas(szobaszam, foglalas_datuma))
            return f"A {szobaszam} számú szoba az alábbi dátumra ezennel le lett foglalva: {foglalas_datuma}"
        else:
            return f"A {szobaszam} számú szoba az alábbi dátumra foglalt: {foglalas_datuma}"
        pass


class Foglalas:

    def __init__(self, szobaszam, foglalas_datuma):
        self.szobaszam = szobaszam
        self.foglalas_datuma = foglalas_datuma


class EgyagyasSzoba(Szoba):
    def __init__(self):
        self.szobaszam = 1
        self.ar = 100000
        self.foglalasok = []


class KetagyasSzoba(Szoba):
    def __init__(self):
        self.szobaszam = 2
        self.ar = 20000
        self.foglalasok = []


class Szalloda:
    def __init__(self):
        self.szobak = []

    def szoba_letrehozas(self, szoba: Szoba):
        self.szobak.append(szoba)

    def betoltes(self):
        self.szoba_letrehozas(EgyagyasSzoba())
        self.szoba_letrehozas(KetagyasSzoba())

    def lemondas(self):
        pass

    def foglalasok(self):
        pass

    def foglal_szobat(self, szobaszam, foglalas_datuma):
        mai_nap = date.today()
        if (foglalas_datuma <= mai_nap ):
            return "Adjon meg jövőbeni időpontot"
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglal(szobaszam, foglalas_datuma)
        return "Szoba nem található."


def foglalas(szalloda: Szalloda):
    szalloda.betoltes()

    while True:
        feladat = input("Miben segíthetek? Használja az alábbi billentyűket:"
                        " \nNyomjon: \nF-t, ha foglalna szobát,"
                        " \nL-t, ha lemondana egy foglalást,"
                        " \nV-t ha listázná valamennyi foglalást,"
                        " \nX-t ha kilépne az alkalmazásból:")

        if feladat == "F":
            foglalas_datuma = datetime.strptime(
                input("Hanyadikára foglalna? Adja meg a foglalás dátumát! pl.20240104: "), '%Y%m%d')
            szobaszam = int(input("Kért szoba száma: "))
            print(szalloda.foglal_szobat(szobaszam, foglalas_datuma))
        elif feladat == "L":
            print(szalloda.lemondas())
        elif feladat == "V":
            print(szalloda.foglalasok())
        elif feladat == "X":
            print("Köszönjük, hogy minket választott!")
            break
        else:
            print("Kérem válasszon a felsorolt betűk közül!")


szalloda = Szalloda()
foglalas(szalloda)
