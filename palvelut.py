import random


class Asiakas:
    def __init__(self, nimi, ika):
        self._nimi = None
        self._ika = None
        self._asiakasnumero = None
        self.set_nimi(nimi)
        self.set_ika(ika)
        self.set_asiakasnumero(self.luo_nro())

    def get_nimi(self):
        return self._nimi

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        self._nimi = nimi

    def get_ika(self):
        return self._ika

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Ikä on annettava.")
        self._ika = ika

    def get_asiakasnumero(self):
        return self._asiakasnumero

    def set_asiakasnumero(self, asiakasnumero):
        if not asiakasnumero:
            raise ValueError("Asiakasnumero on annettava.")
        self._asiakasnumero = asiakasnumero

    def luo_nro(self):
        numerot = [random.randint(0, 9) for _ in range(3)]
        asiakasnumero = f"{numerot[0]}{numerot[1]}-{numerot[2]}{numerot[0]}{numerot[1]}-{numerot[2]}{numerot[0]}{numerot[1]}"
        return asiakasnumero

    def luo_asiakasrivi(self):
        return f"{self._nimi} ({self._asiakasnumero}) on {self._ika}-vuotias"


class Palvelu:
    def __init__(self, tuotenimi):
        self._tuotenimi = tuotenimi
        self._asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Asiakas on annettava.")
        self._asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        try:
            self._asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        print(f"Tuotteen {self._tuotenimi} asiakkaat ovat:")
        for asiakas in self._asiakkaat:
            print(asiakas.luo_asiakasrivi())


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self._edut = []

    def lisaa_etu(self, etu):
        if not etu:
            raise ValueError("Etu on annettava.")
        self._edut.append(etu)

    def poista_etu(self, etu):
        try:
            self._edut.remove(etu)
        except ValueError:
            pass

    def tulosta_edut(self):
        print(f"Tuotteen {self._tuotenimi} edut ovat:")
        for etu in self._edut:
            print(etu)
