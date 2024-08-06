import Strings
import unittest
class TestStrings(unittest.TestCase):
    def setUp(self):
        self.obj = Strings.Strings()
    def test_strings(self):
        self.assertEqual(self.obj.strings(["Mary", "Gary", "Harry"],[1, 2, 0]),['Gary', 'Harry', 'Mary'])
        self.assertEqual(self.obj.strings(["Mary", "Gary", "Harry","gfdg","gdf","gdftry","fgd","5t5yfd","3rewr","ewwr","1e3","dghf"],[1, 2, 0, 7, 4, 9, 10, 3, 5, 6,8,11]),['Gary', 'Harry', 'Mary', "5t5yfd", "gdf", "ewwr", "1e3", "gfdg", "gdftry", "fgd", "3rewr", "dghf"])
        self.assertEqual(self.obj.strings([],[]),[])
    def test_strings2(self):
        self.assertEqual(self.obj.strings2([10, 1, 4, 3, 8, 5]),[4, 1, 8, 3, 10, 5])
        self.assertEqual(self.obj.strings2([10, 1, 4, 3, 8, 5, 534, 43543, 22344222]),[4, 1, 8, 3, 10, 5, 534, 43543, 22344222])
        self.assertEqual(self.obj.strings2([]),[])
unittest.main()
