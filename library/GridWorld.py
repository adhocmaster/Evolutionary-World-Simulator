from library.World import World

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

    def addToLocation(self, location, obj):
        id = self.getIdFromLocation(location)
        super().addToNode(id, obj)
        pass


    def removeFromLocation(self, location, obj):
        id = self.getIdFromLocation(location)
        super().removeFromNode(id, obj)
        pass

    def getObjectsAtLocation(self, location):
        id = self.getIdFromLocation(location)
        return self.getNode(id).objects





    

