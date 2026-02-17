class Zoo:
    """Задача: zoo"""
    def __init__(self):
        self.animals = []

    def add(self, animal_name: str):
        return self.animals.append(animal_name)
