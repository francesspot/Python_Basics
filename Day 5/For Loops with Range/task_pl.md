Połączenie funkcji `range()` z pętlą For w Pythonie pozwala nam uruchomić pętlę tak wiele razy, jak chcemy. Zamiast iterować po każdym elemencie Listy, możemy iterować po zakresie liczb.

### Funkcja range

`range(1, 10)`

Ten kod sam w sobie niczego nie robi. Na przykład, jeśli spróbujesz go wydrukować, nie zwróci on pojedynczych liczb.

Może jednak być użyty w połączeniu z pętlami For. np.

```
for number in range(1, 10):
    print(number)
```

To wydrukuje każdą z liczb od 1 do 9. Zakres można więc wyrazić w ten sposób:

`a <= range(a, b) < b`

Gdzie zakres liczb obejmuje dolną granicę, ale nie obejmuje górnej granicy.

### PRZERWA 1 - Wyzwanie Gaussa
Oblicz sumę liczb pomiędzy 1 a 100, włącznie z 1 i 100.