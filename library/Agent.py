from abc import ABC, abstractmethod

class Agent(ABC):

    def __init__(self, type, id):
        self.type = type
        self.id = id

        pass