from pelitehdas import PeliTehdas

def main():

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            PeliTehdas.kaksinpeli().pelaa()
        elif vastaus.endswith("b"):
            PeliTehdas.yksinpeli().pelaa()
        elif vastaus.endswith("c"):
            PeliTehdas.yksinpeli_vaikea().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
