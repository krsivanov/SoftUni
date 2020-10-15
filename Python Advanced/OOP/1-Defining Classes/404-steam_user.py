from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game:str, hours: int):
        if game not in self.games:
            return f"{game} is not in library"
        self.played_hours += hours
        return f"{self.username} is playing {game}"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        return f"{game} is already in your library"

    def stats(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
