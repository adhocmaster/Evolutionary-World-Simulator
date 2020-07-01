from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        pass