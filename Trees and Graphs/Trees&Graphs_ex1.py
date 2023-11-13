
class Node:
  def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None





def lowestCommonAncestor_Recursive(root, p, q) :
  
  if root is None :  return None
  print(root.val)

  #CASE 1 : if both p and q is higher than root then the new root is the right subtree because this is a binary tree
  if p > root.val and q > root.val :
    return lowestCommonAncestor_Recursive(root.right , p , q)
  

  #CASE 2 : if both p and q is lower than root then the new root is the left subtree because this is a binary tree

  elif p < root.val and q < root.val : 
    return lowestCommonAncestor_Recursive(root.left , p , q)
  

  print("test")
  return root

 
     
  

def lowestCommonAncestor_iterative(root, p, q) :
  
    while(root) :
     
     if p < root.val and q < root.val :
       root = root.left
     elif p > root.val and q > root.val :
       root = root.right
    
     else:
       break
     
    return root



if __name__ == '__main__':
  root = Node(20)
  root.left = Node(8)
  root.right = Node(22)
  root.left.left = Node(4)
  root.left.right = Node(12)
  root.left.right.left = Node(10)
  root.left.right.right = Node(14)
 
  n1 = 10
  n2 = 14
  t = lowestCommonAncestor_iterative(root, n1, n2)
  #t = lowestCommonAncestor_Recursive(root, n1, n2)
  print("LCA of %d and %d is %d" % (n1, n2, t.val))
 
  n1 = 14
  n2 = 8
  t = lowestCommonAncestor_iterative(root, n1, n2)
  #t = lowestCommonAncestor_Recursive(root, n1, n2)
  print("LCA of %d and %d is %d" % (n1, n2, t.val))
 
  n1 = 10
  n2 = 22
  t = lowestCommonAncestor_iterative(root, n1, n2)
  #t = lowestCommonAncestor_Recursive(root, n1, n2)
  print("LCA of %d and %d is %d" % (n1, n2, t.val))
