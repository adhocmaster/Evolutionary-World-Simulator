from abc import ABC, abstractmethod


class Game(ABC):

    def __init__(self, name, maxTurns, worldSize, maxPopulation):
        self.name = name
        self.maxTurns = maxTurns
        self.currentTurn = 0

        self.worldSize = worldSize
        self.maxPopulation = maxPopulation

        pass


    @abstractmethod
    def create(self):
        pass


    @abstractmethod
    def addAgent(self, agent, location):
        pass


    @abstractmethod
    def getAgents(self):
        pass