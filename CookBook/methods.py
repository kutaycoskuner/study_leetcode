class Point:
    x = 0.0
    y = 0.0

    def Set(self, x, y):
        self.x = x
        self.y = y

def Main():
    point = Point()
    point.Set(2,3)
    print("X: " + str(point.x) + ", Y: " + str(point.y))

if __name__ == "__main__":
    Main()