from library.Agent import Agent
from library.Action import Action


class AgentFactory:

    def build(self, type, id):
        return Agent(type = type, id = id)


