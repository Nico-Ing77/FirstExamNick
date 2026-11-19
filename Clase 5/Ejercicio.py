#Se requiere un sistema de monitoreo para una caldera industrial.
#El sofware debe registrar lectura de presion dinamicamente mediante la clase auto-referenciada Nodo evento y la clase gestora Historial eventos
#Debe permitir registar eventos al inicio, contar eventos criticos, mostrar la cadena y reliazar un evento de purgas normales reconectando punteros para liberar memoria

class Nodoevento:
     def __init__(self, id_sensor: str, lectura: float, estado: str, time: str) -> None:
            self.id_sensor: str = id_sensor
            self.lectura: float = lectura
            self.estado: str = estado
            self.time: str = time
            self.siguiente: "Nodoevento | None" = None

     #Registro       

class ListaEvento:
    def __init__(self) -> None:
         self.uno: "Nodoevento | None" = None 

    def registro_evento (self,id_sensor: str, lectura:float, time: str) -> None:

        if lectura >=self.UMBRAL_CRITICO:
         estado = "Critico"
        else:
            estado="NOrmal"
        self.insertar_inicio(id_sensor, lectura, estado, time)

    
    def insertar_inicio(self, id_sensor: str, lectura: float, estado: str, time: str) -> None:
        """Inserta un nodo al inicio de la cadena en tiempo O(1)."""
        nuevo_nodo = Nodoevento(id_sensor, lectura, estado, time)
        nuevo_nodo.siguiente = self.uno
        self.uno = nuevo_nodo

    def insertar_final(self, id_sensor: str, lectura: float, estado: str, time: str) -> None:
        """Inserta un nodo al final de la cadena recorriendo la memoria O(N)."""
        nuevo_nodo = Nodoevento(id_sensor, lectura, estado, time)
        if self.uno is None:
            self.uno = nuevo_nodo
            return
        
            actual = self.uno
            while actual.sigiente is not None:
                 actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        

         #Contar

def contar_criticos(self) -> int:
        contador = 0
        actual = self.uno
        while actual is not None:
            if actual.estado.upper() == "CRITICO":
                contador += 1
            actual = actual.siguiente
        return contador


        #Mostrar la cadena

        def mostrar_historial(self) -> None:
        #""Recorre e imprime la secuencia de eventos."""
        actual = self.uno
        if actual is None:
            print("El historial está vacío.")
            return

        elementos = []
        while actual is not None:
            elementos.append(
                f"[{actual.id_sensor}: {actual.lectura} PSI | "
                f"{actual.estado} | {actual.time}]"
            )
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

        #Purgar Eventos 

 def purgar_normales(self) -> int:
       
        eliminados = 0

        # Caso A: el uno es NORMAL (puede haber varias seguidas)
        while self.uno is not None and self.uno.estado.upper() == "NORMAL":
            self.uno = self.uno.siguiente   # avanzamos uno
            eliminados += 1

        # Caso B: nodos NORMAL en medio o al final → "puenteo"
        actual = self.uno
        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.estado.upper() == "NORMAL":
                actual.siguiente = actual.siguiente.siguiente  # saltamos el nodo
                eliminados += 1
            else:
                actual = actual.siguiente

        return eliminados     

        