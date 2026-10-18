Możesz utworzyć prostą kolekcję uporządkowanych elementów za pomocą listy w Pythonie, np.

`fruits = ["Cherry", "Apple", "Pear"]`

lub

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### dostęp do elementów na listach

Możesz podać nazwę listy, a następnie nawias kwadratowy oraz indeks elementu, który chcesz. np.

`states_of_america[0]`

da ci "Delaware".

Pamiętaj, że w świecie komputerów zaczynamy liczyć od liczby 0, nigdy od 1. 0, 1, 2, 3 zamiast 1, 2, 3, 4.

### ujemne indeksy

Możesz uzyskać dostęp do elementów na liście, licząc od końca listy, za pomocą ujemnych liczb całkowitych. np.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #to będzie "Pear"
```

### modyfikowanie elementów
Możesz użyć tej samej składni, aby uzyskać dostęp do elementów listy, aby je zmodyfikować. np.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits zmieni się teraz na ["Orange", "Apple", "Pear"]
```

### dodawanie elementów
Możesz dodać elementy na koniec listy za pomocą funkcji `append()`. np.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits zmieni się teraz na ["Cherry", "Apple", "Pear", "Orange"]
```

### dokumentacja list
Możesz znaleźć dokumentację dotyczącą list w Pythonie oraz innych funkcji związanych z listami tutaj: https://docs.python.org/3/tutorial/datastructures.html