import random

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_point(self, points):
        self.score += points


def play_game():
    team1 = Team("Team A")
    team2 = Team("Team B")

    for quarter in range(1, 5):
        print(f"Quarter {quarter}:")
        team1_points = random.randint(0, 14)  # Simulate scoring points
        team2_points = random.randint(0, 14)
        team1.score_point(team1_points)
        team2.score_point(team2_points)
        print(f"{team1.name} scores {team1_points} points.")
        print(f"{team2.name} scores {team2_points} points.")
        print(f"Score after quarter {quarter}: {team1.name}: {team1.score}, {team2.name}: {team2.score}\n")

    print("Final Score:")
    print(f"{team1.name}: {team1.score}, {team2.name}: {team2.score}")

if __name__ == "__main__":
    play_game()