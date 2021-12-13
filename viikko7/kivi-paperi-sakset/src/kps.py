from tuomari import Tuomari

class KPS:

    def __init__(self, pelaaja1, pelaaja2) -> None:
        self.pelaaja1 = pelaaja1
        self.pelaaja2 = pelaaja2
        self.tuomari = Tuomari()

    def pelaa(self):
        self._aloitusviesti()
        while True:
            jatketaan = self._kierros()
            if not jatketaan:
                break
        self._lopetusviesti()

    def _kierros(self) -> bool:
        ekan_siirto = self._ensimmaisen_siirto()
        if not self._onko_ok_siirto(ekan_siirto):
            return False
        self._kerro_siirto(ekan_siirto, self.pelaaja1)

        tokan_siirto = self._toisen_siirto(ekan_siirto)
        if not self._onko_ok_siirto(tokan_siirto):
            return False
        self._kerro_siirto(tokan_siirto, self.pelaaja2)

        self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        print(self.tuomari)
        return True

    def _ensimmaisen_siirto(self):
        return self.pelaaja1.anna_siirto()

    def _toisen_siirto(self, ensimmaisen_siirto):
        self.pelaaja2.aseta_siirto(ensimmaisen_siirto)
        return self.pelaaja2.anna_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def _kerro_siirto(self, siirto, pelaaja):
        print("Pelaaja '" + pelaaja.nimi + "' valitsi " + siirto)
    
    def _aloitusviesti(self):
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
    
    def _lopetusviesti(self):
        print("Kiitos!")
        print(self.tuomari)

