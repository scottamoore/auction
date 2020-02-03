import unittest
import utilities as util


class TestAuction(unittest.TestCase):

    def test_round_away_from_zero(self):
        self.assertEqual(util.round_away_from_zero(5.2), 6.0, "Should be 6.0")
        self.assertEqual(util.round_away_from_zero(4.9), 5.0, "Should be 5.0")
        self.assertEqual(util.round_away_from_zero(-5.2), -6.0, "Should be -6.0")
        self.assertEqual(util.round_away_from_zero(-8.7), -9.0, "Should be -9.0")

    def test_round_towards_zero(self):
        self.assertEqual(util.round_towards_zero(6.0), 6.0, "Should be 6.0")
        self.assertEqual(util.round_towards_zero(6.2), 6.0, "Should be 6.0")
        self.assertEqual(util.round_towards_zero(4.9), 4.0, "Should be 4.0")
        self.assertEqual(util.round_towards_zero(-5.2), -5.0, "Should be -6.0")
        self.assertEqual(util.round_towards_zero(-8.7), -8.0, "Should be -9.0")

    def test_calculate_threshold_value(self):
        #    q, t, p, lmbda, w, lower_val, upper_val, lowest_winning_bid)
        self.assertAlmostEqual(util.calculate_threshold_value(10, 24, 68.0, 30.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               23.9833, places=4, msg="Should be approximately 23.9833")
        self.assertAlmostEqual(util.calculate_threshold_value(10, 24, 68.0, 30.0/24.0, 0.5/24.0, 0.0, 100.0, 67.0), 
                               23.5500, places=4, msg="Should be approximately 23.5500")
        self.assertAlmostEqual(util.calculate_threshold_value(2, 24, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               23.6000, places=4, msg="Should be approximately 23.6000")
        self.assertAlmostEqual(util.calculate_threshold_value(2, 24, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 55.0), 
                               22.7000, places=4, msg="Should be approximately 22.7000")
        self.assertAlmostEqual(util.calculate_threshold_value(1, 24, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               11.8000, places=4, msg="Should be approximately 11.8000")
        self.assertAlmostEqual(util.calculate_threshold_value(1, 24, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 58.0), 
                               10.6000, places=4, msg="Should be approximately 10.6000")
        self.assertAlmostEqual(util.calculate_threshold_value(1, 55, 52.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               9.7167, places=4, msg="Should be approximately 9.7167")
        self.assertAlmostEqual(util.calculate_threshold_value(1, 55, 52.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 51.0), 
                               8.1833, places=4, msg="Should be approximately 8.1833")
        self.assertAlmostEqual(util.calculate_threshold_value(20, 72, 57.0, 30.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               35.9167, places=4, msg="Should be approximately 35.9167")
        self.assertAlmostEqual(util.calculate_threshold_value(20, 72, 57.0, 30.0/24.0, 0.5/24.0, 0.0, 100.0, 56.0), 
                               34.6333, places=4, msg="Should be approximately 34.6333")
        self.assertAlmostEqual(util.calculate_threshold_value(2, 72, 53.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               19.7167, places=4, msg="Should be approximately 19.7167")
        self.assertAlmostEqual(util.calculate_threshold_value(2, 72, 53.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 52.0), 
                               16.6000, places=4, msg="Should be approximately 16.6000")
        self.assertAlmostEqual(util.calculate_threshold_value(75, 168, 55.0, 40.0/24.0, 2.0/24.0, 0.0, 100.0, 0.0), 
                               76.1538, places=4, msg="Should be approximately 76.1538")
        self.assertAlmostEqual(util.calculate_threshold_value(75, 168, 55.0, 40.0/24.0, 2.0/24.0, 0.0, 100.0, 50.0), 
                               59.9833, places=4, msg="Should be approximately 59.9833")
        self.assertAlmostEqual(util.calculate_threshold_value(10, 168, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 0.0), 
                               109.9166666, msg="Should be approximately 109.91666", delta=0.000001)
        self.assertAlmostEqual(util.calculate_threshold_value(10, 168, 60.0, 5.0/24.0, 0.5/24.0, 0.0, 100.0, 57.0), 
                               102.6000, places=4, msg="Should be approximately 102.6000")
if __name__ == '__main__':
    unittest.main()