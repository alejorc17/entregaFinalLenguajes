class node:
    def __init__(self, data, next=None):
        self.data = data  # Dato asignado al nodo
        self._next = next  # Puntero o apuntador hacia el siguiente elmento

    def __str__(self):
        return self.data

