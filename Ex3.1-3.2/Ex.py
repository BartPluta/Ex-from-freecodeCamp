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


def computeypay(hours, rate):
    overtime = hours - 40
    if overtime > 0:
        normal_pay = rate * (hours - overtime)
        extra_pay = overtime * (rate * 1.5)
        print(f'''
        Your Hours: {hours}
        Your Rate: {rate}
        Your pay: {normal_pay + extra_pay}''')
    elif overtime < 0:
        normal_pay = rate * hours
        print(f'''
        Your Hours: {hours}
        Your Rate: {rate}
        Your pay: {normal_pay}''')


computeypay(20, 10)

