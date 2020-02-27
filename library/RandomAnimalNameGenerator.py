import random

#Define variables and create lists

#Start the randomising

class RandomAnimalNameGenerator:


    def __init__(self, generatedNames = []):
        
        self.beginningNames = ["Rock", "Croc", "Rabi", "Shar", "Prong", "Polar", "Grizzly", "Meer", "Para", "Arga", "Tyrant", "Ground", "Mynah", "Mega", "Chin", "Star", "Galacta", "Al", "Fer", "Por", "Arma", "Aoud", "Heli", "God"]
        self.endNames = ["drake", "rex", "dragon", "bit", "bear", "fish", "wolf", "raptor", "dillo", "poise", "ret", "chilla", "hog", "zilla", "cat", "tiger", "horn", "coprion"]
        self.generatedNames = generatedNames

    def generate(self, retry = 10):

        for i in range(retry):
            firstName = random.choice(self.beginningNames)
            lastName = random.choice(self.endNames)

            newName = firstName + ' ' + lastName

            if newName not in self.generatedNames:
                self.generatedNames.append(newName)
                return newName


        raise Exception("Couldn't generate a new name. Increase dictionary capacity.")