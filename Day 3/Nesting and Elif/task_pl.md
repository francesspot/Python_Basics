### Zagnieżdżone instrukcje warunkowe  
Możesz umieszczać instrukcje if/else wewnątrz innych instrukcji if/else. Jest to znane jako zagnieżdżanie.  
np.

```
if maths_score >= 90:
    if english_score >= 90:
        print("Jesteś dobry we wszystkim")
    else:
        print("Jesteś dobry z matematyki")
if english_score >= 90:
    print("Jesteś dobry z angielskiego")
```

W tym przypadku tylko wtedy, gdy uczeń ma ponad 90 punktów z matematyki i angielskiego, otrzymuje komunikat "Jesteś dobry we wszystkim".  

Uwaga: Możesz również stosować instrukcje if, które nie mają sparowanej instrukcji else.