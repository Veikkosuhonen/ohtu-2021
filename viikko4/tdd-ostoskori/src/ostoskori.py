from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = dict()
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(
            [ostos.lukumaara() for ostos in self._ostokset.values()]
        )

    def hinta(self):
        return sum(
            [ostos.hinta() for ostos in self._ostokset.values()]
        )
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self._ostokset:
            ostos = self._ostokset[lisattava]
            ostos.muuta_lukumaaraa(1)
        else:
            ostos = Ostos(lisattava)
            self._ostokset[lisattava] = ostos

    def poista_tuote(self, poistettava: Tuote):
        if poistettava in self._ostokset:
            self._ostokset[poistettava].muuta_lukumaaraa(-1)
            if self._ostokset[poistettava].lukumaara() == 0:
                self._ostokset.pop(poistettava)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
