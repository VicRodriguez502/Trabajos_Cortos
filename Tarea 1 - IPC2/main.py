#Tarea #1 Creada por Victor Rodriguez Carnet 201900018

#Creación de la clase Nodo
class nodoPersona():
    #Constructor del nodo para la lista Doble
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.siguiente = None
        self.antes = None

#Clase de lista Doble
class ListaDoble:
    #Constructor de la lista Doble
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    #Creamos una función para verificar que la lista este vacia
    def vacia(self):
        return self.primero == self.ultimo == None

    #Método para agregar celdas a la lista celdas
    def agregarNodoP(self, id, nombre, edad):
        nuevaPersona = nodoPersona(id, nombre, edad)
        if self.vacia():
            self.primero = self.ultimo = nuevaPersona
        elif self.primero == self.ultimo:
            self.ultimo = nuevaPersona
            self.primero.siguiente = self.ultimo
            self.ultimo.antes = self.primero
        else:
            self.ultimo.siguiente = nuevaPersona
            nuevaPersona.antes = self.ultimo
            self.ultimo = nuevaPersona
        self.tamanio = self.tamanio + 1

    def mostrarPersona(self):
        actual = self.primero
        while(actual != None):
            print('ID: ', str(actual.id), 'Nombre: ', str(actual.nombre), 'Edad: ', str(actual.edad))
            print('--------------------------------------------------')
            actual = actual.siguiente

lista = ListaDoble()

#Creación del main
if __name__ == '__main__':
    print('Hola mundo')
    lista.agregarNodoP(1,'Victor', 25)
    lista.agregarNodoP(2,'Marcos',22)
    lista.agregarNodoP(3,'Aaron',23)
    lista.mostrarPersona()