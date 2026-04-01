import random

class WasteEnv:
    def __init__(self):
        self.areas = []
        self.steps = 0

    def reset(self):
        self.areas = [random.randint(20, 80) for _ in range(3)]
        self.steps = 0
        return self.areas

    def step(self, action):
        self.steps += 1

        # safety check
        if action < 0 or action >= len(self.areas):
            action = 0

        # clean selected area
        self.areas[action] = max(0, self.areas[action] - 10)

        # increase other areas
        for i in range(len(self.areas)):
            if i != action:
                self.areas[i] += 5

        # reward (lower garbage is better)
        reward = -sum(self.areas)

        done = self.steps >= 10
        return self.areas, reward, done, {}