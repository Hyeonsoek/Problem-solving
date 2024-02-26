import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
indexes = [ 0 ] * (n + 1)

for x in range(n):
    indexes[inorder[x]] = x

tree = [[0, 0] for _ in range(n + 1)]

def make_tree(istart, iend, pstart, pend):
    if istart == iend and pstart == pend:
        return str(inorder[istart]) + " "
    
    parent = postorder[pend]
    rindex = indexes[parent]
    result = str(parent) + " "
    
    ilstart, ilend = istart, rindex - 1
    plstart, plend = pstart, pstart + rindex - istart - 1
    
    if ilstart <= ilend and plstart <= plend:
        result += make_tree(ilstart, ilend, plstart, plend)
    
    irstart, irend = rindex + 1, iend
    prstart, prend = plend + 1, pend - 1
    
    if irstart <= irend and prstart <= prend:
        result += make_tree(irstart, irend, prstart, prend)
        
    return result

print(make_tree(0, n - 1, 0, n - 1))