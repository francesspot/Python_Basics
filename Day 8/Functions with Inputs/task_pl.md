Wcześniej widzieliśmy, że funkcje pozwalają nam zapakować kod w nazwany blok, który może być używany wielokrotnie w późniejszym czasie.

### PRZERWA 1 - Przejrzyj
- Utwórz funkcję o nazwie `greet()`.  
- Napisz 3 instrukcje `print` wewnątrz funkcji.  
- Wywołaj funkcję `greet()` i uruchom swój kod.  

### Argumenty wejściowe  
Dodanie nazwy zmiennej w nawiasach, gdy tworzymy (definiujemy) nową funkcję, umożliwia tej funkcji przyjmowanie argumentów wejściowych podczas wywoływania.  

Oznacza to, że możemy modyfikować zachowanie funkcji za każdym razem, przekazując różne argumenty wejściowe.  

```
# Tworzenie funkcji
def myFunction(input):
    print(f"Hej! {input}")
```
```
# Używanie funkcji
myFunction("Tommy") 
# Wyświetli "Hej! Tommy"
```

### Argumenty wejściowe to zmienne  
Gdy tworzysz funkcję z argumentami wejściowymi, definiujesz nazwę zmiennej, która będzie przypisana do przekazywanych danych.  

Nazwa zmiennej wejściowej, np. `name` w tym kodzie: `def greet(name):` nazywana jest parametrem.  

Wartość zmiennej wejściowej, np. `Angela` podczas wywoływania funkcji `greet`: `greet("Angela")` nazywana jest argumentem.