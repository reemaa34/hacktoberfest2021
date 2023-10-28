def search(val, root, pos):
 
    # if root is None then return
    if (root == None):
        return None
    else :
        # if node is found
        if (searchnode(val, root, pos)):
            return root
 
        # if not then search in child nodes
        else:
            return search(val, root.child[pos], pos)
     
 
 
# Searches the node
def searchnode(val, n, pos):
    # if val is less than node.value[1]
    if (val < n.value[1]):
        pos = 0
        return 0
     
 
    # if the val is greater
    else :
        pos = n.count
 
        # check in the child array
        # for correct position
        while ((val < n.value[pos]) and pos > 1):
            pos-=1
        if (val == n.value[pos]):
            return 1
        else:
            return 0
    
