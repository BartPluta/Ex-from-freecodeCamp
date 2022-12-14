# Napisz program, który odczytuje liczby tak długo, aż użytkownik wprowadzi „gotowe”.
# Po wpisaniu „gotowe” wypisz sumę, ile wprowadzono liczb oraz średnią z tych liczb. Jeśli użytkownik
# wprowadzi coś innego niż liczba, to używając try i except wykryj jego błąd, wypisz komunikat o błędzie
# oraz przejdź do następnej liczby

suma_liczb = 0
ile_liczb = 0
while True:
    try:
        en = input('Wprowadź liczbę: ')
        if en == 'gotowe':
            break
        en = int(en)
        print(en)
        suma_liczb = suma_liczb + en
        ile_liczb = ile_liczb + 1
    except:
        print('złe dane')
avg = suma_liczb / ile_liczb
print(f'Suma podanych liczb: {suma_liczb}, Podałeś {ile_liczb} liczb, Średnia to {avg}')
