# Ex.3.3 Napisz program, który poprosi użytkownika o wartość pomiędzy 0.0 a 1.0. Jeśli wartość
# jest poza zakresem, wypisz komunikat o błędzie. Jeśli wartość jest między 0.0 a 1.0, wypisz ocenę.

question = input('Please write value between 0.0 and 1.0.\n')
try:
    value = float(question)
    if value >= 0.0 and value <= 1.0:
        if value >= 0.9:
            print('Your mark is 5.0')
        elif value >= 0.8:
            print('Your mark is 4.5')
        elif value >= 0.7:
            print('Your mark is 4.0')
        elif value >= 0.6:
            print('Your mark is 3.5')
        elif value >= 0.5:
            print('Your mark is 3.0')
        else:
            print('Your mark is 2.0')
except:
    print('Incorrect input. Please write numerical value between 0.0 and 1.0')
    exit()
