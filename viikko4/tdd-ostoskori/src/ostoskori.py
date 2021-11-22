from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self.ostokset)

    def hinta(self):
        if self.ostokset:
            return self.ostokset[0].hinta() * 2
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        self.ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
