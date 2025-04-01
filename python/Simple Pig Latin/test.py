import unittest
from simple_Pig_Latin import pig_it

class TestPigIt(unittest.TestCase):
    def test_pig_it(self):
        self.assertEqual(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('Hello world !'), 'elloHay orldway !')

if __name__ == '__main__':
    unittest.main()