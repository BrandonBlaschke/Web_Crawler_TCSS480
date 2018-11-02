import unittest
from main import popularLinks, updateCrawlSpace


# Test class to run some unit tests on the web crawler functions
class TestMethods(unittest.TestCase):

    def testMostPopMul(self):

        links = {'B': ['A'],
                 'A': ['B', 'C', 'D'],
                 'C': ['A', 'B'],
                 'D': ['A', 'B']}

        self.assertEqual(['A', 'B'], popularLinks(links))

    def testMostPopOne(self):
        links = {'B': ['A'],
                 'D': ['A', 'C'],
                 'C': ['A', 'D'],
                 'A': ['B']}

        self.assertEqual(['A'], popularLinks(links))

    def testMostPopNone(self):
        links = {'B': [],
                 'A': [],
                 'C': [],
                 'D': []}

        self.assertEqual([], popularLinks(links))

    def testCrawlSpaceNoDes(self):

        # Adding B To links
        links = {'A': ['B', 'C', 'D'],
                 'C': ['A', 'B'],
                 'D': ['A', 'B']}

        linksCorrect = {'B': [],
                 'A': ['B', 'C', 'D'],
                 'C': ['A', 'B'],
                 'D': ['A', 'B']}

        updateCrawlSpace('B', links)
        self.assertEqual(linksCorrect, links)

    def testCrawlSpaceDes(self):

        # Adding B and links
        links = {'A': ['B', 'C', 'D'],
                 'C': ['A', 'B'],
                 'D': ['A', 'B']}

        linksCorrect = {'B': ['A'],
                        'A': ['B', 'C', 'D'],
                        'C': ['A', 'B'],
                        'D': ['A', 'B']}

        updateCrawlSpace('B', links, des='A')
        self.assertEqual(linksCorrect, links)

    def testCrawlSpaceDupl(self):

        # Trying to add duplicate links
        links = {'B': ['A'],
                        'A': ['B', 'C', 'D'],
                        'C': ['A', 'B'],
                        'D': ['A', 'B']}

        linksCorrect = {'B': ['A'],
                        'A': ['B', 'C', 'D'],
                        'C': ['A', 'B'],
                        'D': ['A', 'B']}

        updateCrawlSpace('B', links, des='A')
        self.assertEqual(linksCorrect, links)


if __name__ == '__main__':
    unittest.main()
