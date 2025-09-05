from src.business_object.Abstractpokemon import AbcPokemon

class Supporter(AbcPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "Supporter")

    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.defense_current) / 200