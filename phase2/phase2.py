"""
Case #2. Exercise  3
@author: EDA Team
"""

# Classes provided by EDA Team
from dlist import DList
from bintree import BinaryNode
from bst import BinarySearchTree

class BST2(BinarySearchTree):


    def find_dist_k(self, n, k):
        lista = []
        node = self.root

        while node is not None:
            if node.elem == n:
                self._find_dist_k(node, k, 0, lista, [])
                return lista

            elif node.elem > n:
                node = node.left

            else:
                node = node.right

        return lista

    def _find_dist_k(self, node, k, dist, lista, visited):
        if not node:
            return

        if node not in visited:
            visited.append(node)

            if dist == k:
                lista.append(node.elem)

            else:
                self._find_dist_k(node.left, k, dist + 1, lista,
                                        visited)
                self._find_dist_k(node.right, k, dist + 1, lista,
                                        visited)
                parent = self.find_parent(node)

                if (parent and (parent.elem, parent.left, parent.right) != (
                        node.elem, node.left, node.right) and dist < k and
                        parent not in visited):
                    self._find_dist_k(parent, k, dist + 1, lista,
                                            visited)


    def find_parent(self, node):
        if node == self.root:
            return None
        else:
            parent = self.root
            while parent is not None:
                if parent.left == node or parent.right == node:
                    return parent
                elif parent.elem > node.elem:
                    parent = parent.left
                else:
                    parent = parent.right
            return None


def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree,
                opc: str):
    if opc == "merge":
        if input_tree1 is None:
            print("El arbol 1 está vacio")
            return input_tree2
        if input_tree2 is None:
            print("El arbol 2 está vacio")
            return input_tree1
        new_tree = BinarySearchTree()

        _insert1(input_tree1.root, new_tree)
        _insert1(input_tree2.root, new_tree)

        return new_tree

    elif opc == "intersection":
        if input_tree1 is None:
            print("El arbol 1 no existe")
            return None
        if input_tree2 is None:
            print("El arbol 2 no existe")
            return None

        new_tree = BinarySearchTree()
        node1 = input_tree1.root
        node2 = input_tree2.root

        _insert2(node1, node2, new_tree)

        return new_tree

    elif opc == "difference":
        if not input_tree1:
            print("El arbol 1 no existe")
            return None
        if not input_tree2:
            print("El arbol 2 no existe")
            return input_tree1

        new_tree = BinarySearchTree()

        node2 = input_tree1.root

        _insert3(input_tree2, node2, new_tree)

        return new_tree


def _insert1(node, tree):
    if node is None:
        return None

    tree.insert(node.elem) #usamos la función insert que viene en el programa

    _insert1(node.left, tree)
    _insert1(node.right, tree)


def _insert2(node1, node2, tree):

    if node1 is None or node2 is None:

        return

    if node1.elem == node2.elem:
        tree.insert(node1.elem)  #usamos la función insert que viene en el programa

    else:
        _insert2(node1, node2.left, tree)
        _insert2(node1, node2.right, tree)

    _insert2(node1.left, node2, tree)
    _insert2(node1.right, node2, tree)


def _insert3(tree: BinarySearchTree, node2: BinaryNode,
             new_tree: BinarySearchTree):

    if node2 is None:
        return new_tree

    node = tree.search(node2.elem)  #usamos la función search que viene en el
    # programa

    if not node:
        new_tree.insert(node2.elem)  #usamos la función insert que viene en el programa

    if node2.left:
        new_tree = _insert3(tree, node2.left, new_tree)

    if node2.right:
        new_tree = _insert3(tree, node2.right, new_tree)

    return new_tree


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]

    input_list_01 = []
    input_list_02 = [1,2,3,4]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
