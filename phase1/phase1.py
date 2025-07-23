from slistH import SList
from slistH import SNode

import sys
import random

class SList2(SList):

    '''del_largest_seq(self), el objetivo del método es eliminar la secuencia más larga
    de números idénticos y consecutivos en la lista. Si hay varias secuencias con la
    misma longitud (la mayor), se eliminará únicamente la última secuencia en la lista.
    El método no devuelve nada, solo modifica la lista invocante'''

    def del_largest_seq(self):

        if self.isEmpty():
            print("Error: la lista está vacía")

        else:
            posicion_del_node = 0
            prev = self._head
            node_it = prev.next
            secuencia_larga = -1
            secuencia_actual = 1
            pos_secuencialarga = self._size

            while node_it is not None:

                while prev.elem == node_it.elem:
                    secuencia_actual += 1
                    prev = prev.next
                    node_it = node_it.next
                    posicion_del_node += 1
                    if secuencia_actual >= secuencia_larga:
                        secuencia_larga = secuencia_actual
                        pos_secuencialarga = (posicion_del_node
                                                          - secuencia_larga)
                    if node_it is None:
                        break
                if node_it is None:
                    break
                secuencia_actual = 1
                prev = prev.next
                node_it = node_it.next
                posicion_del_node += 1

            node_it_2 = self._head
            node_it_3 = self._head

            if pos_secuencialarga == self._size:
                if pos_secuencialarga == 1:
                    self.removeLast()
                    print("La lista está vacía")
                else:
                    for n in range(self._size - 2):
                        node_it_2 = node_it_2.next
                    node_it_2.next = None
            elif pos_secuencialarga == -1:
                for n in range (self._size):
                    self.removeLast()
                print("La lista está vacía")
            else:
                for n in range(pos_secuencialarga):
                    node_it_2 = node_it_2.next

                for n in range(pos_secuencialarga + secuencia_larga + 1):
                    node_it_3 = node_it_3.next
                node_it_2.next = node_it_3

    '''fix _loop(self). El objetivo de este método es detectar si la lista invocante contiene
    un bucle y, en ese caso, romperlo. Una lista contiene un bucle si la referencia next
    de su último nodo apunta a otro nodo de la lista en vez de a None. La siguiente
    figura muestra dos ejemplos de SList que contienen un bucle (en el primer caso la
    lista es completamente circular; en el segundo sólo una parte de la misma tiene
    un bucle – nodos B, C y D -). En ambos casos el nodo A es la cabeza de la lista.
    Si se detecta el bucle, el método debe romperlo y devolver True, o devolver False
    y no modificar la lista en caso contrario. Nota que una SList puede tener un único
    bucle o ninguno, ya que cada nodo sólo tiene una única referencia a su nodo
    siguiente.'''

    def fix_loop(self):
        if self.isEmpty():
            print("Error: la lista está vacía")
            return False
        else:
            node_it = self._head
            if node_it.next is None:
                return False
            else:
                contador = 2
                node_it_2 = node_it.next
                while node_it_2.next is not None:
                    node_it = self._head
                    for n in range(contador):
                        if node_it_2.next == node_it:
                            node_it_2.next = None
                            return True
                        else:
                            node_it = node_it.next

                    node_it_2 = node_it_2.next
                    contador += 1
                return False

    '''left_right_shift(self, left, n), el método recibe un valor booleano, left, un entero
    positivo (mayor de cero), n. Si left es True, el método debe mover al final de la lista
    los n primeros nodos de la lista (ver ejemplos). Por el contrario, si left es False, el
    método deberá mover los n últimos nodos de la lista al comienzo de la lista, tal y
    como se explica en los ejemplos. Si n es igual o mayor al tamaño de la lista, el
    método no hace nada. El método no devuelve nada; simplemente modifica la lista.'''

    def left_right_shift(self, left, n):
        if self.isEmpty():
            print('Error: lista vacia!')
        elif n > len(self):
            print(
                'Error, la n no puede ser mayor o igual a la longitd de la lista')
        elif n == len(self):
            pass
        else:
            node_it = self._head
            last_node = self._head
            for i in range(self._size - 1):
                last_node = last_node.next
            prev = self._head
            if left:
                for j in range(n - 1):
                    prev = prev.next
            else:
                for j in range(self._size - n - 1):
                    prev = prev.next
            self._head = prev.next
            last_node.next = node_it
            prev.next = None


if __name__=='__main__':

    l=SList2()
    print("list:",str(l))
    print("len:",len(l))

    for i in range(7):
        l.addLast(i+1)

    print(l)
    print()

    l=SList2()
    print("list:",str(l))
    print("len:",len(l))

    for i in range(7):
        l.addLast(i+1)

    print(l)
    print()

    # No loop yet, no changes applied
    l.fix_loop()
    print("No loop yet, no changes applied")
    print(l)
    print()

    # We force a loop
    l.create_loop(position=6)
    l.fix_loop()
    print("Loop fixed, changes applied")
    print(l)
    print()
    print()

    
    l = SList2()
    for i in [1,2,3,4,5]:        
        l.addLast(i)
    print(l.del_largest_seq())


    l=SList2()
    for i in range(7):
         l.addLast(i+1)

    print(l)
    l.left_right_shift(False, 2)
    print(l)
