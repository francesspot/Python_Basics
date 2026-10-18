### TODO-1: 
Zaimportuj i wyświetl logo z pliku art.py, gdy program się uruchamia.

### TODO-2: 
Co się stanie, jeśli użytkownik wprowadzi liczbę/symbol/spację, która nie znajduje się na Liście `alphabet`?

Czy możesz poprawić kod tak, aby liczba/symbol/spacja pozostały niezmodyfikowane podczas kodowania/dekodowania tekstu?

Np. 
```
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```

<div class="hint">
  Jeśli znak nie jest literą z Listy alphabet, możesz go po prostu dodać na końcu cipher_text jako niezmodyfikowany znak?
</div>

### TODO-3: 
Czy potrafisz znaleźć sposób na ponowne uruchomienie programu szyfrującego?

Np. 

`Wpisz 'yes', jeśli chcesz spróbować ponownie. W innym wypadku wpisz 'no'.`

Jeśli wpiszą 'yes', poproś ich ponownie o kierunek/tekst/przesunięcie i ponownie wywołaj funkcję `caesar()`.

<div class="hint">
  Spróbuj stworzyć pętlę while, która będzie wykonywała program, jeśli użytkownik wpisze 'yes'.
</div>