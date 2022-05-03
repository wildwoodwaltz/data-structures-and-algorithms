from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        else:
            self.dogs.enqueue(animal)

    def dequeue(self, pref):
        if pref == "cat" and self.cats:
            return self.cats.dequeue()
        if pref == "dog" and self.dogs:
            return self.dogs.dequeue()
        else:
            return None


class Dog:
    pass


class Cat:
    pass
