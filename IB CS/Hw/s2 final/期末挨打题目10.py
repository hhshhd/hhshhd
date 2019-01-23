stack = ['alpha','mu','gamma','delta','epsilon','zeta','lambda','theta']

name =input('name:')
temp = False
position = 0
while not len(stack)==0:
    item = stack.pop()
    if item ==name:
        print('yes,position:',position)
        temp = True
    position += 1
if temp == False:
    print('Not found')
stack = ['alpha','mu','gamma','delta','epsilon','zeta','lambda','theta']
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def left(root):
    return root.left

def right(root):
    return root.right

first_root = Tree(stack.pop())
first_leaf = Tree(stack.pop())

def tree_change(root,leaf):
    while True:
        if leaf.cargo<root.cargo:
            if root.left == None:
                root.left = leaf
                break
            else:
                print(leaf,'left')
                return(root.left,leaf)
        else:
            if root.right == None:
                root.right = leaf
                break
            else:
                print(leaf,'right')
                return(root.right,leaf)

    return tree_change(root,Tree(stack.pop()))

tree_change(first_root,first_leaf)
