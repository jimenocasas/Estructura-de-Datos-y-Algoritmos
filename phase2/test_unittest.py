# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
from phase2 import BST2
from phase2 import create_tree
import unittest




class Test(unittest.TestCase):
    def setUp(self):

        """SetUp del 1º ejercicio: """
        input_list1 = []
        input_list2 = [14, 11, 18]
        input_list3 = [30,50,60,85,90,100]
        input_list4 = [8,12,14]
        input_list5 = [13,48,45,39,9,2,25,68,90]
        input_list6 = [13, 48, 45, 39, 9, 2, 25, 68, 90]
        input_list7 = [50,68,2,45,67,89,1,16]
        self.bst1 = BST2()
        self.bst2 = BST2()
        self.bst3 = BST2()
        self.bst4 = BST2()
        self.bst5 = BST2()
        self.bst6 = BST2()
        self.bst7 = BST2()
        for x in input_list1:
            self.bst1.insert(x)
        for x in input_list2:
            self.bst2.insert(x)
        for x in input_list3:
            self.bst3.insert(x)
        for x in input_list4:
            self.bst4.insert(x)
        for x in input_list5:
            self.bst5.insert(x)
        for x in input_list6:
            self.bst6.insert(x)
        for x in input_list7:
            self.bst7.insert(x)

        """Set Up 2 Unittest"""

        self.a1 = BinarySearchTree()
        self.a1_2 = BinarySearchTree()
        for n in [1,2,3,4,5]:
            self.a1.insert(n)
        for n in [6,7,8,9]:
            self.a1_2.insert(n)

        self.a2_1 = BinarySearchTree()
        self.a2_2 = BinarySearchTree()
        for n in [1,2,3,4]:
            self.a2_1.insert(n)
        for n in [3,4,5,6,7,8]:
            self.a2_2.insert(n)

        self.a3_1= BinarySearchTree()
        self.a3_2 = BinarySearchTree()
        for n in [1,2,3,4]:
            self.a3_1.insert(n)

        self.a4_1 = BinarySearchTree()
        self.a4_2 = BinarySearchTree()

        self.a5_1 = BinarySearchTree()
        self.a5_2 = BinarySearchTree()
        for n in [1,2,3,4,5,6]:
            self.a5_2.insert(n)
            self.a5_1.insert(n)

        self.a6_1 = BinarySearchTree()
        self.a6_2 = BinarySearchTree()
        for n in [4,5,6,7]:
            self.a6_2.insert(n)

    """Test ejercicio 1"""

    def test1_test01(self):
        print("Caso 1: lista vacía")
        expected = []
        actual = self.bst1.find_dist_k(17, 3)
        self.assertEqual((actual), (expected))

    def test1_test02(self):
        print("Caso 2: nodos a distancia 1 (k=1)")
        expected = [11, 18]
        actual = self.bst2.find_dist_k(14, 1)
        self.assertEqual((actual), (expected))

    def test1_test03(self):
        print("Caso 3: nodos a distancia 0 (k=0, devulve el mismo nodo)")
        expected = [60]
        actual = self.bst3.find_dist_k(60, 0)
        self.assertEqual((actual), (expected))

    def test1_test04(self):
        print("Caso 4: k>(profundidad de n)")
        expected = []
        actual = self.bst4.find_dist_k(12, 5)
        self.assertEqual((actual), (expected))

    def test1_test05(self):
        print("Caso 5: k<0")
        expected = []
        actual = self.bst5.find_dist_k(25, -2)
        self.assertEqual((actual), (expected))

    def test1_test06(self):
        print("Caso 6: nodo n es inexistente en el árbol")
        expected = []
        actual = self.bst6.find_dist_k(14, 1)
        self.assertEqual((actual), (expected))

    def test1_test07(self):
        print("Caso 7: regular")
        expected = [1, 45, 67, 89]
        actual = self.bst7.find_dist_k(50, 2)
        self.assertEqual((actual), (expected))

    """Test ejercicio 2"""

    def test2_test_0_1(self):
        print("Caso 1 (merge): Ningún numero se repite, por lo que devuelve "
              "la "
              "suma "
              "de los dos árboles")
        expected_test_0_1 = BinarySearchTree()
        for n in [1,2,3,4,5,6,7,8,9]:
            expected_test_0_1.insert(n)
        prueba_test01 = create_tree(self.a1, self.a1_2, "merge")
        self.assertEqual(prueba_test01, expected_test_0_1)

    def test2_test_0_2(self):
        print("Caso 2 (merge): Se repite algún número, por lo que devuelve "
              "la suma "
              "de los dos árboles, pero los que se repiten no se añaden dos "
              "veces")
        expected_test_0_2 = BinarySearchTree()
        for n in [1, 2, 3, 4, 5, 6, 7, 8]:
            expected_test_0_2.insert(n)
        prueba_test02 = create_tree(self.a2_1,self.a2_2, "merge")
        self.assertEqual(prueba_test02, expected_test_0_2)

    def test2_test_0_3(self):
        print("Caso 3 (merge): El segundo árbol está vacio por lo que "
              "devolvera el "
              "primer árbol")
        expected_test_0_3 = BinarySearchTree()
        for n in [1, 2, 3, 4]:
            expected_test_0_3.insert(n)
        prueba_test03 = create_tree(self.a3_1,self.a3_2, "merge")
        self.assertEqual(prueba_test03, expected_test_0_3)

    def test2_test_0_4(self):
        print("Caso 4 (merge): Los dos árboles están vacíos por lo que "
              "devolverá None")
        expected_test_0_4 = BinarySearchTree()
        prueba_test04 = create_tree(self.a4_1,self.a4_2, "merge")
        self.assertEqual(prueba_test04, expected_test_0_4)

    def test2_test_0_5(self):
        print("Caso 5 (merge): Los dos árboles son iguales por lo que "
              "delvuelve el "
              "mismo árbol")
        expected_test_0_5 = BinarySearchTree()
        for n in [1, 2, 3, 4, 5, 6]:
            expected_test_0_5.insert(n)
        prueba_test05 = create_tree(self.a5_1,self.a5_2, "merge")
        self.assertEqual(prueba_test05, expected_test_0_5)

    def test2_test_1_1(self):
        print("Caso 1 (intersection): Ninguno de los elementos del arbol1 "
              "coincide con los del árbol dos por lo que devolvera None")
        expected_test_1_1 = BinarySearchTree()
        prueba_test11 = create_tree(self.a1, self.a1_2, "intersection")
        self.assertEqual(prueba_test11, expected_test_1_1)

    def test2_test_1_2(self):
        print("Caso 2 (intersection): Coinciden algunos por lo que el árbol "
              "de salida será los elementos que coincidan")
        expected_test_1_2 = BinarySearchTree()
        for n in [4,3]:
            expected_test_1_2.insert(n)
        prueba_test12 = create_tree(self.a2_1, self.a2_2, "intersection")
        self.assertEqual(prueba_test12, expected_test_1_2)

    def test2_test_1_3(self):
        print("Caso 3 (intersection): Coinciden todos por lo que el árbol de "
              "salida será el mismo árbol de netrada")
        expected_test_1_3 = BinarySearchTree()
        for n in [1,2,3,4,5,6]:
            expected_test_1_3.insert(n)
        prueba_test13 = create_tree(self.a5_1, self.a5_2, "intersection")
        self.assertEqual(prueba_test13, expected_test_1_3)

    def test2_test_1_4(self):
        print("Caso 4 (intersection): 1 árbol está vació por lo que "
              "devolvera None")
        expected_test_1_4 = BinarySearchTree()
        prueba_test14 = create_tree(self.a3_1, self.a3_2, "intersection")
        self.assertEqual(prueba_test14, expected_test_1_4)

    def test2_test_1_5(self):
        print("Caso 5 (intersection): Los 2 árboles están vacíos por lo que "
              "devuelve None")
        expected_test_1_5 = BinarySearchTree()
        prueba_test15 = create_tree(self.a4_1, self.a4_2, "intersection")
        self.assertEqual(prueba_test15, expected_test_1_5)

    def test2_test_2_1(self):
        print("Caso 1 (difference): Ninguno de los elementos de los árboles "
              "coinciden por lo que devuleve el arbol1")
        expected_test_2_1 = BinarySearchTree()
        for n in [1,2,3,4,5]:
            expected_test_2_1.insert(n)
        prueba_test21 = create_tree(self.a1, self.a1_2, "difference")
        self.assertEqual(prueba_test21, expected_test_2_1)

    def test2_test_2_2(self):
        print("Caso 2 (difference): Coinciden algunos por lo que devolverá "
              "el árbol1 pero sin los elementos que coincidan")
        expected_test_2_2 = BinarySearchTree()
        for n in [1,2]:
            expected_test_2_2.insert(n)
        prueba_test22 = create_tree(self.a2_1, self.a2_2, "difference")
        self.assertEqual(prueba_test22, expected_test_2_2)

    def test2_test_2_3(self):
        print("Caso 3 (difference): Coinciden todos por lo que el árbol de "
              "salida estará vacio")
        expected_test_2_3 = BinarySearchTree()
        prueba_test23 = create_tree(self.a5_1, self.a5_2, "difference")
        self.assertEqual(prueba_test23, expected_test_2_3)


    def test2_test_2_4(self):
        print("Caso 4 (difference): El segundo árbol está vacio por lo que "
              "devuelve el primero tal cual")
        expected_test_2_4 = BinarySearchTree()
        for n in [1,2,3,4]:
            expected_test_2_4.insert(n)
        prueba_test24 = create_tree(self.a3_1, self.a3_2, "difference")
        self.assertEqual(prueba_test24, expected_test_2_4)

    def test2_test_2_5(self):
        print("Caso 5 (difference): El primer árbol está vacio por lo que "
              "devuelve None")
        expected_test_2_5 = BinarySearchTree()
        prueba_test25 = create_tree(self.a6_1, self.a6_2, "difference")
        self.assertEqual(prueba_test25, expected_test_2_5)

    def test2_test_2_6(self):
        print("Caso 6 (difference): Los dos árboles están vacios por lo que "
              "devuelve None")
        expected_test_2_3 = BinarySearchTree()
        prueba_test24 = create_tree(self.a4_1, self.a4_2, "difference")
        self.assertEqual(prueba_test24, expected_test_2_3)


# Some usage examples
if __name__ == '__main__':
    unittest.main()
