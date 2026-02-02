# Game Engine for NFL Football Game

class GameEngine:
    def __init__(self):
        self.teams = []
        self.scoreboard = {}

    def add_team(self, team_name):
        self.teams.append(team_name)
        self.scoreboard[team_name] = 0

    def update_score(self, team_name, points):
        if team_name in self.scoreboard:
            self.scoreboard[team_name] += points
        else:
            raise ValueError("Team not found")

    def get_score(self):
        return self.scoreboard

    def reset_game(self):
        for team in self.teams:
            self.scoreboard[team] = 0
