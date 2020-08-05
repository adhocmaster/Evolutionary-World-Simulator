import logging
logging.basicConfig(level=logging.INFO)

from library.Game import Game
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GoldResource import GoldResource
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld
from games.GoldHunters.localLib.GHMoveAction import GHMoveAction
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter

from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
from random import randint
class GoldHunters(Game):
    
    def __init__(self, worldSize = (3, 3), encounterEngine = None):

        self.agents = None
        self.world = None
        self.resources = None
        self.encounterEngine = encounterEngine
        if self.encounterEngine is None:
            logging.warning("creating the default encounter engine as none is supplied")
            self.encounterEngine = GoldHunterEncounter()

        self.actionsHandler = GHAgentActions()
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
        factory = GHAgentFactory(self.actionsHandler)
        self.agents = [factory.buildDigger(), factory.buildRobber()]
        # self.agents = factory.buildDiggers(2)
        pass

    def putAgentsInWorld(self):

        for agent in self.agents:
            randomXLocation = randint(0, self.world.size[0] - 1)
            randomYLocation = randint(0, self.world.size[1] - 1)
            self.moveAgent(agent, (randomXLocation, randomYLocation))
        pass


    def moveAgent(self, agent, newLocation):

        # TODO do not move if the there is no change in the location.

        logging.info(f"moving agent {agent} to location {newLocation}")

        self.removeAgentFromOldLocation(agent)

        agent.updateAgentLocation(newLocation)

        logging.info(f"adding agent {agent} to location {newLocation}")
        self.world.addAgentToLocation(newLocation, agent)

        pass

    def removeAgentFromOldLocation(self, agent):
        
        try:
            oldLocation = agent.getLocation()
            if self.world.hasLocation(oldLocation) is False:
                return

            logging.info(f"removing agent {agent} from location {oldLocation}")
            self.world.removeAgentFromLocation(oldLocation, agent)
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
            randomXLocation = randint(0, self.world.size[0] - 1)
            randomYLocation = randint(0, self.world.size[1] - 1)
            location = (randomXLocation, randomYLocation)
            resource.setLocation(location)
            logging.info(f"adding {resource} to {location}")
            self.world.addResourceToLocation(location, resource)
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

            # 1 if the action is a move event.
            if isinstance(action, GHMoveAction):
                newLocation  = self.actionsHandler.aLocationNearby(agent, action.direction, self.world)
                self.moveAgent(agent, newLocation)


        self.doEncounters()

        pass


    def doEncounters(self):

        encounterResults = []
        for location in self.world.locations():
            result = self.doEncounterAtLocation(location)
            if result is not None:
                encounterResults.append(result)
                self.updateAgentsAndResourcesFromEncounterResult(result)

        logging.debug(encounterResults)
        pass
    

    def updateAgentsAndResourcesFromEncounterResult(self, encounterResult):

        """
        { agent1Object: changedObject,
          agent2Object: changedObject,
          goldResource1: changed...
        }
        """

        for originalObject in encounterResult:
            changedObject = encounterResult[originalObject]
            if isinstance(originalObject, GoldResource):
                # TODO changed resource.
                self.updateResource(originalObject, changedObject)

            else:
                # this is an agent.
                self.updateAgent(originalObject, changedObject)
        
        pass


    def updateResource(self, originalObject, changedObject):
        #1. copy properties
        pass
    def updateAgent(self, originalObject, changedObject):
        #1. copy properties getPayoffFromEncounterResults
        pass


    def doEncounterAtLocation(self, location):

            agents = self.world.getAgentsAtLocation(location)
            if len(agents) < 2:
                return None # no encounter

            resources = self.world.getResourcesAtLocation(location)

            if len(resources) == 0:
                return self.encounterEngine.getEncounterResults(agents)

            else:
                # TODO encounter method does not handle more than one resource.
                return self.encounterEngine.getEncounterResults(agents, resources[0]) 


    def run(self, timesToRun = 1):
        # run the loop for timesToRun times

        for turn in range(timesToRun):

            self.runGameLoop(turn)
            for agent in self.agents:
                logging.info(agent.getResourceStats())

        pass


    def runGameLoop(self, turn):

        for agent in self.agents:
            self.actionsHandler.takeTurn(agent, self.world, self.encounterEngine) # it updates nextAction property in an agent.
        self.updateGame()






