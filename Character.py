class Character:

    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.hp = 10
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.quit = False
        self.kill = 0
        self.mission = ''
        self.mission_01 = 0
        self.mission_02 = 0

    def get_name(self):
        return self.name

    def get_x(self):
        """Returns the x-coordinate"""
        return self.x_coord

    def get_y(self):
        """Returns the y- coordinate"""
        return self.y_coord

    def set_x(self, new_coord):
        """sets and returns new x -coordinate"""
        self.x_coord = new_coord
        return new_coord

    def set_y(self, new_coord):
        """sets and returns new y -coordinate"""
        self.y_coord = new_coord
        return new_coord

    def get_hp(self):
        """Returns hp value"""
        return self.hp

    def set_hp(self, new_hp):
        """Sets the new hp value and return"""
        self.hp = new_hp
        return new_hp

    def increment(self):
        """Increase hp value by 1"""
        self.hp += 1

    def get_kill(self):
        """Returns number of kill"""
        return self.kill

    def increment_kill(self):
        self.kill += 1

    def get_mission(self):
        return self.mission

    def set_mission(self, your_mission):
        self.mission = your_mission
        return your_mission

    def get_mission_01(self):
        return self.mission_01

    def set_mission_01(self, mis_01):
        self.mission_01 = mis_01
        return mis_01

    def get_mission_02(self):
        return self.mission_02

    def set_mission_02(self, mis_02):
        self.mission_02 = mis_02
        return mis_02

    def get_quit(self):
        return self.quit

    def set_quit(self, now_quit):
        self.quit = now_quit
        return now_quit
