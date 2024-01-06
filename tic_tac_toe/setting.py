class Setting:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.cell_number = 3
        self.screen_width = 600
        self.screen_height = 600
        self.cell_width = self.screen_width // self.cell_number
        self.cell_height = self.screen_height // self.cell_number

        # Colors
        self.bg_color = (50, 50, 50)
        self.line_color = (202, 200, 202)
        self.circle_color = (235, 0, 126)
        self.cross_color = (0, 180, 236)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        self.radius_of_circle = self.cell_width / 3
