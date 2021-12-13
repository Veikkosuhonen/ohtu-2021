from pelaaja import Pelaaja

class Ihmispelaaja(Pelaaja):

    def anna_siirto(self) -> str:
        return input("Anna pelaajan '" + self.nimi + "' siirto: ")
    