from kps import KPS
from ihmispelaaja import Ihmispelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class PeliTehdas:
    def __init__(self) -> None:
        pass

    def kaksinpeli(self) -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            Ihmispelaaja("pelaaja2")
        )
    
    def yksinpeli(self) -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            Tekoaly()
        )
    
    def yksinpeli_vaikea(self) -> KPS:
        return KPS(
            Ihmispelaaja("pelaaja1"),
            TekoalyParannettu()
        )
    