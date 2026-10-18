### Wybierz swój poziom trudności
- **Normalny** 😎: Użyj wszystkich Wskazówek poniżej, aby ukończyć projekt.
- **Trudny** 🤔: Użyj tylko Wskazówek 1, 2, 3, aby ukończyć projekt.
- **Bardzo trudny** 😭: Użyj tylko Wskazówek 1 i 2, aby ukończyć projekt.
- **Ekspert** 🤯: Użyj tylko Wskazówki 1, aby ukończyć projekt.

### Zasady gry w Blackjacka w naszym domu gier

- Talia kart jest nieskończona.
- W grze nie ma jokerów.
- Walet/Dama/Król są warte 10 punktów.
- As może być wart 11 lub 1 punkt.
- Użyj poniższej listy jako talii kart:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- Karty w liście mają równą szansę na wylosowanie.
- Karty nie są usuwane z talii po ich wylosowaniu.
- Komputer pełni rolę rozdającego.

<div class="hint" title="Hint 1">
  Odwiedź tę stronę i zagraj w Blackjacka:

https://games.washingtonpost.com/games/blackjack/

Następnie wypróbuj ukończony projekt Blackjack tutaj:

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hint 2">
  Przeczytaj szczegółowy opis wymagań programu:

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Następnie spróbuj stworzyć własny schemat blokowy dla programu.
</div>

<div class="hint" title="Hint 3">
  Pobierz i przeczytaj ten schemat blokowy, który przygotowałem:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
</div>

<div class="hint" title="Hint 4">
  Stwórz funkcję <code>deal_card()</code>, która wykorzystuje poniższą listę do zwrócenia losowej karty.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Pamiętaj, że 11 to As.
</div>

<div class="hint" title="Hint 5">
  Rozdaj graczowi i komputerowi po 2 karty za pomocą funkcji <code>deal_card()</code> i metody <code>append()</code>.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hint 6">
  Stwórz funkcję o nazwie <code>calculate_score()</code>, która przyjmuje listę kart jako argument 
i zwraca sumę wszystkich kart w tej liście jako wynik. Poszukaj w Google funkcji <code>sum()</code>, aby to zrobić.
</div>

<div class="hint" title="Hint 7">
Wewnątrz <code>calculate_score()</code> sprawdź, czy masz blackjacka (układ z tylko 2 kartami: as + 10) i zwróć <code>0</code> zamiast faktycznego wyniku. Blackjack będzie w naszej grze reprezentowany przez wartość <code>0</code>.
</div>

<div class="hint" title="Hint 8">
  Wewnątrz <code>calculate_score()</code> sprawdź, czy w talii znajduje się 11 (as). Jeśli wynik przekracza 21, usuń 11 i zastąp go 1. Być może będziesz musiał poszukać w Google dokumentacji wbudowanych funkcji Pythona takich jak <code>append()</code> i <code>remove()</code>.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hint 9">
  Wywołaj funkcję <code>calculate_score()</code>. Jeśli komputer lub gracz ma blackjacka (0) lub wynik gracza przekracza 21, gra się kończy.
</div>

<div class="hint" title="Hint 10">
  Jeśli gra się nie skończyła, zapytaj gracza, czy chce dobrać kolejną kartę. Jeśli tak, użyj funkcji <code>deal_card()</code>, aby dodać kolejną kartę do listy <code>user_cards</code>. Jeśli nie, gra się kończy.
</div>

<div class="hint" title="Hint 11">
  Wynik musi być sprawdzany ponownie po każdym dobraniu karty, a kontrole z Wskazówki 9 muszą być powtarzane, aż gra się zakończy.
</div>

<div class="hint" title="Hint 12">
  Gdy gracz skończy, czas na ruch komputera. Komputer powinien dobierać karty, dopóki jego wynik wynosi mniej niż 17.
</div>

<div class="hint" title="Hint 13">
  Stwórz funkcję o nazwie <code>compare()</code> i przekaż do niej <code>user_score</code> oraz <code>computer_score</code>.

- Jeśli komputer i gracz mają ten sam wynik, jest remis.
- Jeśli komputer ma blackjacka (0), gracz przegrywa. 
- Jeśli gracz ma blackjacka (0), gracz wygrywa. 
- Jeśli wynik <code>user_score</code> przekracza 21, gracz przegrywa. 
- Jeśli wynik <code>computer_score</code> przekracza 21, komputer przegrywa. 
- Jeśli nic z powyższego, wygrywa gracz z wyższym wynikiem.
</div>

<div class="hint" title="Hint 14">
  Zapytaj gracza, czy chce zresetować grę. Jeśli odpowie "tak", wyczyść konsolę, uruchom nową grę w blackjacka i wyświetl logo z pliku art.py.
</div>