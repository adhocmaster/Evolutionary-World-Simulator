from library.Game import Game
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GoldResource import GoldResource
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld
from random import randint
class GoldHunters(Game):
    
    def __init__(self, worldSize = (3, 3)):

        self.agents = None
        self.world = None
        self.resources = None
        self.init(worldSize)

        pass


    def init(self, worldSize = (3, 3)):

        # 1. Create a gridworld
        self.world = GridWorld(size = worldSize)
        # 2. Create some agents
        self.createAgents()
        # 3. Put agents in the world (you will need to remove them from previous node, move the agent to the location and also add them to the corresponding node in the world)
        self.putAgentsInWorld()
        # 4. Create some gold resources
        self.createGoldResources()
        # 5. Put gold resources in the world.
        self.putGoldResourcesInWorld()
        # 6. Run the game loop.
        self.run()

        pass

    def createAgents(self):
        factory = GHAgentFactory()
        self.agents = [factory.buildDigger(), factory.buildRobber()]
        # self.agents = factory.buildDiggers(2)
        pass

    def putAgentsInWorld(self):

        for agent in self.agents:
            randomXLocation = randint(0,self.world.size[0] - 1)
            randomYLocation = randint(0,self.world.size[1] - 1)
            self.moveAgent(agent, (randomXLocation, randomYLocation))
        pass


    def moveAgent(self, agent, newLocation):

        print(f"moving agent {agent} to location {newLocation}")

        self.removeAgentFromOldLocation(agent)

        agent.updateAgentLocation(newLocation)

        print(f"adding agent {agent} to location {newLocation}")
        self.world.addToLocation(newLocation, agent)

        pass

    def removeAgentFromOldLocation(self, agent):
        
        try:
            oldLocation = agent.getLocation()
            print(f"removing agent {agent} from location {oldLocation}")
            self.world.removeFromLocation(oldLocation, agent)
        except NotFoundInTheWorld as e:
            pass
        except Exception as e:
            raise e
        
        pass

    def addAgent(self, agent, newLocation):
        self.agents.append(agent)


    def getAgents(self):
        return self.agents


    def createGoldResources(self):
        self.resources = []
        self.resources.append(GoldResource(2))
        pass

    def putGoldResourcesInWorld(self):
        for resource in self.resources:
            resource.setLocationX(randint(0, self.world.size[0]))
            resource.setLocationY(randint(0, self.world.size[1]))
        pass

    def changeState(self):
        allAgentActions = self.getAllAgentActions()
        self.updateGame(allAgentActions)
        pass

    def getAllAgentActions(self, agents):
        #map the return of payoff for agents in dictionary with key = agent and value = action
        #return the dictionary

    def updateGame(self, agentActions):
        #for each agent:
        #check action
        #if its move then call removeAgentFromOldLocation() and call moveAgentToNewLocation()
        #if agent digs, use a dig encounter with the agent by itself
        #if agent robs, use sabotage encounter?

    def run(self, timesToRun = 1000):
        # run the loop for timesToRun times

        pass
