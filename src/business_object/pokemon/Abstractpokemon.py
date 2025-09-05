import copy

from business_object.statistic import Statistic

from abc import ABC, abstractmethod

class AbcPokemon(ABC):

    def __init__(
        self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None
    ):
        self._stat_max: Statistic = stat_max
        self._stat_current: Statistic = stat_current
        self._level: int = level
        self._name: str = name
        self._type: str = type_pk
    
    @abstractmethod
    def get_pokemon_attack_coef(self):
        pass

    def level_up(self):
        self._level += 1

    def reset_actual_stat(self) -> None:
        self._stat_current = copy.deepcopy(self._stat_max)

    def get_hit(self, damage) -> None:
        """
        Decrease health point when receiving damages
        """
        if damage > 0:
            if damage < self.hp_current:
                self.hp_current -= damage
            else:
                self.hp_current = 0

    def __str__(self):
        res = "I am " + str(self.name)
        res += ", level : " + str(self.level)
        res += ", attack coef : " + str(self.get_pokemon_attack_coef())
        return res
