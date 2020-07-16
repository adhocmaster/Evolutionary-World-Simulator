from abc import ABC, abstractmethod

class Strategy(ABC):

    def update(self, agent):
        
        if self.needChange(agent):
            self.changeStrategy(agent)
        pass


    @abstractmethod
    def needChange(self, agent):
        pass



    @abstractmethod
    def changeStrategy(self, agent):
        pass



    @abstractmethod
    def getBestAction(self, agent):

        # mix up exploitation and exploration.
        pass
