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

    #Método para agregar Personas a la lista doble
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

    #Mostrar Personas mediante el ordenamiento por edad
    def mostrarPersona(self):
        actual = self.primero
        while (actual != None):
            print('ID: ', str(actual.id), 'Nombre: ', str(
                actual.nombre), 'Edad: ', str(actual.edad))
            print('--------------------------------------------------')
            actual = actual.siguiente
    
    #Creación del método ordenamiento para ordenar los datos por medio de la edad
    def ordenamientoListaDouble(self):
        # Verifica si la lista está vacía o tiene un solo elemento
        if self.vacia() or self.primero == self.ultimo:
            return
        # En caso contrario, comienza el ordenamiento por inserción
        else:
            # Crea una variable temporal `temp` que apunta al segundo elemento de la lista
            temp = self.primero.siguiente
            
            # Itera a través de cada elemento de la lista después del primer elemento
            while temp:
                # Almacena los valores actuales de `temp` en variables temporales
                val = temp.edad
                val_id = temp.id
                val_nombre = temp.nombre
                
                # Crea una variable temporal `temp_antes` que apunta al elemento anterior de `temp`
                temp_antes = temp.antes
                
                # Mientras `temp_antes` no sea `None` y su valor de edad sea mayor que el valor actual de `temp`,
                # mueve el valor de `temp_antes` a su siguiente elemento y actualiza las variables temporales
                while temp_antes and temp_antes.edad > val:
                    temp_antes.siguiente.edad = temp_antes.edad
                    temp_antes.siguiente.id = temp_antes.id
                    temp_antes.siguiente.nombre = temp_antes.nombre
                    temp = temp_antes
                    temp_antes = temp_antes.antes
                # Asigna los valores temporales al elemento actual `temp`
                temp.edad = val
                temp.id = val_id
                temp.nombre = val_nombre
                
                # Actualiza `temp` para apuntar al siguiente elemento
                temp = temp.siguiente

lista = ListaDoble()

#Creación del main
if __name__ == '__main__':
    print('Datos Agregados manualmente')
    lista.agregarNodoP(1, 'Victor', 25)
    lista.agregarNodoP(2, 'Marcos', 22)
    lista.agregarNodoP(3, 'Aaron', 23)
    lista.agregarNodoP(4, 'Salas', 5)
    lista.agregarNodoP(5, 'Rey', 40)
    lista.agregarNodoP(6, 'July', 11)
    lista.mostrarPersona()

    print("Después de esto el ordenamiento se aplica al obejto de la clase ListaDouble")
    lista.ordenamientoListaDouble()
    lista.mostrarPersona()