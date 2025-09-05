from src.business_object.Abstractpokemon import AbcPokemon

class Attacker(AbcPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "Attacker")

    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.attack_current) / 200