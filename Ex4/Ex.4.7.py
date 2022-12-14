#Ex 4.14.7 Napisz ponownie program z poprzedniego rozdziału do wyliczania ocen za pomocą funkcji
# o nazwie computegrade(), która przyjmuje jako argument wartość i zwraca ocenę jako napis.


def computegrade (question):
    try:
        value = float(question)
        if value < 0 or value > 1:
            print('Incorrect input. Please enter value between 0.0 and 1.0')
        elif 0.0 <= value <= 1.0:
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


question = input('Please write value between 0.0 and 1.0.\n')
computegrade(question)