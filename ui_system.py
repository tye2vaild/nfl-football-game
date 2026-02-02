# UI and HUD System

class UI:
    def __init__(self):
        self.hud = HUD()
        self.setup()

    def setup(self):
        # Initialize UI components
        pass

    def display(self):
        # Logic to display the UI
        pass

class HUD:
    def __init__(self):
        self.score = 0
        self.time = 0

    def update(self, score, time):
        self.score = score
        self.time = time
        self.render()

    def render(self):
        # Logic to render the HUD
        print(f"Score: {self.score}, Time: {self.time}")
