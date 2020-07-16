from library.Object import Object
class Node(Object):

    def __init__(self, id, name, position = None):

        super().__init__(id, name)
        
        self.position = position
        self.agents = []
        self.resources = []
        pass


    def __str__(self):
        return (
            f"id: {self.id} \n"
            f"name: {self.name} \n"
            f"position: {self.position} \n"
            f"objects: {self.agents} \n"
            f"objects: {self.resources} \n"
        )
        

    def addAgent(self, agent):
        self.agents.append(agent)
        pass


    def removeAgent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)
        pass


    def addResource(self, resource):
        self.resources.append(resource)
        pass


    def removeResource(self, resource):
        if resource in self.resources:
            self.resources.remove(resource)
        pass




