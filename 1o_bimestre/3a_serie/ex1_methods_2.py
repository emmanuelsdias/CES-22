import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def speak():
        """ This method should print the animal sound """


class Dog(Animal):
    def speak():
        print("Woof!")


class Cat(Animal):
    pass


# Dog class implemented speak method, but Cat class didn't
# We can instantiate Dog class, but not Cat class
# There will be a TypeError
marley = Dog()
garfield = Cat()