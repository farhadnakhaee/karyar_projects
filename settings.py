class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)

        # Ship setting
        self.ship_limit = 3

        # Bullet setting
        self.bullet_width = 500
        self.bullet_height = 12
        self.bullet_color = (160, 160, 0)
        self.bullets_allowed = 3

        # Alien setting
        self.fleet_drop_speed = 20

        # How quickly the game speed up
        self.speedup_scale = 4

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize setting that change throughout the game."""
        self.fleet_direction = 1
        self.ship_speed = 1
        self.bullet_speed = 1
        self.alien_speed = 0.25

    def increase_speed(self):
        """Increase speed setting."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale





