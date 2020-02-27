class Trait:

    def __init__(self, name, actions, offensiveActions, defensiveActions):
        self.name = name
        self.actions = actions
        self.offensiveActions = offensiveActions
        self.defensiveActions = defensiveActions

        pass


    def __str__(self):

        actions = [str(action) for action in self.actions]
        offensiveActions = [str(action) for action in self.offensiveActions]
        defensiveActions = [str(action) for action in self.defensiveActions]

        return f"""
        name: {self.name}
        actions: {actions}
        offensiveActions: {offensiveActions}
        defensiveActions: {defensiveActions}
        """