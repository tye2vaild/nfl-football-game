# Season Manager

class SeasonManager:
    def __init__(self, season_year):
        self.season_year = season_year
        self.current_week = 1
        self.franchise_mode = False

    def start_season(self):
        print(f"Starting the {self.season_year} season...")

    def end_season(self):
        print(f"Ending the {self.season_year} season...")

    def toggle_franchise_mode(self):
        self.franchise_mode = not self.franchise_mode
        mode = 'Franchise' if self.franchise_mode else 'Regular'
        print(f"Switched to {mode} mode.")

    def advance_week(self):
        self.current_week += 1
        print(f"Advanced to week {self.current_week}.")

# Example usage:
# manager = SeasonManager(2026)
# manager.start_season()
# manager.toggle_franchise_mode()
# manager.advance_week()