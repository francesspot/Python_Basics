Napraw wszelkie błędy (czerwone podkreślenia), które pojawiają się w edytorze, zanim uruchomisz swój kod. Ostrzeżenia (żółte) to opcjonalne poprawki, czasami mogą powodować problemy w późniejszym etapie, innym razem są nieszkodliwe, a edytor po prostu nie rozumie, co próbujesz zrobić.

### Obsługa wyjątków
W Pythonie możesz użyć bloku try/except, aby wychwycić wszelkie wyjątki, które mogą się pojawić. Na przykład, jeśli wyobrażasz sobie, że istnieje możliwość błędu użytkownika. Możesz zapobiec awarii swojego kodu, przewidując ten błąd. Niebezpieczny kod umieszczasz wewnątrz bloku try i używasz bloku except, aby przechwycić potencjalne błędy. Następnie określasz, co powinno się stać, gdy błąd wystąpi, zamiast po prostu przerwać działanie kodu.

np.

```
try:
    print(6 > "five")
except TypeError:
    print("Nie możesz porównywać liczb całkowitych i ciągów znaków")
```

### pauza 1 
Napraw błąd tak, aby instrukcja print wyświetlała poprawną wartość zmiennej age w obszarze wynikowym.