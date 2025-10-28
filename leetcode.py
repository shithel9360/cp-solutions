"""
=====================================================
Leetcode Problem Solution Template
=====================================================
Platform: Leetcode
Author: [Your Name]
Problem: [Problem Number - Problem Name]
Difficulty: [Easy/Medium/Hard]
Link: [Problem URL]
=====================================================
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import math

"""
=====================================================
EXAMPLE SOLUTION: Two Sum (Leetcode #1)
Problem: Find indices of two numbers that add up to target
Time Complexity: O(n)
Space Complexity: O(n)
=====================================================
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Example solution using hash map approach.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers
        """
        # Dictionary to store value -> index mapping
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our seen dictionary
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found
        return []


"""
=====================================================
PROBLEM SOLVING TEMPLATE
Use this as a starting point for new problems
=====================================================
"""

class SolutionTemplate:
    def problemName(self, param1: List[int], param2: int) -> int:
        """
        Problem description here.
        
        Approach:
        1. Analyze the problem
        2. Identify patterns or known algorithms
        3. Implement the solution
        4. Test with examples
        
        Time Complexity: O(?)
        Space Complexity: O(?)
        
        Args:
            param1: Description
            param2: Description
            
        Returns:
            Description of return value
        """
        # Initialize variables
        result = 0
        
        # Main logic here
        # ...
        
        return result


"""
=====================================================
COMMON UTILITY FUNCTIONS
=====================================================
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper functions
def print_array(arr: List[int]) -> None:
    """Print array in readable format."""
    print(f"[{', '.join(map(str, arr))}]")


def binary_search(arr: List[int], target: int) -> int:
    """Standard binary search implementation."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Testing the solution
if __name__ == "__main__":
    # Example test case
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")  # Expected: [0, 1]
    print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}")
