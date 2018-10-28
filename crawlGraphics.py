from tkinter import Tk, Canvas, Frame
from math import pi, cos, sin
from Node import Node

class CrawlGraphic(Frame):

    # Given a dictionary of the crawl space, will create graphical representation of it.
    def __init__(self, crawlSpace):
        self.crawlSpace = crawlSpace
        self.initUI()

    def initUI(self):

        # Create ids for each link
        ids = {}

        count = 0
        for i in self.crawlSpace.keys():
            ids[i] = count
            count += 1
        root = Tk()
        canvas = Canvas(root, width=900, height=900)
        canvas.pack()

        # Create all the nodes for the graph
        nodes = {}
        count = 0
        width = 12
        distanceFromCenter = 400
        offset = 450
        for i in self.crawlSpace.keys():
            angle = self.mapRange(count, 0, len(self.crawlSpace), 0, pi*2)
            x = distanceFromCenter * cos(angle) + offset
            y = distanceFromCenter * sin(angle) + offset
            nodes[i] = Node(x, y, count, i, self.crawlSpace[i])
            count += 1

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

            canvas.create_oval(x - width, y - width, x + width, y + width, outline='#f11', fill='#1f1', width=2)
            canvas.create_text(x + 2, y + 2, text=ids[i])
        root.mainloop()

    # Maps a val from one range to another range
    @staticmethod
    def mapRange(val, low1, high1, low2, high2):
        return (val - low1)/(high1 - low1) * (high2 - low2) + low2
