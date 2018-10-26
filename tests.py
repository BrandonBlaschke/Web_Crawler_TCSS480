import unittest
from main import popularLinks


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

if __name__ == '__main__':
    unittest.main()
