Celem jest stworzenie programu kalkulatora.

### Demo
https://appbrewery.github.io/python-day10-demo/

### Przechowywanie funkcji jako wartości zmiennej
Możesz przechowywać referencję do funkcji jako wartość zmiennej.  
np.
```
def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Zwróci 8
```
W pliku początkowym znajdziesz słownik odnoszący się do każdej operacji matematycznej, którą może wykonać nasz kalkulator. Wypróbuj i sprawdź, czy potrafisz wykonać dodawanie, odejmowanie, mnożenie i dzielenie.

### PAUZA 1 
TODO: Napisz pozostałe 3 funkcje - odejmowanie, mnożenie i dzielenie.

### PAUZA 2
TODO: Dodaj te 4 funkcje do słownika jako wartości. Klucze = "`+`", "`-`", "`*`", "`/`"

### PAUZA 3
TODO: Użyj operacji w słowniku, aby wykonać kalkulację. Pomnóż 4 * 8, korzystając ze słownika.

### Funkcjonalność
- Program pyta użytkownika o wpisanie pierwszej liczby.
- Program pyta użytkownika o wpisanie operatora matematycznego (do wyboru: "`+`", "`-`", "`*`" lub "`/`").
- Program pyta użytkownika o wpisanie drugiej liczby.
- Program oblicza wynik na podstawie wybranego operatora matematycznego.
- Program pyta, czy użytkownik chce kontynuować pracę z poprzednim wynikiem.
- Jeśli tak, program w pętli wykorzystuje poprzedni wynik jako pierwszą liczbę i powtarza proces obliczeń.
- Jeśli nie, program pyta użytkownika ponownie o pierwszą liczbę i czyści wszystkie wcześniejsze dane obliczeń.
- Dodaj logo z pliku art.py.

<div class="hint">
  Spróbuj narysować schemat blokowy, aby zaplanować swój program.
</div>

<div class="hint">
    Aby wywołać mnożenie ze słownika operacji, napisałbyś swój kod w ten sposób:

<code>result = operations["*"](n1= 5, n2= 3)</code>

wynik (result) byłby wtedy równy 15.
</div>