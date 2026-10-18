Możesz wymusić, aby kod pozwalał ci modyfikować coś za pomocą `global`, jeśli użyjesz słowa kluczowego `global` przed jego wykorzystaniem.

Na przykład: Ten kod spowoduje wystąpienie błędu

```
a = 1
def my_function():
    a += 1
    print(a)
```

Natomiast ten kod zadziała
```
a = 1
def my_function():
    global a
    a += 1
    print(a)