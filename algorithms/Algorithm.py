from abc import ABC, abstractmethod
import random
from State import State
from combat_actions.CombatActions import CombatAction


class Algorithm(ABC):

    def __init__(self, max_epsilon: float = 0, epsilon_decay_rate: float = 1):
        self.epsilon_decay_rate = epsilon_decay_rate
        self.epsilon = max_epsilon

    @abstractmethod
    def exploit_best_action(self, state: State, available_actions: list[CombatAction]) -> CombatAction:
        pass

    @abstractmethod
    def learn(self, state, action, reward, next_state, done, **kwargs):
        pass

    @abstractmethod
    def save_value_function(self, pickle_filename):
        pass

    def epsilon_greedy(
        self, state: State, available_actions: list[CombatAction], linear_decay_over_episodes
    ) -> CombatAction:
        if self.epsilon_decay_rate == "linear_over_episodes":
            self.epsilon = 1 - linear_decay_over_episodes  # linear decay over all episodes
        elif self.epsilon_decay_rate == "half_linear_over_episodes":
            self.epsilon = 1 - (linear_decay_over_episodes / 2)  # half-linear decay over all episodes
        else:
            self.epsilon = self.epsilon * self.epsilon_decay_rate
        # Explore
        if random.random() < self.epsilon:
            return random.choice(available_actions)

        # Exploit
        return self.exploit_best_action(state, available_actions)
