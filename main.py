import time
print('Rodzaje biletów.')
type_of_ticket = ['normalny 30 minutowy', 'normalny całodniowy', 'ulgowy 30 minutowy', 'ulgowy całodniowy']
print(*type_of_ticket,sep='\n')
selected_ticket = input('Wybierz, który chcesz zakupić: ')

def normalny_30_minutowy():
    price = 4
    return price

def normalny_calodniowy():
    price = 20
    return price

def ulgowy_30_minutowy():
    price = normalny_30_minutowy() * 0.50
    return int(price)

def ulgowy_calodniowy():
    price = normalny_calodniowy() * 0.50
    return int(price)

if selected_ticket == 'normalny 30 minutowy':
    print('Wybrałeś bilet normalny 30 minutowy, jego cena to: ', normalny_30_minutowy(),'PLN')
    credit_cart = int(input('Wprowadź numer karty: '))
    pin = int(input('Wprowadź pin karty: '))
    print("Zakupiono bilet normalny 30 minutowy")

elif selected_ticket == 'normalny całodniowy':
    print('Wybrałeś bilet normalny całodniowy, jego cena to: ', normalny_calodniowy(),'PLN')
    credit_cart = int(input('Wprowadź numer karty: '))
    pin = int(input('Wprowadź pin karty: '))
    print("Zakupiono bilet normalny całodniowy")

elif selected_ticket == 'ulgowy 30 minutowy':
    print('Wybrałeś bilet ulgowy 30 minutowy, jego cena to: ', ulgowy_30_minutowy(),'PLN')
    credit_cart = int(input('Wprowadź numer karty: '))
    pin = int(input('Wprowadź pin karty: '))
    print("Zakupiono bilet ulgowy 30 minutowy")

elif selected_ticket == 'ulgowy całodniowy':
    print('Wybrałeś bilet ulgowy całodniowy, jego cena to: ', ulgowy_calodniowy(),'PLN')
    credit_cart = int(input('Wprowadź numer karty: '))
    pin = int(input('Wprowadź pin karty: '))
    print("Zakupiono bilet ulgowy całodniowy")

elif selected_ticket != type_of_ticket:
    print("Taki bilet nie jest możliwy do kupienia.")

time.sleep(10)