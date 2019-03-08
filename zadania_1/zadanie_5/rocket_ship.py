from rocket_engine import RocketEngine

class RocketShip:
    def __init__(self):
        self.engines = []

    def manewruj(self):
        if RocketEngine.all_power < 50:
            self.engines.append(RocketEngine('maly', 25))
            self.engines.append(RocketEngine('maly', 25))
        else:
            while RocketEngine.all_power > 50:
                self.engines.pop()

    def rozpedzaj(self):
        if RocketEngine.all_power < 500 + 50:
            self.engines.append(RocketEngine('sredni', 250)
    