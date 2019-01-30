class Monster:

    def __init__(self):
        self.name = "EVIL MONSTER"
        self.hp = 5

    def get_hp(self):
        """return the hp value"""
        return self.hp

    def set_hp(self, new_hp):
        """Sets the new hp value and return"""
        self.hp = new_hp
        return self.hp

    def get_name(self):
        return self.name