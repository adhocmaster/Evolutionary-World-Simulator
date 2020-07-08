from library.Game import Game
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GoldResource import GoldResource
from random import randint
class GoldHunters(Game):
    
    def __init__(self):

        self.agents = None
        self.world = None
        self.resources = None
        self.init()

        pass


    def init(self):

        # 1. Create a gridworld
        self.world = GridWorld()
        # 2. Create some agents
        self.createAgents()
        # 3. Put agents in the world (you will need to remove them from previous node, move the agent to the location and also add them to the corresponding node in the world)
        self.putAgentsInWorld(self.agents)
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
        pass

    def putAgentsInWorld(self, agents):
        for agent in agents:
            randomXLocation = randint(0,self.world.size[0])
            randomYLocation = randint(0,self.world.size[1])
            agent.moveTo(randomXLocation, randomYLocation)
        pass


    def addAgent(self, agent, newLocation):
        oldLocation = agent.getLocation()
        oldNode = self.world.getNodeAt(oldLocation[0], oldLocation[1])
        oldNode.remove(agent)

        agent.moveTo(newLocation[0], newLocation[1])

        newNode = self.world.getNodeAt(newLocation[0], newLocation[1])
        newNode.add(agent)

        self.agents.append(agent)


    def getAgents(self):
        return self.agents


    def createGoldResources(self):
        self.resources = []
        self.resources.append(GoldResource(2))
        pass

    def putGoldResourcesInWorld(self):
        for resource in self.resources:
            resource.setLocationX(randint(0, self.world(0)))
            resource.setLocationY(randint(0, self.world(1)))
        pass

    def run(self, timesToRun = 1000):
        # run the loop for timesToRun times

        pass
