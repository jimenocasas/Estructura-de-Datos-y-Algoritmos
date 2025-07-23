
import unittest
from phase1 import SList2

class Test(unittest.TestCase):


    '''class Test (unittest. TestCase): implementar la clase Test que consiste en un
    conjunto de casos de prueba (test cases) que se utilizan para probar la
    implementación de las funciones anteriores. Un caso de prueba (Test case) es la
    unidad individual de prueba y permite comprobar una respuesta específica a un
    conjunto particular de entradas. Unittest proporciona una clase base, TestCase,
    que se puede utilizar para crear nuevos casos de prueba. En la implementación
    de esta clase, puede usar listas de Python para crear sus casos de prueba.'''

    def setUp(self):
        '''Set Up 1º ejercicio: del_largest_seq'''
        self.l1 = SList2()
        for n in [1, 2, 3, 4]:
            self.l1.addLast(n)
        self.l2 = SList2()
        self.l2.addLast(1)
        self.l3 = SList2()
        for n in [3,4,4,4,5,6,7]:
            self.l3.addLast(n)
        self.l4 = SList2()
        for n in [1,2,3,4,4,4,4]:
            self.l4.addLast(n)
        self.l5 = SList2()
        for n in [1,2,2,2,4,5,6,6,6,7]:
            self.l5.addLast(n)
        self.l6 = SList2()
        self.l7 = SList2()
        for n in [1,1,2,2,3,3,4,4,5,5,6,6]:
            self.l7.addLast(n)

        '''Set Up 2º ejercio: fix_loop'''

        self.list1 = SList2()
        self.list2 = SList2()
        self.list3 = SList2()
        self.list4 = SList2()

        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list1.addLast(n)
        self.list1.create_loop(position=5)
        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list2.addLast(n)
        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list3.addLast(n)
        self.list3.create_loop(position=1)

        '''Set Up 3º ejercicio: left_right_shift'''

        self.list5 = SList2()
        self.list6 = SList2()
        self.list7 = SList2()
        self.list8 = SList2()
        self.list9 = SList2()

        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list5.addLast(n)
        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list6.addLast(n)
        for n in [2, 3, 4, 6, 8, 10, 5]:
            self.list7.addLast(n)

        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.list9.addLast(n)


    def test1_ej1(self):
        print("Caso 1: Todos los numeros se repiten solo una vez por lo que "
              "se borra el último")
        l1_1 = SList2()
        for n in [1, 2, 3]:
            l1_1.addLast(n)
        self.l1.del_largest_seq()
        expected1_ej1 = l1_1
        self.assertEqual(str(self.l1), str(expected1_ej1))

    def test2_ej1(self):
        print("Caso 2: Solo hay un número en la lista, se borra y aparace "
              "-La lista está vacía- ")
        l2_2 = SList2()
        self.l2.del_largest_seq()
        self.assertEqual(str(self.l2), str(l2_2))

    def test3_ej1(self):
        print("Caso 3: Elimina la secuencia más larga del medio (la de 4s)")
        l3_3 = SList2()
        for n in [3,5,6,7]:
            l3_3.addLast(n)
        self.l3.del_largest_seq()
        self.assertEqual(str(self.l3), str(l3_3))

    def test4_ej1(self):
        print("Caso 4: borra la secuencia más larga, que es la última")
        l4_4 = SList2()
        for n in [1,2,3]:
            l4_4.addLast(n)
        self.l4.del_largest_seq()
        self.assertEqual(str(self.l4), str(l4_4))

    def test5_ej1(self):
        print("Caso 5: como hay dos secuencias del mismo tamaño (mayor que "
              "uno) borra la última")
        l5_5 = SList2()
        for n in [1,2,2,2,4,5,7]:
            l5_5.addLast(n)
        self.l5.del_largest_seq()
        self.assertEqual(str(self.l5), str(l5_5))

    def test6_ej1(self):
        print("Caso 6: la lista está vacía por lo que devuelve la frase "
              "-Error: la lista está vacía- y no hace nada")
        l6_6 = SList2()
        self.l6.del_largest_seq()
        self.assertEqual(str(self.l6), str(l6_6))

    def test7_ej1(self):
        print("Caso 6: todas las secuencias son mayores que uno y son "
              "iguales por lo que se borrará la última")
        l7_7 = SList2()
        for n in [1,1,2,2,3,3,4,4,5,5]:
            l7_7.addLast(n)
        self.l7.del_largest_seq()
        self.assertEqual(str(self.l7), str(l7_7))

    def test_2_1(self):
        print("Bucle en posicion 5")
        self.assertEqual(self.list1.fix_loop(), True)

    def test_2_2(self):
        print("Sin bucles")
        self.assertEqual(self.list2, False)

    def test_2_3(self):
        print("Bucle en posicion 1")
        self.assertEqual(self.list3.fix_loop(), True)

    def test_2_4(self):
        print("Lista vacía")
        lista_vacia = SList2()
        self.assertEqual(str(self.list4), str(lista_vacia))

    def test_3_1(self):
        print("Caso 1: left = True y n = 2")
        list3_1 = SList2()
        for n in [3, 4, 5, 6, 7, 1, 2]:
            list3_1.addLast(n)
        self.list5.left_right_shift(True, 2)
        expected_ej1 = list3_1
        self.assertEqual(str(self.list5), str(expected_ej1))

    def test_3_2(self):
        print("Caso 2: left = False y n = 2")
        list3_2 = SList2()
        for n in [6, 7, 1, 2, 3, 4, 5]:
            list3_2.addLast(n)
        self.list6.left_right_shift(False, 2)
        expected_ej2 = list3_2
        self.assertEqual(str(self.list6), str(expected_ej2))

    def test_3_3(self):
        print("Caso 3: la lista está desordenada, left = True y n = 1")
        list3_1 = SList2()
        for n in [3, 4, 6, 8, 10, 5, 2]:
            list3_1.addLast(n)
        self.list7.left_right_shift(True, 1)
        expected_ej3 = list3_1
        self.assertEqual(str(self.list7), str(expected_ej3))

    def test_3_4(self):
        print("Caso 4: lista vacía, da un error")
        list4_1 = SList2()
        self.list8.left_right_shift(True, 10)
        expected_ej4 = list4_1
        self.assertEqual(str(self.list8), str(expected_ej4))

    def test_3_5(self):
        print("Caso 5: la n es igual al size de la lista")
        list3_5 = SList2()
        for n in [1, 2, 3, 4, 5, 6, 7]:
            list3_5.addLast(n)
        self.list9.left_right_shift(True or False, 7)
        expected_ej5 = list3_5
        self.assertEqual(str(self.list9), str(expected_ej5))


if __name__ == "__main__":
    unittest.main()