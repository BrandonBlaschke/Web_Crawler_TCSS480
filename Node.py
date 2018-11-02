

class Node:
    """ Node class that stores position and other points to connect to """

    def __init__(self, x, y, id, link, links):
        """
        :param x: X coordinate
        :param y: Y coordinate
        :param id: ID number of the node that ties it to the link
        :param link: Link of this node
        :param links: List of links that this node is connected to
        """
        self.x = x
        self.y = y
        self.id = id
        self.link = link
        self.links = links

    def addPoint(self, x, y):
        """
         Add a point to (connection) to this Node
        :param x: X coordinate
        :param y: Y coordinate
        :return: Null
        """
        self.points.append((x,y))

    def __str__(self):
        """
        String representation of Node
        :return: String
        """
        return "I am id: " + str(self.id) + " my links are " + str(self.links)
