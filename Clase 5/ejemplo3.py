#Algorito de busqueda y eliminacion de nodos de memoria ram
class NodoSensor:
    """Representa un elemento individual en la memoria RAM (Unidad 3.3)."""

    def __init__(self, id_sensor: str, lectura: float) -> None:
        self.id_sensor: str = id_sensor
        self.lectura: float = lectura
        self.siguiente: "NodoSensor | None" = None

class ListaEnlazadaSensores:
    """Clase gestora que administra la cadena de nodos dinámicos."""

    def __init__(self) -> None:
        self.cabeza: "NodoSensor | None" = None

    def insertar_inicio(self, id_sensor: str, lectura: float) -> None:
        """Inserta un nodo al inicio de la cadena en tiempo O(1)."""
        nuevo_nodo = NodoSensor(id_sensor, lectura)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, id_sensor: str, lectura: float) -> None:
        """Inserta un nodo al final de la cadena recorriendo la memoria O(N)."""
        nuevo_nodo = NodoSensor(id_sensor, lectura)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self) -> None:
        """Recorre la lista e imprime la secuencia ordenada de sensores."""
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
            return

        elementos = []
        while actual is not None:
            elementos.append(f"[{actual.id_sensor}: {actual.lectura}°C]")
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")


class ListaEnlazadaAvanzada(ListaEnlazadaSensores):
    """Extensión de la clase gestora con búsqueda y eliminación de memoria."""

    def buscar_sensor(self, id_sensor: str) -> bool:
        """Busca si un sensor existe en la estructura dinámicamente."""
        actual = self.cabeza
        while actual is not None:
            if actual.id_sensor == id_sensor:
                return True
            actual = actual.siguiente
        return False

    def eliminar_sensor(self, id_sensor: str) -> bool:
        """Elimina un nodo desconectando sus referencias en la RAM."""
        actual = self.cabeza
        anterior: "NodoSensor | None" = None

        if actual is None:
            return False  # La lista está vacía

        # Caso 1: El nodo a eliminar es la cabeza de la lista
        if actual.id_sensor == id_sensor:
            self.cabeza = actual.siguiente  # Avanzamos la cabeza
            return True

        # Caso 2: El nodo está en el medio o al final
        while actual is not None and actual.id_sensor != id_sensor:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False  # El sensor no se encontró en la lista

        # Reconexión de punteros (se "puentea" el nodo actual)
        anterior.siguiente = actual.siguiente
        return True


# --- PRUEBA DE BÚSQUEDA Y ELIMINACIÓN ---
red_sensores = ListaEnlazadaAvanzada()
red_sensores.insertar_final("S_01", 18.2)
red_sensores.insertar_final("S_ERRONEO", -999.0)  # Lectura ruidosa a eliminar
red_sensores.insertar_final("S_03", 21.4)

print("=== ANTES DE LA ELIMINACIÓN ===")
red_sensores.mostrar_lista()

# Búsqueda
print(f"\n¿Existe S_ERRONEO?: {red_sensores.buscar_sensor('S_ERRONEO')}")

# Eliminación y reconexión
red_sensores.eliminar_sensor("S_ERRONEO")

print("\n=== DESPUÉS DE ELIMINAR Y PUENTEAR EN RAM ===")
red_sensores.mostrar_lista()