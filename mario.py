class Mario:
    """ This class stores all the information needed for Mario"""
    def __init__(self, x: int, y: int, dir: bool):
        """ This method creates the Mario object
        @param x the starting x of Mario
        @param y the starting y of Mario
        @param dir a boolean to store the initial direction of Mario.
                True is facing right, False is facing left"""
        self.x = x
        self.y = y
        self.direction = dir
        # Here we are assuming Mario will be always placed at the first
        # bank at first position and it will have a 16x16 size
        self.sprite = (0, 0, 48, 16, 16)
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3
        self.big = False
        self.y_top = self.y - 80
        self.y_ground = self.y
        self.jumping = False
        self.falling = False
        self.over = False
        self.finish = False
        self.loose = False


    def move(self, direction: str, size: int):
        """This function makes Mario move for all the different directions, depending on the parameter"""
        self.size = size
        # Mario movement
        if direction.lower() == 'right':
            self.x += 4
            if not self.big:
                self.sprite = (0, 0, 48, 16, 16)
            elif self.big:
                self.sprite = (0, 0, 72, 16, 32)
        elif direction.lower() == 'left':
            # I am assuming that if it is not right it will be left
            self.x -= 4
            if not self.big:
                self.sprite = (0, 0, 48, -16, 16)
            elif self.big:
                self.sprite = (0, 0, 72, -16, 32)
            if self.x <= 0:
                self.x = 0
        elif direction.lower() == "up":
            self.over = False
            self.jumping = True
            if self.y > self.y_top:
                self.y -= 5
            else:
                self.jumping = False
                self.falling = True
        elif direction.lower() == "down":
            self.jumping = False
            self.falling = True
            self.over = True
            self.y += 5











