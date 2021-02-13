import unittest
import main


class TestTableMethods(unittest.TestCase):

    def test_makeTable_isStr(self):
        self.assertEqual(
            type(main.makeTable([{'a': '1'}, {'b': '2'}])), type(str()))

    def test_listToLine_isStr(self):
        self.assertEqual(
            type(main.listToLine([[1, 2], [3, 4]])), type(str()))
        self.assertEqual(type(main.listToLine(
            [[1, 2], [3, '4']])), type(str()))

    def test_load(self):
        self.assertEqual(type(main.load()), type(list()))


def test():
    t = TestTableMethods()
    t.test_makeTable_isStr()
    t.test_listToLine_isStr()
    t.test_load()


test()
