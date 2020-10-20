from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            self.players.append(player)
            player.name = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        playerss = [p for p in self.players]
        if player_name not in playerss:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player_name)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for p in self.players:
            data += p.player_info()
        return  data


player = Player("George", 50, 100)
print(player)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shit Break", 20))

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())