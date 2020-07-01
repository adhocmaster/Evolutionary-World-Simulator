from library.Object import Object
class Node(Object):

    def __init__(self, id, name, position = None):

        super(id, name)
        
        self.position = position
        self.objects = []
        pass


    def add(self, object):
        self.objects.append(object)
        pass


    def remove(self, object):
        self.objects.remove(object)
        pass




