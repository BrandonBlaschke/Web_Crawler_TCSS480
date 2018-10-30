

# Node class that stores position and other points to connect to
class Node:

    def __init__(self, x, y, id, link, links):
        self.x = x
        self.y = y
        self.id = id
        self.link = link
        self.links = links

    # Add a point (connection) to this Node
    def addPoint(self, x, y):
        self.points.append((x,y))

    # String representation of Node
    def __str__(self):
        return "I am id: " + str(self.id) + " my links are " + str(self.links)
