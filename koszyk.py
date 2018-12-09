zakup = ['kefir', 'marchew', 'kawa']
ceny = [1.0, 2.0,3.5]
wartosc = [2]
# ilosc_marchewe = [1]
# ilosc_kefir = [1]
# ilosc_kawa = [1]
# cena_marchew = [5]
# cena_kefir = [10]
# cena_kawa = [15]
# wartosc = [0]

if wartosc < 1 and wartosc < 6.5:
    print('Promocja 20%')
    wartosc = wartosc - (wartosc *20) / 100

elif wartosc >=6.5:
    print('Promocja 25%')
    wartosc = wartosc - (wartosc *25) / 100

    print('Do zaplacenia ' + str(wartosc))
