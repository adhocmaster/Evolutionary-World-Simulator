from library.Object import Object
class Node(Object):

    def __init__(self, id, name, position = None):

        super().__init__(id, name)
        
        self.position = position
        self.objects = []
        pass


    def __str__(self):
        return (
            f"id: {self.id} \n"
            f"name: {self.name} \n"
            f"position: {self.position} \n"
            f"objects: {self.objects} \n"
        )
        

    def add(self, object):
        self.objects.append(object)
        pass


    def remove(self, object):
        self.objects.remove(object)
        pass




