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
        self.bullet_width = 50
        self.bullet_height = 12
        self.bullet_color = (160, 160, 0)
        self.bullets_allowed = 3

        # Alien setting
        self.fleet_drop_speed = 20

        # How quickly the game speed up
        self.speedup_scale = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize setting that change throughout the game."""
        self.fleet_direction = 1
        self.ship_speed = 1
        self.bullet_speed = 1
        self.alien_speed = 5

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed setting."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

    def select_level(self, level):
        speed_multiplier = 1.0

        if level.lower() == "medium":
            speed_multiplier = 1.2
        elif level.lower() == "hard":
            speed_multiplier = 1.5

        self.ship_speed *= speed_multiplier
        self.bullet_speed *= speed_multiplier
        self.alien_speed *= speed_multiplier
