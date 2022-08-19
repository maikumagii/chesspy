import unittest
import common.enums as enums

NOT_IMPLEMENTED = "Not Yet Implemented"

class TestEnums(unittest.TestCase):
  def test_color(self):
    self.assertEqual(int(enums.Color.WHITE.value), 0)
    self.assertNotEqual(int(enums.Color.WHITE.value), 1)
    self.assertEqual(int(enums.Color.BLACK.value), 1)
    self.assertNotEqual(int(enums.Color.BLACK.value), 0)

  def test_piece(self):
    self.skipTest(NOT_IMPLEMENTED)

  def test_coord(self):
    self.skipTest(NOT_IMPLEMENTED)