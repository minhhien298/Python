class Person(object):
    """A simple class."""
    species = "Homo Sapiens"

    def __init__(self, name):   # Constructor
        """This is the initializer. It's a special method (see below).
        """
        self.name = name

    def __str__(self):          # Special method
        """This method is run when Python tries to cast the object to a string. Return this string when using print(), etc. """
        return self.name

    def rename(self, renamed):  # Regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))


kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

print(kelly)
