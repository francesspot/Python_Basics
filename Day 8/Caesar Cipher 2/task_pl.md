### TODO-1: 
Utwórz funkcję nazwaną `decrypt()`, która przyjmuje `original_text` i `shift_amount` jako 2 argumenty.

### TODO-2: 
W funkcji `decrypt()`, przesuń każdą literę z `original_text` w alfabecie *do tyłu* o wartość `shift_amount` i wyświetl zdeszyfrowany tekst.

<div class="hint">
  Możesz pomnożyć dowolną liczbę przez -1, aby stała się liczbą ujemną.
</div>

### TODO-3: 
- Połącz funkcje `encrypt()` oraz `decrypt()` w jedną funkcję nazwaną `caesar()`.  
- Użyj wartości zmiennej `direction`, wybranej przez użytkownika, aby zdecydować, którą funkcjonalność zastosować.  
- Wywołaj funkcję `caesar` zamiast funkcji encrypt/decrypt i przekaż wszystkie trzy zmienne: `direction`/`text`/`shift`.

<div class="hint">
  Pamiętaj, że mnożąc liczbę przez -1, zmienisz jej znak.  
np. <code>3 + ( 5 * -1)</code> to to samo co <code>3 - 5</code>.
</div>

<div class="hint">
Powinno wyświetlić:  

<code>Here is the encoded result: XXX</code>  

lub  

<code>Here is the decoded result: XXX</code>  
</div>