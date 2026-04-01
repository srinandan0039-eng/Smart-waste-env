from waste_env import WasteEnv
import random

env = WasteEnv()

state = env.reset()
print("Initial State:", state)

done = False

while not done:
    action = random.randint(0, len(state) - 1)

    state, reward, done, _ = env.step(action)

    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print("-----")

print("Finished Successfully")