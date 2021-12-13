from pelitehdas import PeliTehdas

def main():
    pelitehdas = PeliTehdas()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            pelitehdas.kaksinpeli().pelaa()
        elif vastaus.endswith("b"):
            pelitehdas.yksinpeli().pelaa()
        elif vastaus.endswith("c"):
            pelitehdas.yksinpeli_vaikea().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
