Możesz używać docstringów do pisania wielolinijkowych komentarzy, które dokumentują Twój kod.

### Składnia  
Wystarczy umieścić swój tekst pomiędzy trzema podwójnymi cudzysłowami.

np.  
```
"""
Mój
Wielolinijkowy
Komentarz
"""
```

### Dokumentowanie funkcji  
Ciekawą cechą docstringów jest to, że możesz ich używać tuż pod definicją funkcji, a tekst ten będzie wyświetlany po najechaniu na wywołanie funkcji. To dobry sposób, aby przypomnieć sobie, co robi funkcja, którą samodzielnie stworzyłeś.

np.  
```
def my_function(num):
    """Mnoży liczbę przez samą siebie."""
    return num * num