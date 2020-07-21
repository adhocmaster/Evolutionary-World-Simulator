import math
from games.GoldHunters.localLib.GoldResource import GoldResource

class GHAgentActions:

    def dig(self, agent, resource):
        
        amountDug = resource.amountPerDig(agent.getDiggingRate())
        resource.deplete(amountDug)
        collectableAmount = math.ceil(amountDug * agent.getEfficiency())
        return collectableAmount


    def getMaxCollectableFromResource(self, agent, goldResource):
        
        amountDug = goldResource.amountPerDig(agent.getDiggingRate())
        collectableAmount = math.ceil(amountDug * agent.getEfficiency())
        return collectableAmount

    
    def getMaxCollectableFromResources(self, agent, resources):

        amount = 0
        maxAmount = agent.getDiggingRate() * agent.getEfficiency()

        for resource in resources:
            if isinstance(resource, GoldResource):
                amountFromThisResource = resource.amountPerDig(agent.getDiggingRate())
                if amount + amountFromThisResource <= maxAmount:
                    amount = amount + amountFromThisResource

        return amount


    