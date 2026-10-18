### Zakres lokalny  
Zmienne (lub funkcje) zadeklarowane wewnątrz funkcji mają zakres lokalny (nazywany również zakresem funkcji). Są widoczne tylko dla innego kodu w tym samym bloku kodu.

np.  
```
def my_function():
    my_local_var = 2
    
# To spowoduje błąd NameError
print(my_local_var) 
```

### Zakres globalny  
Zmienne lub funkcje zadeklarowane na najwyższym poziomie (bez wcięcia) w pliku kodu mają zakres globalny. Są dostępne w dowolnym miejscu w pliku kodu.

np.  

```
my_global_var = 3

def my_function():
    # To działa bez problemu
    print(my_global_var)