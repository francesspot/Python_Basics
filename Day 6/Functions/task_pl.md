Funkcja w swojej najprostszej formie jest po prostu nazwą opakowania dla bloku kodu. Nadajesz jej nazwę, a potem, gdy wywołujesz funkcję po tej nazwie, cały kod wewnątrz bloku funkcji zostaje wykonany. To może pomóc zaoszczędzić czas i zredukować powtarzający się kod.

### Definiowanie nowej funkcji
```
def <nazwa_funkcji>():
    print("Cześć")
    # Robi coś innego
    # Robi coś innego ...
```

### Wywoływanie funkcji
Wywołanie funkcji oznacza po prostu jej uruchomienie. Możemy wywołać funkcję w dowolnym momencie naszego kodu w Pythonie.

```
<nazwa_funkcji>()
```

Łącząc wszystko w całość, np.:
```
#Tworzenie funkcji
def get_user_name():
    name = input("Jak masz na imię? ")
    print("Cześć, " + name)
    # Wewnątrz funkcji

#Poza funkcją
print("Cześć")
get_user_name() # Wywołanie funkcji
```

Ten kod spowoduje następującą sekwencję wyników:
```
Cześć
Jak masz na imię? #Wpisuję Angela
Cześć
Angela