Większość IDE (Inteligentne Środowiska Programistyczne), takie jak PyCharm, posiada wbudowane narzędzia do debugowania. Zwykle znane są one jako debuger. W pewnym sensie są one jak instrukcje `print`, ale znacznie bardziej zaawansowane.

Debugery pozwalają zajrzeć do naszego kodu podczas wykonywania, zatrzymać się na wybranych liniach, aby zrozumieć, jak działają wewnętrzne mechanizmy, i ustalić, gdzie występuje problem.

Istnieje kilka funkcji wspólnych dla większości IDE, które warto poznać:

1. **Punkt przerwania (Breakpoint)** - Możesz ustawić punkt przerwania, klikając w żłobek kodu (miejsce, gdzie znajdują się numery linii). W tym miejscu program zatrzyma się podczas uruchamiania w trybie debugowania.

2. **Przejdź Dalej (Step Over)** - Ten przycisk umożliwia przechodzenie przez wykonywanie kodu linia po linii oraz przeglądanie wartości pośrednich zmiennych.

3. **Wejdź w Kod (Step Into)** - Ta funkcja pozwala wejść do innych modułów, do których odnosi się Twój kod, np. jeśli użyjesz funkcji z modułu `random`, pokaże Ci oryginalny kod tej funkcji, abyś lepiej zrozumiał jej działanie i jak odnosi się do Twojego problemu.

4. **Wejdź w Mój Kod (Step Into My Code)** - Ta opcja działa tak samo jak „Wejdź w Kod”, ale ogranicza zakres do kodu Twojego projektu, pomijając kod z bibliotek, takich jak `random`.

### PAUZA 1  
Użyj debugera PyCharm, aby znaleźć problem w początkowym kodzie i go naprawić.