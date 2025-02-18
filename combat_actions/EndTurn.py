from combat_actions.CombatActions import CombatAction


class EndTurn(CombatAction):

    name: str = "EndTurn"

    def is_available(self, agent, current_position: tuple[int, int], grid, n_squares_height, n_squares_width):
        # EndTurn is always available
        return True
