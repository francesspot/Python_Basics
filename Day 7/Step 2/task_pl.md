### TODO-1
- Utwórz pusty ciąg znaków o nazwie `placeholder`.
- Dla każdej litery w `chosen_word` dodaj `_` do `placeholder`.
- Tak więc, jeśli `chosen_word` to "apple", `placeholder` powinien wyglądać jak `_ _ _ _ _`, gdzie 5 znaków `"_"` reprezentuje każdą literę do odgadnięcia.
- Wypisz `hint`.

<div class="hint">
  Pamiętaj, że możesz użyć funkcji range() wewnątrz pętli, aby wykonać akcję określoną liczbę razy.
</div>


### TODO-2
- Utwórz pusty ciąg znaków o nazwie `display`.
- Iteruj przez każdą literę w `chosen_word`.
- Jeśli litera na danej pozycji pasuje do `guess`, odsłoń tę literę w `display` na tej pozycji.
- np. jeśli użytkownik poda literę "p", a słowem do odgadnięcia było "apple", `display` powinien wyglądać jak `_ p p _ _`.
- Wypisz `display`, aby zobaczyć odgadniętą literę na właściwej pozycji.
- Jednak każda litera, która nie pasuje, jest reprezentowana przez "_".

<div class="hint">
  Pamiętaj, że pętla for przechodzi przez każdą literę w `chosen_word` w ustalonej kolejności. Możesz użyć tego faktu, aby stworzyć nowy ciąg, dodając literę lub "_".
</div>