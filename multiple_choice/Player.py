class Player:
    def __init__(self, name, role, kd):
        self.name = name
        self.role = role
        self.kd = kd

    def on_honor_roll(self):
        if self.kd >= 3.5:
            return True
        else:
            return False
