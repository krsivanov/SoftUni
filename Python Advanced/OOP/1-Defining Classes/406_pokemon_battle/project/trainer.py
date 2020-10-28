from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, *args):
        self.name = name
        self.pokemon = list(args)

    def add_pokemon(self, pokemon: Pokemon):
        pokemons = [p for p in self.pokemon if p.name == pokemon]
        if pokemon in pokemons:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return "Caught " + pokemon.pokemon_details()

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemons:
            self.pokemon.remove(pokemons[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            data += "- "+ p.pokemon_details() + "\n"
        return data

pokemon = Pokemon("Pikachu", 90)
pokemon2 = Pokemon("Kukachu", 200)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(pokemon2))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
