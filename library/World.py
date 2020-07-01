from abc import ABC, abstractmethod
from library.Node import Node

class World(ABC):

    def __init__(self, name, initialState = {}):
        self.name = name
        self.state = initialState
        self.nodes = {} # each node is a possible location in the world.
        pass

    
    def createNode(self, id, name, position):
        node = Node(id, name, position)
        self.nodes[id] = node
        pass
    

    def getNodes(self):
        return self.nodes


    def getObjectsAt(self, id):
        if id in self.nodes:
            return self.nodes[id].objects
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass
        
    
    def addToNode(self, id, object):

        if id in self.nodes:
            self.nodes[id].add(object)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass


    def removeFromNode(self, id, object):
        if id in self.nodes:
            self.nodes[id].remove(object)
        else:
            raise Exception(f"Node node in the world with id {id}")
        pass

    
