Funkcje kończą się na słowie kluczowym `return`. Jeśli napiszesz kod poniżej instrukcji return, ten kod nie zostanie wykonany.

Możesz jednak mieć wiele instrukcji return w jednej funkcji. Jak to działa?

### Warunkowe zwroty

Gdy mamy przepływ kontrolny, czyli gdy kod zachowuje się różnie (podąża różnymi ścieżkami wykonania) w zależności od określonych warunków logicznych, możemy mieć wiele zakończeń (zwrotów).

np.
```
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
```

### Puste zwroty
Możesz również napisać return bez niczego po nim, co po prostu informuje funkcję, aby zakończyła swoje działanie.

np.
```
def canBuyAlcohol(age):
    # Jeśli typ danych przekazanego wieku nie jest liczbą całkowitą, zakończ.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False