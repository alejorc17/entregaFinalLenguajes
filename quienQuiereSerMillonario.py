import random
from listas import SinglyLinkedList
from datos import nombres, comodines

class aspirante:
    def __init__(self, nombre, id, tiempoPreguntaClasificatoria):
        self.nombre=nombre
        self.id=id
        self.tiempoPreguntaClasificatoria = tiempoPreguntaClasificatoria

    def imprimirAspirante(self):
        return f'El participante {self.nombre}, de id {self.id}, tiene: tiempo de pregunta clasifictoria: {self.tiempoPreguntaClasificatoria}'

class Usuario(aspirante):
    def __init__(self, nombre, id, tiempoPreguntaClasificatoria):
        super().__init__(nombre,id,tiempoPreguntaClasificatoria)
        self.preguntasRespondidas = 0
        self.seguro = 0
        self.premio = 0
        self.ayudasUsadas = 0
        self.activoPrograma = True

    def __str__(self):
        return self.imprimirAspirante()+f' respondío {self.preguntasRespondidas} preguntas, obtuvo de premio {self.premio} de pesos y usó {self.ayudasUsadas} comodines'

class programa:
    def __init__(self):
        self.listaParticipantes = SinglyLinkedList()
        self.premio = 0

    def crearParticipantes(self):
        repeticiones = random.randint(2, 5)
        for i in range(repeticiones):
            participanteX = Usuario(nombres[random.randint(0, len(nombres)-1)], random.randint(0, 1000000), random.randint(10, 200))

            self.listaParticipantes.insertFirst(participanteX)

    def sumatoriaPremio(self):
        aux = self.listaParticipantes.first
        while aux:
            self.premio += aux.data.premio  # Accede al atributo premio a través de aux.data
            aux = aux._next

class diaDePrograma(programa):
    def __init__(self, dia):
        super().__init__()
        self.listaParticipantes = SinglyLinkedList()
        self.dia = dia
        self.premio = 0
    def desarrollo(self):
        self.crearParticipantes()
        aux = self.listaParticipantes.first
        while aux:
            i = 1
            while i < 16:
                print(f'Día: {self.dia}, Participante: {aux.data.nombre}, Pregunta: {i}')

                if i < 6:
                    probabilidadDeAcertar = random.randint(0, 100)
                    if probabilidadDeAcertar > 20:
                        if aux.data.ayudasUsadas < 3 and probabilidadDeAcertar > 90:
                            aux.data.ayudasUsadas += 1
                        aux.data.preguntasRespondidas = i
                        if i < 4:
                            aux.data.premio += 100000
                        elif i < 5:
                            aux.data.premio += 200000
                        elif i < 6:
                            aux.data.premio += 500000
                            aux.data.seguro = 500000
                        i += 1
                    else:
                        aux.data.activoPrograma = False
                        aux.data.premio = aux.data.seguro
                        break
                elif i < 10:
                    probabilidadDeAcertar = random.randint(0, 100)
                    if probabilidadDeAcertar > 40:
                        if aux.data.ayudasUsadas < 3 and probabilidadDeAcertar > 70:
                            aux.data.ayudasUsadas += 1
                        aux.data.preguntasRespondidas = i
                        if i < 8:
                            aux.data.premio += 1000000
                        elif i < 10:
                            aux.data.premio += 2000000
                        elif i < 11:
                            aux.data.premio += 3000000
                            aux.data.seguro = 10000000
                        i += 1
                    else:
                        aux.data.activoPrograma = False
                        aux.data.premio = aux.data.seguro
                        break
                else:
                    probabilidadDeAcertar = random.randint(0, 100)
                    if probabilidadDeAcertar > 70:
                        if aux.data.ayudasUsadas < 3 and probabilidadDeAcertar > 75:
                            aux.data.ayudasUsadas += 1
                        aux.data.preguntasRespondidas = i
                        if i < 12:
                            aux.data.premio += 2000000
                        elif i < 13:
                            aux.data.premio += 8000000
                        elif i < 14:
                            aux.data.premio += 30000000
                        elif i < 15:
                            aux.data.premio += 50000000
                        else:
                            aux.data.premio += 200000000
                            aux.data.seguro = aux.data.premio
                        i += 1
                    else:
                        aux.data.activoPrograma = False
                        aux.data.premio = aux.data.seguro
                        break

            aux = aux._next

        self.sumatoriaPremio()
        print(f'En el día {self.dia}, el total de premio entregado fue: {self.premio}')
        aux = self.listaParticipantes.first
        while aux:
            print(aux.data.__str__())
            aux = aux._next



