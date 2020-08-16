
import unittest

from Testing.SampleProgram import eat


class SampleProgramTest(unittest.TestCase):
    def test_eatHealthy(self):
        self.assertEqual(eat("Veg"),"Healthy Food")

    def test_eatUnhealthy(self):
        self.assertEqual(eat("Non-Veg"), "Unhealthy Food")


if __name__ == "__main__":
    unittest.main()

