from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keymap = {}
        for idx, value in enumerate(nums):
            keymap[value] = idx

        for i, val in enumerate(nums):
            if target - val in keymap and keymap[target - val] != i:
                return i, keymap[target - val]
        return None

    def is_valid(s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or mapping.get(char) != stack.pop():
                    return False

        return not stack

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            temp = a + b
            a, b = b, temp
        return b

    # def firstUniqChar(self, s: str) -> int:
    #     keymap = {}
    #     array = [False] * len(s)
    #
    #     for i, x in enumerate(s):
    #         if x in keymap:
    #             idx = keymap[x]
    #             array[i] = True
    #             array[idx] = True  # mark as duplicate
    #         else:
    #             keymap[x] = i  # store index of first occurrence
    #     # print(array)
    #
    #     for i in range(len(s)):
    #         if not array[i]:
    #             return i
    #
    #     return -1
    def firstUniqChar(self, s: str) -> int:
        keymap = {}
        for x in s:
            keymap[x] = keymap.get(x, 0) + 1
        for i, x in enumerate(s):
            if x in keymap and keymap[x] == 1: return i
        return -1

    class Tnode:
        def __init__(self):
            self.child = [None] * 26

    def __init__(self):
        self.trie = {}
        self.root = Solution.Tnode()

    def build(self, words: List[str]) -> int:
        def insert(word: str) -> None:
            cur = self.root
            for c in word:
                idx = ord(c) - ord('a')
                if not cur.child[idx]:
                    cur.child[idx] = Solution.Tnode()
                cur = cur.child[idx]

        for x in words:
            insert(x[::-1])

        return self.dfs(self.root, 0)

    def dfs(self, node: 'Solution.Tnode', depth: int) -> int:
        if all(child is None for child in node.child):
            return depth + 1
        return sum(self.dfs(child, depth + 1) for child in node.child if child)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        return self.build(words)

    # 211 of leetcode

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.trie)

    def _search(self, word, i, node):
        if i == len(word):
            return '#' in node

        ch = word[i]
        if ch == '.':
            for key in node:
                if key != '#' and self._search(word, i + 1, node[key]):
                    return True
            return False
        elif ch in node:
            return self._search(word, i + 1, node[ch])
        else:
            return False


word = " hi "
sol = Solution()
d = {}

print(sol.firstUniqChar("bab"))
