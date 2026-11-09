# My first file tracked by Git
# Author: Òscar Pan Partagas
def greet(name):
 """Return a welcome message for the given name."""
 return f"Hello, {name}! Welcome to Git."
# This block runs only when the file is executed directly,
# not when it is imported as a module from another file.
README.md 2026-10-09
15 / 43
if __name__ == "__main__":
 print(greet("World")) # Call the greet function and print the result
