from library.Resource import Resource
from library.ResourceType import Resourcetype

class GoldResource(Resource):

    def __init__(self, quantity):
        self.quantity = quantity
        self.value = 3
        self.locationX = None
        self.locationY = None
        pass
    
    def getQuantity(self):
        return self.quantity

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity
        pass

    def getValue(self):
        return self.value
    
    def setValue(self, newValue):
        self.value = newValue
        pass

    def getLocationX(self):
        return self.locationX

    def setLocationX(self, newLocationX):
        self.locationX = newLocationX
        pass

    def getLocationY(self):
        return self.locationY

    
    def setLocationY(self, newLocationY):
        self.locationY = newLocationY
        pass
    
    def attemptToDig(self, attemptedAmount):

        amountDug = attemptedAmount

        self.quantity -= attemptedAmount

        if self.quantity < 0:
           
            amountDug += self.quantity
            self.quantity = 0
            
        return amountDug
        
    def use(self):
        pass


