class ParenRep:
    def __init__(self, rep, unclosed, rl, rr):
        self.rep = rep
        self.unclosed = unclosed
        self.rl = rl
        self.rr = rr
    def isOpen(self):
        return self.unclosed > 0
    def addOpen(self):
        return ParenRep(self.rep + '(', self.unclosed+1, self.rl-1, self.rr)
    def addClose(self):
        return ParenRep(self.rep + ')', self.unclosed-1, self.rl, self.rr-1)
    def finished(self):
        return self.rl == 0 and self.rr == 0
    def __str__(self):
        return str({
            'rep': self.rep, 'rleft':self.rl, 'rright':self.rr, 'open':self.unclosed
        })
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [ParenRep('(', 1, n-1, n)]
        result = []
        while stack:
            curr = stack.pop()
            if not curr.isOpen():
                if curr.rl > 0: stack.append(curr.addOpen())
            else:
                if curr.rl > 0: stack.append(curr.addOpen())
                if curr.rr > 0: stack.append(curr.addClose())
            
            if curr.finished():
                result.append(curr.rep)
        return result