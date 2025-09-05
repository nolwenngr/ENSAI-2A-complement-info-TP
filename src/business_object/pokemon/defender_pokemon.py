from src.business_object.pokemon.Abstractpokemon import AbcPokemon

class Defender(AbcPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "Defender")

    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current) / 200
