Pętle pozwalają nam nakazać komputerowi powtarzanie czynności bez konieczności wielokrotnego pisania tego samego kodu. Gdybyśmy chcieli, żeby komputer wypisał liczby od 1 do 100, byłoby bardzo uciążliwe wpisywanie instrukcji `print` dla każdej liczby lub nawet samo wypisywanie wszystkich liczb od 1 do 100. Pętle pozwalają nam stworzyć regułę, za którą komputer podąża, aby wykonać powtarzającą się czynność.

### Składnia

```
for <nazwa zmiennej dla każdego elementu> in <Lista>:
    <zrób coś>
    <zrób coś innego> 
```

### PAUZA 1 - Zostań komputerem
Przewidź, co zostanie wypisane przez poniższy kod:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### Wcięcia
Wcięcia są bardzo ważne w programowaniu w Pythonie. Za każdym razem, gdy używany jest symbol `:`, musisz zwrócić uwagę na wcięcia w liniach, które pojawiają się potem.

Np. Ten kod będzie działał zupełnie inaczej:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

niż ten kod:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")