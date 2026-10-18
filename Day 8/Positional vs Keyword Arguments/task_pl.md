### Wiele danych wejściowych
Możesz używać wielu danych wejściowych w funkcjach. Wystarczy oddzielić je przecinkiem `,`.

### PRZERWA 1 
Utwórz funkcję z wieloma danymi wejściowymi

<div class="hint">
  <code>
def greet(name, greeting):

    ____print(f"{greeting} {name}")
    
greet("Angela", "Yo!")
</code>
</div>

### PRZERWA 2
Zmodyfikuj funkcję tak, aby wypisywała oczekiwane wartości.
```
def greet_with(name, location)
    Witaj name
    Jak jest w location
```

### Argumenty pozycyjne
Domyślnie, kiedy tworzysz funkcję w Pythonie, zachowuje ona kolejność argumentów zgodnie z definicją funkcji.

Na przykład: W poniższej funkcji, pierwszy argument zawsze zostanie wypisany przed drugim. `a = 2, b = 1`

```
def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #Wypisze:
 # 2
 # 1
```

### Argumenty słowne
Możesz używać słów kluczowych, gdy przekazujesz argumenty przy wywoływaniu funkcji, aby było mniej niejasności, która wartość jest przypisana do którego parametru wejściowego.

### PRZERWA 3 
Wywołaj funkcję `greet_with()` używając argumentów słownych.

<div class="hint">
  <code>
greet_with(location="London", name="Angela")
</code>
</div>