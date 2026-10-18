### Długość listy  
Możesz uzyskać długość listy (liczbę elementów w liście) lub długość ciągu znaków (liczbę znaków w ciągu) za pomocą funkcji `len()`. https://docs.python.org/3/library/functions.html#len  

### IndexError  
Kiedy spróbujesz uzyskać dostęp do elementu, który nie znajduje się w zakresie listy, otrzymasz błąd IndexError. Np.:  

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #To spowoduje błąd IndexError
```  

### Zagnieżdżone listy  
Możesz umieścić listy w innych listach, co nazywa się "zagnieżdżoną listą" lub "listą 2D". Np.:  

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#Lista wygląda w ten sposób: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```  
Możesz również przedstawić listę w formacie 2D w ten sposób:  
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]