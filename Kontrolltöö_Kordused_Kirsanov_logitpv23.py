from random import *
from math import *


#5 Найти сумму и произведение цифр, введенного целого числа. Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
print("Sisesta number ")
n=int(input()) # Loeme kasutajalt sisendit ja teisendame selle täisarvuks. Salvestame selle muutujasse n.
a=0
b=1
while n>0: # While-tsükkel, mis käib läbi iga numbri kasutaja sisestatud numbris.
    c=n%10
    a=a+c
    b=b*c
    n=n//10
    print("Summa => ",a)
    print("korrutis => ", b)
    print()

#4 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.




#3 В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

num = randint(0, 100)  # Genereerime juhusliku numbri vahemikus 0 kuni 100 ja salvestame selle muutujasse num
n = 1  # Seadistame katsearvu muutuja väärtuseks 1
# Kasutajale antakse 9 võimalust arvamiseks.
while n < 10:
    # Küsime kasutajalt sisendit ja teisendame selle täisarvuks
    h = int(input("juhuslik täisarv kuni 100 => "))
    # Kontrollime, kas sisestatud arv on väiksem kui juhuslik number
    if h < num:
        print("Rohkem")  # Teavitame kasutajat, et sisestatud number peaks olema suurem
    # Kontrollime, kas sisestatud arv on suurem kui juhuslik number
    elif h > num:
        print("Väiksem")  # Teavitame kasutajat, et sisestatud number peaks olema väiksem
    # Kontrollime, kas sisestatud arv on võrdne juhusliku numbriga
    elif h == num:
        print("Arvasite ära ")  # Teavitame kasutajat, et number on ära arvatud
        break  # Katkestame tsükli, kuna number on ära arvatud
    
    n += 1  # Suurendame katsearvu muutujat 1 võrra pärast igat tsükli iteratsiooni

# Pärast 9 katset väljastatakse juhuslik number.
print("See on number => " + str(num))
print
print()

#2 Посчитать сумму числового ряда от 0 до L (например, 14) включительно. Например, 0+1+2+3+…+14;
L = int(input("Sisesta number" ))  # Küsime kasutajalt sisendit ja teisendame selle täisarvuks. Salvestame selle muutujasse L.
sum = 0  # Initsialiseerime muutuja summa väärtusega 0.
# Tsükkel käib läbi kõik arvud vahemikus 0 kuni L (kaasa arvatud).
for i in range(L+1):
    sum += i  # Lisame iga arvu summale.
    print("Numbrite summa 0 kuni L on: ", sum)  # Prindime välja arvude summa vahemikus 0 kuni L pärast iga iteratsiooni.



#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зайцев. Mежду двумя соседними зайцами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего зайца.
#
#   (\_/)
#   (o o)
#   / | \*

n=randint(1,9) # Genereerime juhusliku arvu vahemikus 1 kuni 9 ja salvestame selle muutujasse n.
for i in range(n): # For-tsükkel, mis käib läbi vahemiku n (kaasa arvatud).
   
    print("    (\_/)  ")
    print("    (o o)  ")
    print("    / | \* ")
    print()
