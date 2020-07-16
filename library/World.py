from abc import ABC, abstractmethod
from library.Node import Node

class World(ABC):

    def __init__(self, name, initialState = None):
        self.name = name
        
        if initialState is None:
            self.state = {} 
        else:
            self.state = initialState
            
        self.nodes = {} # each node is a possible location in the world.
        pass


    def __str__(self):
        nodeStr = ''
        for node in self.nodes.values():
            nodeStr = nodeStr + str(node)
        return (
            f"name: {self.name} \n"
            f"state: {self.state} \n"
            f"nodes: {nodeStr} \n"
        )
    
    @abstractmethod
    def createNodes(self):
        pass

    
    def createNode(self, id, name, position):
        node = Node(id, name, position)
        self.nodes[id] = node
        pass

    def getNode(self, id):
        return self.nodes[id]


    def getNodes(self):
        return self.nodes


    # def getObjectsAt(self, id):
    #     if id in self.nodes:
    #         return self.nodes[id].objects
    #     else:
    #         raise Exception(f"Node node in the world with id {id}")
    #     pass
        
    
    def addAgentToNode(self, id, agent):

        if id in self.nodes:
            self.nodes[id].addAgent(agent)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass


    def removeAgentFromNode(self, id, agent):
        if id in self.nodes:
            self.nodes[id].removeAgent(agent)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass

    
    def addResourceToNode(self, id, resource):

        if id in self.nodes:
            self.nodes[id].add(resource)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass


    def removeResourceFromNode(self, id, resource):
        if id in self.nodes:
            self.nodes[id].remove(resource)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass

    
