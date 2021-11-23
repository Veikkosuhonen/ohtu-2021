from typing import List

KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")

        self.kasvatuskoko = kasvatuskoko
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")

        self.taulukko = [0] * self.kapasiteetti

        self.alkioiden_maara = 0


    def kuuluu(self, n) -> bool:
        for i in range(self.alkioiden_maara):
            if self.taulukko[i] == n:
                return True
        return False


    def lisaa(self, n) -> bool:
        if self.kuuluu(n):
            return False
        
        if self.alkioiden_maara == len(self.taulukko):
            self._kasvata_taulukkoa()
        
        self.taulukko[self.alkioiden_maara] = n
        self.alkioiden_maara = self.alkioiden_maara + 1

        return True


    def _kasvata_taulukkoa(self):
        taulukko_old = self.taulukko
        uusi_kapasiteetti = self.alkioiden_maara + self.kasvatuskoko
        self.taulukko = [0] * uusi_kapasiteetti
        self._kopioi_taulukko(taulukko_old, self.taulukko)
        self.kapasiteetti = uusi_kapasiteetti
    

    def _kopioi_taulukko(self, vanha, uusi):
        for i in range(0, len(vanha)):
            uusi[i] = vanha[i]


    def poista(self, n) -> bool:
        indeksi = self._hae_indeksi(n)

        if indeksi == -1:
            return False
        
        viimeinen_indeksi = self.alkioiden_maara - 1
        self._vaihda_arvot(indeksi, viimeinen_indeksi)
        self.alkioiden_maara -= 1

        return True


    def _hae_indeksi(self, n) -> int:
        for i in range(0, self.alkioiden_maara):
            if n == self.taulukko[i]:
                return i
        return -1
    

    def _vaihda_arvot(self, i, j):
        temp = self.taulukko[i]
        self.taulukko[i] = self.taulukko[j]
        self.taulukko[j] = temp


    def mahtavuus(self) -> int:
        return self.alkioiden_maara


    def to_int_list(self) -> List[int]:
        lista = [0] * self.alkioiden_maara
        for i in range(self.alkioiden_maara):
            lista[i] = self.taulukko[i]
        return lista


    def _kopio(self):
        uusi = IntJoukko(self.kapasiteetti, self.kasvatuskoko)
        self._kopioi_taulukko(self.taulukko, uusi.taulukko)
        uusi.alkioiden_maara = self.alkioiden_maara
        return uusi


    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = a._kopio()
        for i in range(b.alkioiden_maara):
            yhdistejoukko.lisaa(b.taulukko[i])

        return yhdistejoukko


    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = a._kopio()
        for i in range(a.alkioiden_maara):
            if not b.kuuluu(a.taulukko[i]):
                leikkausjoukko.poista(a.taulukko[i])

        return leikkausjoukko


    @staticmethod
    def erotus(a, b):
        erotusjoukko = a._kopio()
        for i in range(b.alkioiden_maara):
            erotusjoukko.poista(b.taulukko[i])

        return erotusjoukko


    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.taulukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(self.alkioiden_maara - 1):
                tuotos += str(self.taulukko[i])
                tuotos += ", "
            tuotos += str(self.taulukko[self.alkioiden_maara - 1])
            tuotos += "}"
            return tuotos
    