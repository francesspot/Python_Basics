Python różni się nieco od innych języków programowania tym, że nie posiada zakresu blokowego.

Oznacza to, że zmienne utworzone w zagnieżdżonych blokach kodu, np. w pętlach for, instrukcjach if, pętlach while itp., nie mają lokalnego zakresu. Otrzymują zakres funkcji, jeśli znajdują się w funkcji, lub zakres globalny, jeśli nie są w żadnej funkcji.

np.

```
# Dostępne w dowolnym miejscu
my_global_var = 1

def my_function():
    # Dostępne tylko wewnątrz my_function()
    my_local_var = 2
    
for _ in range(10):
    # Dostępne w dowolnym miejscu
    my_block_var = 3