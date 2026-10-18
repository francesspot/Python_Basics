### Zaokrąglanie liczby w dół
Możesz zaokrąglić liczbę w dół lub usunąć wszystkie miejsca po przecinku, używając funkcji `int()` która konwertuje liczbę zmiennoprzecinkową (z miejscami dziesiętnymi) na liczbę całkowitą (liczbę całkowitą bez miejsc dziesiętnych).

`int(3.738492) # Staje się 3`

### Zaokrąglanie liczby
Jeśli jednak chcesz zaokrąglić liczbę dziesiętną do najbliższej liczby całkowitej w tradycyjny matematyczny sposób, gdzie wszystko powyżej .5 zaokrągla się w górę, a wszystko poniżej w dół, możesz użyć funkcji `round()` w Pythonie.

`round(3.738492) # Staje się 4`

`round(3.14159) # Staje się 3`

`round(3.14159, 2) # Staje się 3.14`

### Operatory przypisania
Operatory przypisania, takie jak operator przypisania z dodawaniem `+=`, dodają liczbę po prawej stronie do pierwotnej wartości zmiennej po lewej stronie i przypisują nową wartość do tej zmiennej.

`+=`

`-=`

`*=`

`/=` 

### f-Stringi
W Pythonie można używać f-stringów do wstawiania zmiennej lub wyrażenia do ciągu znaków.

`age = 12`

`print(f"Mam {age} lat")`

`# Zwróci "Mam 12 lat".`