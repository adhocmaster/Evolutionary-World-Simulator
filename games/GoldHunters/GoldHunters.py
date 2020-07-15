from library.Game import Game
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GoldResource import GoldResource
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld
from random import randint
class GoldHunters(Game):
    
    def __init__(self, worldSize = (3, 3), encounterEngine = None):

        self.agents = None
        self.world = None
        self.resources = None
        self.encounterEngine = encounterEngine
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
        # 6. do not Run the game loop.
        # self.run()

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
        self.updateGame()



    def updateGame(self):
        #for each agent:
        #check next action
        #if its move then call removeAgentFromOldLocation() and call moveAgentToNewLocation()
        #if agent digs, use a dig encounter with the agent by itself
        #if agent robs, use sabotage encounter?

        for agent in self.agents:
            action = agent.getNextAction()
            # TODO do whatever you want to do.

        self.doEncounters()

        pass


    def doEncounters(self):

        # iterate through all the nodes in the world. If any node has more than one agent, 
        # call playEncounter(self, agents, goldResource = None)
        pass
    

    def run(self, timesToRun = 1):
        # run the loop for timesToRun times

        for turn in range(timesToRun):

            self.runGameLoop(turn)

        pass


    def runGameLoop(self, turn):

        for agent in self.agents:
            agent.takeTurn(self.world, self.encounterEngine); # it updates nextAction property in an agent.
        self.updateGame()


