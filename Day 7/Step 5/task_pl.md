### TODO-1: 
- Zaktualizuj listę słów tak, aby używała `word_list` z pliku hangman_words.py

### TODO-2: 
- Zaktualizuj kod, aby korzystał z `stages` z pliku hangman_art.py

### TODO-3: 
- Zaimportuj `logo` z pliku hangman_art.py i wydrukuj je na początku gry.

### TODO-4: 
- Jeśli użytkownik wprowadził literę, którą już wcześniej zgadywał, wyświetl tę literę i poinformuj go o tym.
- Nie powinniśmy odejmować życia w takiej sytuacji.
- np. Już zgadywałeś tę literę a

### TODO-5: 
- Jeśli litera nie znajduje się w `chosen_word`, wyświetl tę literę i poinformuj, że nie znajduje się w słowie.
- np. Zgadywałeś literę d, która nie znajduje się w słowie. Tracisz życie.

### TODO-6: 
- Zaktualizuj kod poniżej, aby poinformować użytkownika, ile żyć mu pozostało.
```print("****************************<???>/6 ŻYĆ POZOSTAŁO****************************")```

### TODO-7: 
- Zaktualizuj polecenie print, aby podać użytkownikowi poprawne słowo, które próbował odgadnąć.
- np. `TO BYŁO <Correct Word>! PRZEGRAŁEŚ`