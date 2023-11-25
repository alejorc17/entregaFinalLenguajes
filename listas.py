from nodes import node


class SinglyLinkedList:
    def __init__(self):
        self.first = None  # Puntero hacia el primer elemento de la lista
        self.last = None  # Puntero hacai el ultimo elemento de la lista
        self.size = 0  # cantidad de eleentos de la lista

    # Metodo para verificar si la lista esta vacia
    def Empty(self):
        return self.first == None  # retorna si es verdadero o falso

    # Operaion para insertar elementos al inicio de la lista

    def insertFirst(self, data):
        # Asignar en memoria y rellenar el camo de dato
        newNode = node(data)
        # verificar si la lista esta vacia
        if self.Empty():
            # Operacion para insertar un elemento en una lista vacia
            self.first = newNode
            self.last = newNode
            # Actualizar el tamaño
            # self.size += 1

        else:
            # Operacion para insertar un elemento al inicio de la lista
            # El nuevo nodo debe puntar al primer elemento de la lista
            newNode._next = self.first  # Se mueve el puntero del nodo
            # Se mueve el puntero al inicio
            self.first = newNode  # Se reconoce el nodo como el nuevo primer nodo
            # Actualizar el tamaño de la lista
            # self.size+=1  Como la operacion se hace en el if y en else, se puede dejar esta operacion para el final
        self.size += 1

    # Metodo para mostrar los elementos de la lista
    def Show(self):
        aux = self.first
        while aux:
            print(aux.data)  # Accede directamente al objeto Usuario en el nodo
            aux = aux._next
        print("")

