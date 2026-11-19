#Crea una clase bateria que permita manejar los atributos AIDE y votaje y usemos la funcion copy.deepcopy() en donde modifiquemos la copia sin afectar el original, crea nodo bateria y lista bateria con un unico puntero cabeza he implementar los metodos incertar_al_inicio(bateria) y el metodo purgar_agotadoas() el cual debe recorrer la lista y recolectar los punteros y elimine las baterias con menos de 3 voltios

class Bateria:

    def __init__(self, aide: str, voltaje: float) -> None:
        self.aide: str = aide 
        self.voltaje: float = voltaje

    def __repr__(self) -> str:
    
        return f"Bateria(AIDE={self.aide!r}, voltaje={self.voltaje}V)"

class NodoBateria: 

    def __init__(self, bateria: Bateria) -> None:
        self.bateria: Bateria = bateria
        self.siguiente: "NodoBateria | None" = None

class ListaBateria:

    def __init__(self) -> None:
        self.cabeza: NodoBateria | None = None

    def insertar_al_inicio(self, bateria: Bateria) -> None:
        
        nuevo = NodoBateria(bateria)
        nuevo.siguiente = self.cabeza   # El nuevo va al viejo primero
        self.cabeza = nuevo             # La cabeza se mueve al nuevo nodo

    def purgar_agotadas(self, umbral: float = 3.0) -> int:
       
        eliminadas: int = 0
        anterior: NodoBateria | None = None
        actual: NodoBateria | None = self.cabeza

        while actual is not None:
            if actual.bateria.voltaje < umbral:
                #  Recolectar punteros y desenlazamos el nodo
                if anterior is None:
                # Caso 1: el nodo agotado es la cabeza
                    self.cabeza = actual.siguiente
                else:
                # Caso 2: saltamos el nodo: anterior -> actual.siguiente
                    anterior.siguiente = actual.siguiente

                eliminadas += 1
                actual = actual.siguiente      # Seguimos sin mover el anterior
            else:
            # Batería sana: avanzamos ambos punteros
                anterior = actual
                actual = actual.siguiente

        return eliminadas

    def mostrar(self) -> None: #Imprime el contenido

        print("-Lista de Baterías-:")
        actual: NodoBateria | None = self.cabeza
        while actual is not None:
            dir_sig = hex(id(actual.siguiente)) if actual.siguiente else "None"
            print(
                f"AIDE: {actual.bateria.aide:<10} | "
                f"Voltaje: {actual.bateria.voltaje:>4}V | "
                f"Nodo en: {hex(id(actual))} | "
                f"Siguiente: {dir_sig}"
            )
            actual = actual.siguiente
        print("-------------------------\n")


if __name__ == "__main__": # 1. Creamos varias baterías con cualquier valore
    
    b1 = Bateria("AIDE-01", 3.7)
    b2 = Bateria("AIDE-02", 2.5)   # agotada
    b3 = Bateria("AIDE-03", 4.2)
    b4 = Bateria("AIDE-04", 1.8)   # agotada
    b5 = Bateria("AIDE-05", 3.0)  

    # 2. Insertamos al inicio (el orden se invierte)
    lista = ListaBateria()
    for bateria in (b1, b2, b3, b4, b5)
        lista.insertar_al_inicio(bateria)

    print("Lista origial de BAteiras")
    lista.mostrar()

    # 3. Demostración de copy.deepcopy(): copia 
    print(" Demostracion copy.deepcopy()")
    lista_respaldo = copy.deepcopy(Lista)
    lista_respaldo.cabeza.bateria.voltaje = 99.9   # Modificamos la copia
    print(f"Original  (cabeza): {lista.cabeza.bateria} | ID nodo: {hex(id(lista.cabeza))}")
    print(f"Respaldo  (cabeza): {lista_respaldo.cabeza.bateria} | ID nodo: {hex(id(lista_respaldo.cabeza))}")
    print("=> IDs distintos y voltaje intacto en el original.\n")``

    # 4. Purgamos las baterías con menos de 3 V
    eliminadas = lista.purgar_agotadas(umbral=3.0)
    print(f"Baterías eliminadas (voltaje < 3.0 V): {eliminadas}\n")

    print("Lista nueva luego de Purgar")
    lista.mostrar()