class Solution:
    def removeDuplicates(self, s: str) -> str:
        head_stack = []
        for char in s:
            if not head_stack or char != head_stack[-1]:
                head_stack.append(char)
            else:
                head_stack.pop()
        return ''.join(head_stack)