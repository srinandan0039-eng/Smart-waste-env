import random

class WasteEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.areas = [random.randint(20, 80) for _ in range(3)]
        self.steps = 0
        return self.areas

    def step(self, action):
        self.steps += 1

        # clean selected area
        self.areas[action] -= 10

        # increase others
        for i in range(3):
            if i != action:
                self.areas[i] += 5

        # reward (less garbage = better)
        reward = -sum(self.areas)

        done = self.steps >= 10
        return self.areas, reward, done, {}