# Napisz program odczytujący plik i wypisz zawartość pliku (wiersz po wierszu), ale dużymi literami.

fname = input('Podaj nazwę pliku: ')
fhand = open(fname)
plik = fhand.read().upper()
print(plik)