class Dot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y =y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

d1 = Dot(4,8)
print(f"Your dot is placed at {d1}")    