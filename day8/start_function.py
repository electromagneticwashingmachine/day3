def greet():
    print("Greetings!")
    print("How do you do?")
    print("Isn't the weather nice todat?")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Greetings! {name}")
    print(f"How do you do? {name}")
    print("Isn't the weather nice todat?")

greet_with_name("Tyron")


# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="Nowhere", name="Jaks")
