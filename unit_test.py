import unittest 
import main

class test(unittest.TestCase):

    def test_program(self):
        self.assertEqual(main.builder("Graph.csv",'A','B'),5)
        self.assertEqual(main.builder("Graph.csv",'B','A'),5)
        self.assertEqual(main.builder("Graph.csv",'C','F'),10)
        self.assertEqual(main.builder("Graph.csv",'F','G'),8)
        self.assertEqual(main.builder("Graph.csv",'F','C'),10)
if __name__ == "__main__":
    unittest.main()