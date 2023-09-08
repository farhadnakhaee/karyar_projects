class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)
        self.ship_speed = 1
        self.bullet_speed = 1
        self.bullet_width = 500
        self.bullet_height = 12
        self.bullet_color = (160, 160, 0)
        self.bullets_allowed = 3
        self.alien_speed = 0.25
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        self.ship_limit = 3



