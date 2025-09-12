import copy
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

    # Day 2 ------------------------------------------------------------------------------------------------------------

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

    # Day 3 ------------------------------------------------------------------------------------------------------------

    # Q = 648  Leetcode
    def b(self, dic: List[str]) -> None:

        for word in dic:
            d = self.trie
            for char in word:
                if char not in d:
                    d[char] = {}
                d = d[char]
            d["#"] = word

    def search2(self, word: str, i: int = 0, d: dict = None, n: List[str] = None) -> bool:
        if d is None: d = self.trie
        if i == len(word):
            if '#' in d:
                n.append(d.get('#'))
                return True
            else:
                return False
        if '#' in d:
            n.append(d.get('#'))
            return True
        return self.search2(word, i + 1, d[word[i]], n)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.b(dictionary)
        res = []
        for word in sentence.split():
            n = []
            res.append(n[0]) if self.search2(word, n=n) else res.append(word)
        return " ".join(res)

    # Day 4 ------------------------------------------------------------------------------------------------------------
    # 212 leetcode
    def b2(self, words: List[str]) -> None:
        for word in words:
            d = self.trie
            for char in word:
                if char not in d: d[char] = {}
                d = d[char]
            d['#'] = word

    def search3(self, word, board, i, y, idx, bools, d):
        if idx == len(word):
            return True

        if i < 0 or y < 0 or i >= len(board) or y >= len(board[0]) or bools[i][y]:
            return False

        char = board[i][y]
        if char != word[idx] or char not in d:
            return False

        bools[i][y] = True  # Mark cell as visited

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if self.search3(word, board, i + dx, y + dy, idx + 1, bools, d[char]):
                return True

        bools[i][y] = False  # Unmark

        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.b2(words)
        d = self.trie
        res = set()
        rows, cols = len(board), len(board[0])

        for word in words:
            found = False
            for i in range(rows):
                for j in range(cols):
                    bools = [[False for _ in range(cols)] for _ in range(rows)]
                    if self.search3(word, board, i, j, 0, bools, d):
                        res.add(word)
                        found = True
                        break
                if found:
                    break
        return list(res)

    # 78 -> Leetcode , subset
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        t = []

        def rec(i: int = 0):
            if i == len(nums): res.append(copy.deepcopy(t))

            t.append(nums[i])
            rec(i + 1)
            t.remove(nums[i])
            rec(i - 1)

        rec()
        return res

    # 98 -> Leetcode , subset II
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def dfs(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                # ✅ Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        values = []
        self.getV(root1, values)
        self.getV(root2, values)
        values.sort(key=lambda x: x.val)
        return values

    def getV(self, root1: TreeNode, val: list) -> None:
        self.getV(root1.left, val)
        val.append(root1.val)
        self.getV(root1.right, val)

    def isGood(self, nums: List[int]) -> bool:
        m = 0
        for num in nums: m = max(num, m)
        if len(nums) != m + 1: return False

        array = [False] * m
        c = 0
        for num in nums:
            if m == num: c += 1
            if num - 1 >= 0: array[num - 1] = True

        for x in array:
            if not x: return False
        return c == 2
