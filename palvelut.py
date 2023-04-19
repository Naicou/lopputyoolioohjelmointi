import random


class Asiakas:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.asiakasnumero = self.luo_nro()

    def get_nimi(self):
        return self.nimi

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Nimi ei voi olla tyhjä")
        self.nimi = nimi

    def get_ika(self):
        return self.ika

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Ikä ei voi olla tyhjä")
        self.ika = ika

    def get_asiakasnumero(self):
        return f"{self.asiakasnumero[0]:02}-{self.asiakasnumero[1]:03}-{self.asiakasnumero[2]:03}"

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Asiakas ei voi olla tyhjä")
        self.asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        try:
            self.asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))

    def luo_nro(self):
        return [random.randint(0, 9) for _ in range(3)]

    def luo_asiakasrivi(self, asiakas):
        return f"{asiakas.nimi} ({asiakas.ika}-vuotias)\n{asiakas.get_nimi()} ({asiakas.get_asiakasnumero()}) on {asiakas.get_ika()}-vuotias."


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Asiakas ei voi olla tyhjä")
        self.asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        try:
            self.asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        print(f"Tuotteen {self.tuotenimi} asiakkaat ovat:")
        for asiakas in self.asiakkaat:
            print(asiakas.luo_asiakasrivi(asiakas))


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        if not etu:
            raise ValueError("Etu ei voi olla tyhjä")
        self.edut.append(etu)

    def poista_etu(self, etu):
        try:
            self.edut.remove(etu)
        except ValueError:
            pass

    def tulosta_edut(self):
        print(f"Tuotteen {self.tuotenimi} edut ovat:")
        for etu in self.edut:
         print(etu)
