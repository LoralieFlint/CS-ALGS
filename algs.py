""" Balanced Brackets """
# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

# By this logic, we say a sequence of brackets is balanced if the following conditions are met:

# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

# Function Description

# Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.

# isBalanced has the following parameter(s):

# s: a string of brackets
# Input Format

# The first line contains a single integer , the number of strings.
# Each of the next  lines contains a single string , a sequence of brackets.

# Constraints

# , where  is the length of the sequence.
# All chracters in the sequences ∈ { {, }, (, ), [, ] }.
# Output Format

# For each string, return YES or NO.
def is_balanced(string ): 

""" Arrays: Left Rotation """
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below. It should return the resulting array of integers.

# rotLeft has the following parameter(s):

# An array of integers .
# An integer , the number of rotations.
# Input Format

# The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

def rotLeft(a, d):

""" Insert a node at a specific position in a linked list """
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

# Example
#  refers to the first node in the list 


# Insert a node at position  with . The new list is 

# Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.

# insertNodeAtPosition has the following parameters:

# head: a SinglyLinkedListNode pointer to the head of the list
# data: an integer value to insert as data in your new node
# position: an integer position to insert the new node, zero based indexing
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the revised list
# Input Format

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
# The next line contains an integer , the data of the node that is to be inserted.
# The last line contains an integer .

# Constraints

# , where  is the  element of the linked list.
# .

def insertNodeAtPosition(head, data, position):

""" Inserting a Node Into a Sorted Doubly Linked List """
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
# Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.

# Example

#  refers to the list 

# Return a reference to the new list: .

# Function Description

# Complete the sortedInsert function in the editor below.

# sortedInsert has two parameters:

# DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

# int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

# Returns

# DoublyLinkedListNode pointer: a reference to the head of the list
# Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

# Input Format

# The first line contains an integer , the number of test cases.

# Each of the test case is in the following format:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the data for each node of the linked list.
# The last line contains an integer, , which needs to be inserted into the sorted doubly-linked list.
# Constraints

def sortedInsert(head, data):


""" Remove Nth Node From End of List """
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
"""


""" Two Sum """
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # input 
        dictionary = {}
    # output
        answer = []
        # for all nums in array
        for i in range(len(nums)):
            # targeted number in array - index of array
            secondNumber = target-nums[i]
            # if = second number return the keys of indexs in array
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                # if target is not met return array of numbers
                if(i != secondIndex):
                    return sorted([i, secondIndex])
            dictionary.update({nums[i]: i})

"""

""" 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""

""" 3sum """ 
# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
"""

""" Search Insert Position """
# https://leetcode.com/problems/search-insert-position/
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
"""