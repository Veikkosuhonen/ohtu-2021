import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


MAITO_ID = 1
MAITO_HINTA = 5
MEHU_ID = 2
MEHU_HINTA = 4
LOPPUNUT_ID = 3
LOPPUNUT_HINTA = 7

 # tehdään toteutus saldo-metodille
def varasto_saldo(tuote_id):
    if tuote_id == MAITO_ID or tuote_id == MEHU_ID:
        return 10
    if tuote_id == LOPPUNUT_ID:
        return 0

# tehdään toteutus hae_tuote-metodille
def varasto_hae_tuote(tuote_id):
    if tuote_id == MAITO_ID:
        return Tuote(MAITO_ID, "maito", MAITO_HINTA)
    if tuote_id == MEHU_ID:
        return Tuote(MEHU_ID, "mehu", MEHU_HINTA)
    if tuote_id == LOPPUNUT_ID:
        raise Exception("Loppunutta tuotetta ei saa hakea varastosta")
    

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    

    def test_ostoksen_paatyttya_tilisiirto_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("kekkonen", "00000")

        self.pankki_mock.tilisiirto.assert_called_with("kekkonen", 42, "00000", ANY, MAITO_HINTA)

    
    def test_kahden_eri_tuotteen_ostoksessa_tilisiirto_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.lisaa_koriin(MEHU_ID)
        self.kauppa.tilimaksu("pave", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("pave", 42, "11111", ANY, MAITO_HINTA + MEHU_HINTA)
    

    def test_kahden_saman_tuotteen_ostoksessa_tilisiirto_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("pave", 42, "11111", ANY, 2*MAITO_HINTA)


    def test_saatavan_tuotteen_ja_loppuneen_tuotteen_ostoksessa_tilisiirto_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.lisaa_koriin(LOPPUNUT_ID)
        self.kauppa.tilimaksu("pave", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("pave", 42, "11111", ANY, MAITO_HINTA)
    

    def test_asioinnin_aloitus_nollaa_ostoskorin(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("pave", 42, "11111", ANY, MAITO_HINTA)
    

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [100, 101, 102]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")
        self.pankki_mock.tilisiirto.assert_called_with("pave", 100, "11111", ANY, MAITO_HINTA)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")
        self.pankki_mock.tilisiirto.assert_called_with("pave", 101, "11111", ANY, MAITO_HINTA)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")
        self.pankki_mock.tilisiirto.assert_called_with("pave", 102, "11111", ANY, MAITO_HINTA)
    
    def test_ostoskorista_poistettu_tuote_ei_tule_maksuun(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.lisaa_koriin(MEHU_ID)
        self.kauppa.poista_korista(MAITO_ID)
        self.kauppa.tilimaksu("pave", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("pave", 42, "11111", ANY, MEHU_HINTA)
    
    def test_ostoskorista_poistettu_tuote_palautetaan_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO_ID)
        self.kauppa.lisaa_koriin(MEHU_ID)
        self.kauppa.poista_korista(MAITO_ID)

        self.varasto_mock.palauta_varastoon.assert_called_once_with(Tuote(MAITO_ID, "maito", MAITO_HINTA))
