class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Main():
    point = Point(2, 3)
    print("X: " + str(point.x) + ", Y: " + str(point.y))

if __name__ == "__main__":
    Main()