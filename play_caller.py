class PlayCaller:
    def __init__(self):
        self.plays = ["Run the ball", "Pass the ball", "Field goal attempt"]

    def call_play(self):
        import random
        return random.choice(self.plays)

if __name__ == '__main__':
    play_caller = PlayCaller()
    print("Play called:", play_caller.call_play())