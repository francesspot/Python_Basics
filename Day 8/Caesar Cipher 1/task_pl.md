Będziesz tworzyć program do szyfrowania i deszyfrowania z użyciem [szyfru Cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara).

### Demo
https://appbrewery.github.io/python-day8-demo/

### TODO-1: 
Utwórz funkcję o nazwie `encrypt()`, która przyjmie `original_text` i `shift_amount` jako 2 argumenty.

### TODO-2: 
Wewnątrz funkcji 'encrypt' przesuwaj każdą literę z `original_text` do przodu w alfabecie o ilość określoną przez `shift_amount`, a następnie wyświetl zaszyfrowany tekst.

Możesz użyć wbudowanej w Python funkcji `index()`, aby znaleźć pozycję elementu na liście, np.:
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

Przykładowo, jeśli mamy następujące wartości:
```
plain_text = "hello"
shift_amount = 1
```
Ostateczny zaszyfrowany wynik powinien wyglądać następująco:

`Oto zakodowany wynik: ifmmp`

Gdzie każda litera z 'hello' jest przesunięta o 1 w górę. 

<div class="hint">
Rozłóżmy problem na części:

1. Potrzebujesz pętli for, aby iterować przez każdą literę w plain_text. 
2. Znajdź pozycję każdej litery na liście alfabetu.
3. Dodaj żądaną przez użytkownika wartość shift_amount do pozycji, aby uzyskać pozycję zaszyfrowanej litery.
4. Znajdź literę odpowiadającą tej pozycji.
5. Dodawaj każdą zakodowaną literę do nowego łańcucha znaków i wyświetl go po zakończeniu pętli.

</div>

### TODO-3: 
Wywołaj funkcję `encrypt()` i przekaż do niej dane wprowadzone przez użytkownika. Powinieneś być w stanie przetestować kod i zaszyfrować wiadomość.

### TODO-4: 
Co się stanie, jeśli spróbujesz przesunąć literę 'z' o 9 do przodu? Czy możesz poprawić kod?

<div class="hint">
Istnieje wiele podejść, które można zastosować.
1. Możesz dodać więcej niż jeden zestaw alfabetu do listy liter alfabetu.
2. Możesz dostosować wartość shift_amount tak, aby zawsze mieściła się w przedziale 0 - 25 i pasowała do listy.
3. Możesz skorzystać z operacji modulo, aby uzyskać resztę z dzielenia.
</div>