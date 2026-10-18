### Pseudolosowe generatory liczb
Komputery nie są losowe, ponieważ zostały zbudowane z użyciem obwodów i przełączników. Jednak losowość jest bardzo ważna przy tworzeniu oprogramowania, zwłaszcza gier. Byłoby naprawdę nudno, gdyby każdy ruch w grze wideo był z góry ustalony.

Dlatego niektórzy informatycy wynaleźli pseudolosowe generatory liczb, np. https://pl.wikipedia.org/wiki/Mersenne_Twister.

Jeśli chcesz dowiedzieć się więcej o pseudolosowych generatorach liczb, polecam obejrzenie tego filmu od Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### Moduł Random w Pythonie
Przeczytaj dokumentację tutaj:  
https://docs.python.org/3/library/random.html

Aby go użyć, musisz go najpierw zaimportować:

`import random`

### Losowe liczby całkowite w zakresie

```
import random
rand_num = random.randint(1, 10)

# To wygeneruje losową liczbę całkowitą z zakresu od 1 do 10 (włącznie).
```

### Moduły w Pythonie
Python pozwala nam umieszczać kod w różnych plikach i importować go, jeśli jest potrzebny. Oznacza to, że możemy lepiej organizować i modularyzować nasz kod.

Możesz utworzyć nowy moduł, po prostu tworząc nowy plik `.py`, a następnie możesz importować zmienne lub funkcje z tego pliku za pomocą słowa kluczowego `import`.

### Losowe liczby zmiennoprzecinkowe 
Możesz wygenerować losową liczbę z zakresu od 0.0 (włącznie) do 1.0 (bez włączenia) używając poniższego kodu z modułu random:

```
import random
rand_num_0_to_1 = random.random()
```
Można to również przedstawić w ten sposób:  

`0.0 <= random.random() < 1.0`

Zakres generowanych liczb losowych w tej metodzie można rozszerzyć za pomocą mnożenia.

Np. `random.random() * 5`

Wygeneruje liczbę losową z zakresu od 0 do 5.

Innym sposobem generowania losowych liczb zmiennoprzecinkowych jest użycie funkcji `uniform()`:

```
import random
random_float = random.uniform(1, 10)
# To wygeneruje losową liczbę zmiennoprzecinkową z zakresu od 1 do 10.
```
Ta metoda może, ale nie musi, uwzględniać górną granicę, w zależności od zaokrąglenia liczby zmiennoprzecinkowej.  
Najlepiej można to przedstawić jako:

`a <= random.uniform(a, b) <= b`

W zależności od tego, czy chcesz uwzględnić górną granicę, wybierzesz użycie `random.random()` lub `random.uniform()`.

### PAUZA 1 - Orzeł czy Reszka
Stwórz program rzutu monetą, korzystając z tego, czego nauczyłeś się o losowości w Pythonie. Powinien losowo drukować "Orzeł" lub "Reszka" za każdym razem, gdy zostanie uruchomiony.  

<div class="hint">
  Będziesz musiał pomyśleć o tym, czego nauczyłeś się o instrukcjach warunkowych w Pythonie.
</div>