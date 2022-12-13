# Ex. 3.1 Przepisz ponownie swój program obliczający wynagrodzenie, tak aby dać pracownikowi
# 1,5 raza większą stawkę godzinową za czas przepracowany powyżej 40 godzin.
# Ex.3.2  Przepisz ponownie swój program płacowy, używając try i except, tak aby elegancko 
# obsługiwał on nienumeryczne dane wejściowe, wyświetlając w takim przypadku wiadomość i kończąc swoje działanie

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric number')
    quit()

if hours <= 40:
    normal_pay = hours * rate
    print(f'''
    Your Hours: {hours}
    Your Rate: {rate}
    Your pay: {normal_pay}''')
overtime = hours - 40
if overtime > 0:
    normal_pay = rate * (hours - overtime)
    extra_pay = overtime * (rate * 1.5)
    print(f'''
    Your Hours: {hours}
    Your Rate: {rate}
    Your pay: {normal_pay + extra_pay}''')
    
#Jako cos dodatkowego stworzyłęm funkcja która wykonuje zadania z ćwiczenia powyzej,a jednocześnie mogłaby zostać użyta dla wielu osób dzięki dodaniu paramtetru z imieniem.


def computeypay(name, hours, rate):
    overtime = hours - 40
    if overtime > 0:
        normal_pay = rate * (hours - overtime)
        extra_pay = overtime * (rate * 1.5)
        print(f'''
        {name}
        Your Hours: {hours}
        Your Rate: {rate}
        Your pay: {normal_pay + extra_pay}''')
    elif overtime < 0:
        normal_pay = rate * hours
        print(f'''
        {name}
        Your Hours: {hours}
        Your Rate: {rate}
        Your pay: {normal_pay}''')


computeypay('Bartek', 20, 10)



