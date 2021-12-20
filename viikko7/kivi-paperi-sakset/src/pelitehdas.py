from kps import KPS
from ihmispelaaja import Ihmispelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class PeliTehdas:

    @staticmethod
    def kaksinpeli() -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            Ihmispelaaja("pelaaja2")
        )
    
    @staticmethod
    def yksinpeli() -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            Tekoaly()
        )
    
    @staticmethod
    def yksinpeli_vaikea() -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            TekoalyParannettu()
        )
    