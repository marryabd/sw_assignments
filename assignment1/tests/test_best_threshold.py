import unittest
from modul_1.functions import find_best_threshold  # Ensure the function is correctly imported


class TestBestThreshold(unittest.TestCase):

    def test_normal_case(self):
        """Test with standard input values."""
        thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]
        tp = [50, 48, 45, 40, 35]
        tn = [30, 32, 33, 40, 50]
        fp = [10, 12, 14, 18, 20]
        fn = [5, 6, 7, 8, 9]

        result = find_best_threshold(thresholds, tp, fn, tn, fp)
        self.assertEqual(result, 0.1)

    def test_empty_input_lists(self):
        """Test handling of empty input lists."""
        with self.assertRaises(ValueError) as context:
            find_best_threshold([], [], [], [], [])
        self.assertTrue("All input lists must be non-empty." in str(context.exception))

    def test_non_negative_values(self):
        """Test that input values must be non-negative."""
        with self.assertRaises(ValueError) as context:
            find_best_threshold([0.1], [50], [-30], [10], [5])
        self.assertTrue("All inputs must be non-negative." in str(context.exception))

    def test_input_length_mismatch(self):
        """Test that all input lists must have the same length."""
        with self.assertRaises(ValueError) as context:
            find_best_threshold([0.1], [50, 48], [30], [10], [5])
        self.assertTrue("All input lists must have the same length." in str(context.exception))

    def test_all_zero_inputs(self):
        """Test the function's behavior with all zero values."""
        thresholds = [0.1, 0.2, 0.3]
        tp = [0, 0, 0]
        fn = [0, 0, 0]
        tn = [0, 0, 0]
        fp = [0, 0, 0]

        with self.assertWarns(UserWarning):
            result = find_best_threshold(thresholds, tp, fn, tn, fp)

        self.assertIsNone(result)

    def test_zero_tp_fn_combination(self):
        """Test the behavior when both TP and FN are zero for some thresholds."""
        thresholds = [0.1, 0.2, 0.3]
        tp = [0, 20, 30]  # First threshold has TP = 0
        fn = [0, 2, 3]  # First threshold has FN = 0
        tn = [5, 6, 7]
        fp = [0, 0, 0]

        with self.assertWarns(UserWarning):
            best_threshold = find_best_threshold(thresholds, tp, fn, tn, fp)

        # Since recall cannot be calculated for the first threshold, we expect
        # the best threshold to return one of the others if they meet recall >= 0.9.
        # If the function is working correctly, best_threshold should not be None.
        self.assertIsNotNone(best_threshold)


if __name__ == '__main__':
    unittest.main()
