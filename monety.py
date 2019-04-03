
kwota1 = int(input('podaj kwote: '))
nominaly1 = [200, 100, 50, 20, 10, 5, 2, 1]


def wydaj(nom):
    global kwota1
    ilosc_do_wydania = 0
    while kwota1 >= nom:
        ilosc_do_wydania += 1
        kwota1 = kwota1 - nom
    print('nominał: {}zl, do wydania: {}'.format(nom, ilosc_do_wydania))


# for nominal in nominaly:
#     wydaj(nominal)


def wydaj_z_kwoty(kwota):
    print('kwota do rozmienienia: {}'.format(kwota))
    nominaly = [200, 100, 50, 20, 10, 5, 2, 1]
    for nominal in nominaly:
        ilosc_do_wydania = 0
        while kwota >= nominal:
            ilosc_do_wydania += 1
            kwota = kwota - nominal
        print('nominal: {} ilosc do wydania: {} pozostalo: {}'.format(nominal, ilosc_do_wydania, kwota))


def wydaj_z_kwoty_w_nominalach(kwota, nominaly):
    print('kwota do rozmienienia: {}\n'.format(kwota))
    print('dostepne nominaly: {}\n'.format(nominaly))
    for nominal in nominaly:
        ilosc_do_wydania = 0
        while kwota >= nominal:
            ilosc_do_wydania += 1
            kwota = kwota - nominal
        if ilosc_do_wydania != 0:
            print('nominal: {} ilosc do wydania: {} pozostalo: {}'.format(nominal, ilosc_do_wydania, kwota))
        else:
            pass


# wydaj_z_kwoty(kwota1)
wydaj_z_kwoty_w_nominalach(kwota1, [200, 100, 1])