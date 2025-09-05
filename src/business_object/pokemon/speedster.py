from src.business_object.Abstractpokemon import AbcPokemon

class Speedster(AbcPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "Speedster")

    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.sp_atk_current) / 200