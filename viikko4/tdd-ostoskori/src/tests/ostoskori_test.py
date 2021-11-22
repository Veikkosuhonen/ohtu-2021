import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.assertEqual(self.kori.hinta(), 10)
    
    def test_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(Tuote("Maito", 5))
        self.assertEqual(len(self.kori._ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[maito]
        self.assertEqual("Maito", ostos.tuote.nimi())
        self.assertEqual(1, ostos.lukumaara())

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        mehu = Tuote("Mehu", 4)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(len(self.kori.ostokset()), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_ostoksella_oikeat_tiedot(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual("Maito", self.kori.ostokset()[maito].tuotteen_nimi())
        self.assertEqual(2, self.kori.ostokset()[maito].lukumaara())
    
    def test_kahden_saman_tuotteen_korista_tuotteen_poistamisen_jalkeen_ostoksen_lukumaara_1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(1, self.kori.ostokset()[maito].lukumaara())