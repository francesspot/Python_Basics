Program zapyta:  
```
Ile liter chciałbyś mieć w swoim haśle?  
Ile symboli chciałbyś mieć?  
Ile liczb chciałbyś mieć?  
```

Celem jest pobranie odpowiedzi użytkownika na powyższe pytania, a następnie wygenerowanie losowego hasła. Wykorzystaj swoją wiedzę na temat list i pętli w Pythonie, aby rozwiązać to zadanie.

### Demo  
https://appbrewery.github.io/python-day5-demo/

### Łatwa wersja  
Wygeneruj hasło w kolejności. Najpierw litery, potem symbole, a na końcu liczby. Jeśli użytkownik chce:  

4 litery  
2 symbole oraz  
3 liczby  

hasło może wyglądać tak:  

`fgdx$*924`  

Zauważ, że wszystkie litery są razem. Wszystkie symbole znajdują się obok siebie, a liczby również występują kolejno. Spróbuj najpierw rozwiązać ten problem.  

<div class="hint">  
  Pamiętaj, że możesz użyć funkcji random.choice(), aby wybrać losowy element z listy! Ale najpierw musisz zaimportować moduł random.  
</div>  

### Trudna wersja  
Gdy ukończysz łatwą wersję, możesz spróbować trudniejszej wersji. W zaawansowanej wersji projektu końcowe hasło nie podąża za żadnym wzorcem. Więc powyższy przykład może wyglądać tak:  

`x$d24g*f9`  

Za każdym razem, gdy generujesz hasło, pozycje symboli, liczb i liter są różne. To sprawia, że hasło jest trudniejsze do złamania przez hakerów.  

Kluczowa umiejętność dobrego programisty to korzystanie z Google'a w celu znalezienia potrzebnych informacji. Twój mózg służy do myślenia, a nie zapamiętywania funkcji! Aby rozwiązać ten projekt na trudnym poziomie, będziesz musiał coś wyszukać w Google. Jeśli utkniesz, sprawdź poniższą wskazówkę, czego szukać.  

<div class="hint">  
  Spróbuj wyszukać: "How to shuffle items in a List in Python"  
</div>