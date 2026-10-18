### TypeError
Te błędy występują, gdy używasz nieodpowiedniego typu danych.  
np. `len(12345)`  

Ponieważ funkcja `len()` może przyjmować jedynie ciągi znaków (Strings), odmówi działania i zwróci błąd TypeError, jeśli podasz jej liczbę całkowitą (Integer).  

#### PAUZA 1. Popraw funkcję `len()`, aby nie generowała więcej ostrzeżeń ani błędów.

### Sprawdzanie typu
Możesz sprawdzić typ danych dowolnej wartości lub zmiennej w Pythonie, używając funkcji `type()`.  

`print(type("abc")) #zwróci <class 'str'>`  

#### PAUZA 2. Napisz 4 sprawdzenia typu, aby wydrukować wszystkie 4 typy danych  
Użyj funkcji `type()` i `print()` do wydrukowania 4 wierszy na obszar wyjściowy, aby uzyskać pełną kolekcję typów danych, które poznaliśmy. `<class 'str'> <class 'int'> <class 'float'> i <class 'bool'>`

### Konwersja typów
Możesz konwertować dane do różnych typów za pomocą specjalnych funkcji.  
np.  

`float()`  

`int()`  

`str()`  

#### PAUZA 3. Spraw, aby ten kod działał bez błędów
`print("Liczba liter w Twoim imieniu: " + len(input("Wpisz swoje imię")))`