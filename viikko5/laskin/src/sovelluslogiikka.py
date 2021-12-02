class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.edelliset = []
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos -= arvo

    def plus(self, arvo):
        self.tulos += arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def tallenna(self):
        self.edelliset.append(self.tulos)
    
    def kumoa(self):
        if self.edelliset:
            self.tulos = self.edelliset.pop()
