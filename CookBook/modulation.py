# import Vector2D 
from Modules.Vector2D import Vector2D #:: or alter * for everything
# https://stackoverflow.com/questions/2349991/how-to-import-other-python-files

def Main():
    vec1 = Vector2D(3,4)
    vec2 = Vector2D(5,5)

    print(str(vec1.x) + " " + str(vec1.y))

if __name__ == "__main__":
    Main()