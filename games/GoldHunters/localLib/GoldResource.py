from library.Resource import Resource
from library.ResourceType import ResourceType

class GoldResource(Resource):

    def __init__(self, quantity):
        self.quantity = quantity
        self.location = None
        pass


    def __str__(self):
        return(
            f"quantity: {self.quantity} "
            f"location: {self.location}"
        )
    
    def getQuantity(self):
        return self.quantity

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity
        pass
    
    def setLocation(self, location):
        self.location = location
        pass

    
    def getLocation(self):
        return self.location
    
    def amountPerDig(self, attemptedAmount):

        if self.quantity > attemptedAmount:
            return attemptedAmount
        
        return self.quantity

    
    def deplete(self, attemptedAmount):

        self.quantity = self.quantity - self.amountPerDig(attemptedAmount)
        
        
    def use(self):
        pass


