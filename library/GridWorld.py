from library.World import World

class GridWorld(World):

    def __init__(self, size = (10, 10), name = 'A beautiful world', initialState = {}):
        
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
                id = self.getIdFromLocation(x, y)
                name = f'({id})'
                position = (x, y)
                self.createNode(id, name, position)
        pass

    def getIdFromLocation(self, x, y):
        return f'{x},{y}'

    def getNodeAt(self, x, y):
        return self.getNode(self.getIdFromLocation(x, y))

    

