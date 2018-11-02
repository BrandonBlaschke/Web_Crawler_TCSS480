from tkinter import Tk, Canvas, Scrollbar, RIGHT, Y, X, BOTTOM, HORIZONTAL, VERTICAL
from math import pi, cos, sin
from node import Node


class CrawlGraphic:
    """ Draws the graph of a given crawlSpace"""

    def __init__(self, crawlSpace):
        """
        Given a dictionary of the crawl space, will create graphical representation of it.
        :param crawlSpace: Dictionary of the crawlSpace to display
        """
        self.crawlSpace = crawlSpace
        self.initUI()

    def initUI(self):
        """
        Starts the drawing process
        :return: Null
        """

        # Create ids for each link
        ids = {}

        count = 0
        for i in self.crawlSpace.keys():
            ids[i] = count
            count += 1

        root = Tk()

        canvas = Canvas(root, width=900, height=900, scrollregion=(0,0,1200,1200))

        sbarH = Scrollbar(root, orient=HORIZONTAL)
        sbarH.pack(side=BOTTOM, fill=X)
        sbarH.config(command=canvas.xview)

        sbarV = Scrollbar(root, orient=VERTICAL)
        sbarV.pack(side=RIGHT, fill=Y)
        sbarV.config(command=canvas.yview)

        canvas.config(xscrollcommand=sbarH.set)
        canvas.config(yscrollcommand=sbarV.set)
        canvas.pack()

        nodes = self.__createNodes__()

        self.__drawGraph__(nodes, canvas, ids)
        root.mainloop()

    def __createNodes__(self):
        """
         Private method to create nodes from a dictionary, used to reference when drawing nodes
        :return:
        """

        # Create all the nodes for the graph
        nodes = {}
        count = 0
        distanceFromCenter = 400
        offset = 450
        for i in self.crawlSpace.keys():
            angle = self.mapRange(count, 0, len(self.crawlSpace), 0, pi * 2)
            x = distanceFromCenter * cos(angle) + offset
            y = distanceFromCenter * sin(angle) + offset
            nodes[i] = Node(x, y, count, i, self.crawlSpace[i])
            count += 1
        return nodes

    def __drawGraph__(self, nodes, canvas, ids):
        """
        Draws the graph given nodes, canvas, and ids for the nodes
        :param nodes: Dictionary of Nodes from __createNodes__
        :param canvas: TK canvas for drawing
        :param ids: Ids of all the nodes
        :return: Null
        """

        width = 12
        # Draw dots and lines
        for i in self.crawlSpace.keys():
            print("Node " + str(ids[i]) + " " + i + " and Links:")
            x = nodes[i].x
            y = nodes[i].y

            for j in nodes[i].links:
                print('\t' + j)
                try:
                    canvas.create_line(x, y, nodes[j].x, nodes[j].y)
                except KeyError:
                    pass

            canvas.create_oval(x - width, y - width, x + width, y + width, outline='#000', fill='#FF9216', width=2)
            canvas.create_text(x + 2, y + 2, text=ids[i])

    @staticmethod
    def mapRange(val, low1, high1, low2, high2):
        """
        Maps a val from one range (low1 - to high1) to another range (low2 - high2)
        :param val: Val to map
        :param low1: Lower boundary 1
        :param high1: Higher boundary 1
        :param low2: Lower boundary 1
        :param high2: Higher boundary 2
        :return: Value within the new boundary
        """
        return (val - low1)/(high1 - low1) * (high2 - low2) + low2
