Możesz łączyć i dopasowywać różne typy danych, aby osiągnąć pożądaną strukturę.

### Zagnieżdżanie listy w słowniku
Zamiast wartości typu String przypisanej do klucza, możemy zastąpić ją Listą. Możesz zagnieździć Listę w Słowniku w taki sposób:

```
my_dictionary = {
    key1: [Lista],
    key2: Wartość,
}
```

### PAUZA 1
Sprawdź, czy potrafisz wymyślić, jak wydrukować "Lille" z zagnieżdżonej Listy o nazwie `travel_log`.
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  Aby uzyskać tę część: <code>["Paris", "Lille", "Dijon"]</code>
Potrzebujesz: <code>travel_log["France"]</code>

Dlatego, aby uzyskać Lille, potrzebujesz:
<code>travel_log["France"][1]</code>
</div>

### Zagnieżdżanie list w innych listach

Widzieliśmy wcześniej zagnieżdżone listy:

```
nested_list = ["A", "B", ["C", "D"]]
```

### PAUZA 2
Czy pamiętasz, jak uzyskać elementy, które są głęboko zagnieżdżone w liście? Spróbuj wydrukować "D" z listy `nested_list`.

<div class="hint">
  Aby uzyskać tę listę: ["C", "D"] potrzebujemy kodu:

<code>nested_list[2]</code>

Dlatego, aby uzyskać "D", potrzebujemy:

<code>nested_list[2][1]</code>
</div>

### Zagnieżdżanie słownika w słowniku
Możesz również zagnieździć słownik w słowniku:

```
my_dictionary = {
    key1: Wartość,
    key2: {Klucz: Wartość, Klucz: Wartość},
}
```

### PAUZA 3
Wymyśl, jak wydrukować "Stuttgart" z poniższej listy:
```
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}