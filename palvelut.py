import random
class Asiakas:
    def __init__(self, nimi, ika):
        """Luokka, joka edustaa asiakasta.

        Args:
            nimi (str): Asiakkaan nimi.
            ika (int): Asiakkaan ikä.
        """
        self._nimi = None
        self._ika = None
        self._asiakasnumero = None
        self.set_nimi(nimi)
        self.set_ika(ika)
        self.set_asiakasnumero(self.luo_nro())

    def get_nimi(self):
        """Palauttaa asiakkaan nimen."""
        return self._nimi

    def set_nimi(self, nimi):
        """Asettaa asiakkaan nimen.

        Args:
            nimi (str): Asiakkaan nimi.
        
        Raises:
            ValueError: Jos nimi ei ole annettu.
        """
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        self._nimi = nimi

    def get_ika(self):
        """Palauttaa asiakkaan iän."""
        return self._ika

    def set_ika(self, ika):
        """Asettaa asiakkaan iän.

        Args:
            ika (int): Asiakkaan ikä.
        
        Raises:
            ValueError: Jos ikä ei ole annettu.
        """
        if not ika:
            raise ValueError("Ikä on annettava.")
        self._ika = ika

    def get_asiakasnumero(self):
        """Palauttaa asiakkaan asiakasnumeron."""
        return self._asiakasnumero

    def set_asiakasnumero(self, asiakasnumero):
        """Asettaa asiakkaan asiakasnumeron.

        Args:
            asiakasnumero (str): Asiakkaan asiakasnumero.
        
        Raises:
            ValueError: Jos asiakasnumero ei ole annettu.
        """
        if not asiakasnumero:
            raise ValueError("Asiakasnumero on annettava.")
        self._asiakasnumero = asiakasnumero

    def luo_nro(self):
        """Luo uuden asiakasnumeron satunnaisista numeroista.

        Returns:
            str: Luotu asiakasnumero.
        """
        numerot = [random.randint(0, 9) for _ in range(3)]
        asiakasnumero = f"{numerot[0]}{numerot[1]}-{numerot[2]}{numerot[0]}{numerot[1]}-{numerot[2]}{numerot[0]}{numerot[1]}"
        return asiakasnumero

    def luo_asiakasrivi(self):
        """Luo asiakkaasta rivin tulostusta varten.

        Returns:
            str: Asiakkaasta luotu rivi.
        """
        return f"{self._nimi} ({self._asiakasnumero}) on {self._ika}-vuotias"



class Palvelu:
    def __init__(self, tuotenimi):
        """
        Luo Palvelu-olio.

        Args:
            tuotenimi (str): Tuotteen nimi.
        """
        self._tuotenimi = tuotenimi
        self._asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        """
        Lisää asiakas Palveluun.

        Args:
            asiakas (Asiakas): Asiakas-olio.

        Raises:
            ValueError: Jos asiakas on None.
        """
        if not asiakas:
            raise ValueError("Asiakas on annettava.")
        self._asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        """
        Poistaa asiakas Palvelusta.

        Args:
            asiakas (Asiakas): Asiakas-olio.
        """
        try:
            self._asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        """
        Tulostaa Palvelun asiakkaat.
        """
        print(f"Tuotteen {self._tuotenimi} asiakkaat ovat:")
        for asiakas in self._asiakkaat:
            print(asiakas.luo_asiakasrivi())


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        """
        Luo ParempiPalvelu-olio.

        Args:
            tuotenimi (str): Tuotteen nimi.
        """
        super().__init__(tuotenimi)
        self._edut = []

    def lisaa_etu(self, etu):
        """
        Lisää etu ParempiPalveluun.

        Args:
            etu (str): Etu.

        Raises:
            ValueError: Jos etu on None.
        """
        if not etu:
            raise ValueError("Etu on annettava.")
        self._edut.append(etu)

    def poista_etu(self, etu):
        """
        Poistaa etu ParempiPalvelusta.

        Args:
            etu (str): Etu.
        """
        try:
            self._edut.remove(etu)
        except ValueError:
            pass

    def tulosta_edut(self):
        """
        Tulostaa ParempiPalvelun edut.
        """
        print(f"Tuotteen {self._tuotenimi} edut ovat:")
        for etu in self._edut:
            print(etu)
