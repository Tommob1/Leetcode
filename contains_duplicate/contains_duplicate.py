import unittest
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]), "Should return False for an empty list")

    def test_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]), "Should return False for a list with no duplicates")

    def test_with_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 3]), "Should return True for a list with duplicates")

if __name__ == '__main__':
    unittest.main()
