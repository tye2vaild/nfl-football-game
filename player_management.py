class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

class PlayerManager:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        self.players = [player for player in self.players if player.name != player_name]

    def list_players(self):
        for player in self.players:
            print(f'Name: {player.name}, Age: {player.age}, Position: {player.position}')