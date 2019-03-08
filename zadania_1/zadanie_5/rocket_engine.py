class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False):
        self.name = name
        self.power = power
        self.working = working

        RocketEngine.count += 1

    def start(self):
        if not self.working:
            RocketEngine.all_power += self.power
            self.working = True

    def stop(self):
        if self.working:
            RocketEngine.all_power -= self.power
            self.working = False

    def __str__(self):
        return f'Silnik {self.name} o mocy {self.power} | Stan {"pracujący" if self.working else "nie pracujacy"}'
    
    def __del__(self):
        RocketEngine.count -= 1
        print('Usuwanie')

    @staticmethod
    def status():
        print(f'Count: {RocketEngine.count} | All_power: {RocketEngine.all_power}')
