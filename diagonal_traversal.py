from collections import deque
def solve(self, A):
    if not A:
        return
    tem, p, res = A, deque(), []
    while True:
        if tem != None:
            res.append(tem.val)
            p.append(tem)
            tem = tem.right
        elif p:
            tem  =  p.popleft()
            tem = tem.left
        else:
            break
    return res