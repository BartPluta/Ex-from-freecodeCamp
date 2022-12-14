# Napisz kolejny program, który będzie prosił o listę liczb tak jak wyżej, ale na końcu
# zamiast średniej wypisze zarówno największą, jak i najmniejszą wprowadzoną liczbę.

liczby = list()
while True:
    try:
        en = input('Wprowadź liczbę: ')
        if en == 'gotowe':
            break
        en = int(en)
        print(en)
        liczby.append(en)
    except:
        print('złe dane')

max_value = None
min_value = None
for x in liczby:
    if max_value is None or x > max_value:
        max_value = x
print(f'Największa liczba z wprowadzonych to: {max_value}')

for x in liczby:
    if min_value is None or x < min_value:
        min_value = x
print(f'Najmniejsza liczba z wprowadzonych to: {min_value}')

print('Największa wprowadzona liczba uzyskana łatwiejszym sposobem to:', max(liczby))
print('Najmniejsza wprowadzona liczba uzyskana łatwiejszym sposobem to: ', min(liczby))