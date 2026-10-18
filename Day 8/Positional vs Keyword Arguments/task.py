# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet(name, greeting):
    print(f"{greeting} {name}!")

greet("Yo", "Jack")

def greet_with(name="Franciszek", location="Sulmierzyce"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack", "London")
greet_with()