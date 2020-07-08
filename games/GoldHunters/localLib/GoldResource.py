from library.Resource import Resource
from library.ResourceType import Resourcetype


class GoldResource(Resource):
    

    def __init__(self, quantity):
        super().__init__('gold', quantity, type=Resourcetype.GOLD)
    

    def getQuantity(self):
        return self.quantity

        
    def attemptToDig(self, attemptedAmount):

        amountDug = attemptedAmount

        self.quantity -= attemptedAmount

        if self.quantity < 0:
           
            amountDug -= self.quantity
            self.quantity = 0
            
        return amountDug

    def use(self):
        pass
