import random
from iss_docking_env import IssDockingEnvironment


def main():
    # Set up the environment:
    env = IssDockingEnvironment()

    # This is needed to let the website load.
    env.start()

    # Reset to initial states:
    obs = env.reset()

    def random_policy():
        return random.choice(range(env.action_space))

    while True:
        obs, reward, done, info = env.step(action=random_policy())

        print(f"observation (euler angles(3) and rates(3): {obs}")

        if done:
            break

    # Close the environment:
    print(f"Closing environment.")
    env.close()


if __name__ == "__main__":
    main()
