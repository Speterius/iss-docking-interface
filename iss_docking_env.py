import time
from website_interface import iss_docking_interface
from website_interface.website_buttons import NoButtonError


class IssDockingEnvironment:
    """RL environment wrapper around the python - ISS Docker interface."""

    def __init__(self):
        # Python-web interface
        self.browser, self.iss = iss_docking_interface()

        # Minimum time-step between action and observation
        self.dt = 0.01

        # Keep track of (integer) time samples (int) and have a maximum episode sample limit
        self.t = 0
        self.T_max = 50

        # Discrete state-action space sizes:
        self.action_space = 6
        self.observation_space = 3

    def start(self) -> None:
        """Starting sequence to begin the simulation."""
        print("Attempting to click Begin to start simulation.")

        # Keep trying to click the start button:
        while True:
            try:
                self.iss.website.begin()
                break
            except NoButtonError:
                time.sleep(0.5)
                continue

        # Wait a bit for the simulation to load.
        print(f"Waiting 5 seconds for the simulation to load.")
        time.sleep(5.0)

    def reset(self) -> list:
        """Reset the simulation and return the states."""
        self.t = 0

        # Click the reset button
        self.iss.website.reset_states()

        # Have to wait a bit for the reset animation to end:
        time.sleep(3.0)

        # Return the states:
        # todo: use numpy array as return type
        return self.get_observation()

    def get_observation(self) -> list:
        """Define the observation vector."""
        # todo: use numpy array as return type
        # return [
        #     *self.iss.states.get_angles(),
        #     *self.iss.states.get_angular_rates(),
        #     *self.iss.states.get_positions(),
        #     self.iss.states.get_velocity(),
        #     self.iss.states.get_rotation_str(),
        #     self.iss.states.get_translation_str()
        # ]

        return [*self.iss.states.get_angles(), *self.iss.states.get_angular_rates()]

    def do_action(self, action_index: int) -> None:
        """Define which discrete index corresponds to which action and execute."""
        actions = [
            self.iss.actions.roll_left,
            self.iss.actions.roll_right,
            self.iss.actions.pitch_up,
            self.iss.actions.pitch_down,
            self.iss.actions.yaw_left,
            self.iss.actions.yaw_right,
        ]

        # Do the action
        actions[action_index]()

    def step(self, action: int) -> (list, float, bool, dict):
        """Do the action, wait a bit, observe states and return reward, done info."""

        # Do the action:
        self.do_action(action)

        # Wait a timestep:
        time.sleep(self.dt)

        # Observe MDP state:
        observation = self.get_observation()

        # Example reward function:
        reward = -(self.iss.states.get_angles()[0] ** 2)

        # Done condition: if the simulation failed or time expired:
        done = self.iss.website.is_retry_available() or self.t >= self.T_max

        # Info is empty dict for now:
        info = {}

        # Step the sample counter:
        self.t += 1

        return observation, reward, done, info

    def close(self):
        """The browser should be closed at the end of the session."""
        self.browser.close()
