from library.World import World
from library.Agent import Agent
from library.Resource import Resource

class GridWorld(World):

    def __init__(self, size = (10, 10), name = 'A beautiful world', initialState = None):
        
        super().__init__(name, initialState)

        self.size = size

        self.createNodes()

        pass


    def __str__(self):
        baseRep = super().__str__()
        return (
            f"size: {self.size} \n {baseRep}"            
        )


    def createNodes(self):
        print(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                id = self.getIdFromLocation((x, y))
                name = f'({id})'
                position = (x, y)
                self.createNode(id, name, position)
        pass

    def getIdFromLocation(self, location):
        return f'{location[0]},{location[1]}'

    def getNodeAt(self, location):
        """
        for test purposes. don't use in code.
        """
        return self.getNode(self.getIdFromLocation(location))

    def addAgentToLocation(self, location, agent):
        id = self.getIdFromLocation(location)
        super().addAgentToNode(id, agent)
        pass


    def removeAgentFromLocation(self, location, agent):
        id = self.getIdFromLocation(location)
        super().removeAgentFromNode(id, agent)
        pass

    def addResourceToLocation(self, location, resource):
        id = self.getIdFromLocation(location)
        super().addResourceToNode(id, resource)
        pass


    def removeResourceFromLocation(self, location, resource):
        id = self.getIdFromLocation(location)
        super().removeResourceFromNode(id, resource)
        pass

    def getAgentsAtLocation(self, location):
        # TODO the client should cache the results per turn

        id = self.getIdFromLocation(location)
        return self.getNode(id).agents


    def getResourcesAtLocation(self, location):
        # TODO the client should cache the results per turn

        id = self.getIdFromLocation(location)
        return self.getNode(id).resources


    def locations(self):
        for x in self.size[0]:
            for y in self.size[1]:
                yield (x, y)


    def hasLocation(self, location):

        if location[0] >= self.size[0] or location[1] >= self.size[1] or location[0] < 0 or location[1] < 0:
            return False
            
        return True

    

