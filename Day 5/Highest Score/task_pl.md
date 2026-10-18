### Sum
Python posiada wiele wbudowanych funkcji, które pomagają nam pracować z liczbami. Jedna z nich umożliwia obliczenie sumy (całkowitej wartości).  
Np.
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
```
Ale jak działa `sum()` "za kulisami"? Kod został napisany przez osoby, które opracowały Pythona, i może wyglądać mniej więcej tak:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
```



### PAUZA 1 – Max
Python posiada również wbudowane metody takie jak `max()` i `min()`, które pozwalają przekazać listę liczb i zwracają najwyższą lub najniższą liczbę.

Twoim zadaniem jest odkrycie, jak programiści Pythona mogli stworzyć tę funkcjonalność, używając pętli i instrukcji warunkowych.

## ROZWIĄŻ TO ZADANIE BEZ UŻYWANIA max()

Masz podaną listę wyników egzaminów i musisz wydrukować najwyższy wynik z listy.  
Będziesz musiał użyć swojej wiedzy na temat list, pętli for i instrukcji warunkowych, aby wydrukować najwyższy wynik z listy student_scores.  
Na przykład, jeśli wyniki wyglądają następująco:
```
8 65 89 86 55 91 64 89
```
Twój kod powinien wydrukować
```
91