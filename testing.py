import unittest
from addtask import addtask

class TestAddTask(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(addtask(1, 2), 3)
    
    def test_add_floats(self):
        self.assertEqual(addtask(1.5, 2.5), 4.0)
    
    def test_add_negative_numbers(self):
        self.assertEqual(addtask(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(addtask(0, 0), 0)
        self.assertEqual(addtask(0, 3), 3)
        self.assertEqual(addtask(6, 0), 6)

if _name_ == '_main_':
    unittest.main()