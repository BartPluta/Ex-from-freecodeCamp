# Napisz program proszący o podanie nazwy pliku, a następnie przeszukaj ten plik w celu
# znalezienia linii podobnych do poniższej:
# X - DSPAM - Confidence : 0.8475
# Gdy trafisz na linię, która zaczyna się od „X-DSPAM-Confidence:”, podziel linię tak, by wyodrębnić
# z niej liczbę zmiennoprzecinkową. Zliczaj te linie i sumuj wartości oznaczające pewność, że mamy do
# czynienia ze spamem. Kiedy dotrzesz do końca pliku, wydrukuj średnią wartość pewności spamu.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Error, this file name does not exist.')
    exit()

count = 0
sumnum = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        line = line.split()
        number = float(line[1])
        sumnum += number
avgnum = sumnum / count
print(f'Avarage spam confidence: {avgnum}')




