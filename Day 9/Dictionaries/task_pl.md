Słownik w Pythonie działa podobnie do słownika w prawdziwym życiu. Jest to struktura danych, która pozwala nam skojarzyć klucz z wartością i połączyć te dwa elementy danych razem.

Oto, jak utworzyć słownik w Pythonie:
```
# Przykładowy słownik
kolory = {
    "jabłko": "czerwony", 
    "gruszka": "zielony", 
    "banan": "żółty"
}

```

Oto, jak pobrać elementy ze słownika:
```
print(kolory["gruszka"])
# Wyświetli "zielony"
```

Oto, jak utworzyć pusty słownik:
```
moj_pusty_slownik = {}
```

Oto, jak dodać nowe elementy do istniejącego słownika:

```
kolory["brzoskwinia"] = "różowy"
```

Oto również, jak edytować istniejącą wartość w słowniku:
```
kolory["jabłko"] = "zielony"
```

Oto, jak iterować przez słownik i wyświetlić wszystkie klucze:
```
for key in kolory:
    print(key)
```

Oto, jak iterować przez słownik i wyświetlić wszystkie wartości:
```
for key in kolory:
    print(kolory[key])