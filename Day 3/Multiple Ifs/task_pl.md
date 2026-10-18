Możesz napisać dowolną liczbę instrukcji if, aby sprawdzić różne warunki, które nie są ze sobą powiązane.  
Porównaj poniższe bloki kodu:  
```
# If/elif/else
if <warunek 1 jest spełniony>
    <zrób A>
elif <warunek 2 jest spełniony>
    <zrób B>
else
    <zrób C>
```
```
# Zagnieżdżone instrukcje if
if <warunek 1 jest spełniony>
    <zrób A>
    if <warunek 2 jest spełniony>
        <zrób B>
        if <warunek 3 jest spełniony>
            <zrób C>
```

```
# Wiele instrukcji if
if <warunek 1 jest spełniony>
    <zrób A>
if <warunek 2 jest spełniony>
    <zrób B>
if <warunek 3 jest spełniony>
    <zrób C>
```

W bloku if/elif/else tylko jedna z akcji (A, B lub C) może się wykonać, ponieważ if/elif/else są wzajemnie wykluczające się. Pierwszy warunek musi być nieprawdziwy, aby przejść do elif, a elif (lub kilka elif) muszą być nieprawdziwe, aby przejść do else. Warunek 2 jest sprawdzany tylko wtedy, gdy warunek 1 jest fałszywy.

W zagnieżdżonych instrukcjach if wszystkie akcje (A, B i C) mogą się wykonać, ale warunki 1, 2 i 3 muszą być spełnione. Komputer sprawdzi warunek 2 tylko wtedy, gdy warunek 1 jest prawdziwy.

W przypadku wielu instrukcji if, wszystkie akcje (A, B i C) mogą się wykonać. Ale są one całkowicie niezależne od siebie. C może się zdarzyć, nawet jeśli A i B się nie zdarzą. Każdy warunek jest sprawdzany, niezależnie od wyniku pozostałych.