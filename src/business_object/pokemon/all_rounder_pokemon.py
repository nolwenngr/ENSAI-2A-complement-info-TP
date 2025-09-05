from src.business_object.Abstractpokemon import AbcPokemon

class AllRounder(AbcPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "All rounder")

    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
