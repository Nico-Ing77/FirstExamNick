class Glosario:

    def __init__(self) -> None:
        self.terminos: dict[str, str] = {}

    def agregar_termino (self,palabra:str,concepto:str) ->None:
        palabra_actual= palabra.strip()
        self.terminos[palabra_actual] = concepto.strip()
        return f"Termino guardado {palabra_actual.upper()}"
    
    def buscar_termino(self,palabra:str) -> str:
        palabra_buscar= palabra.strip()
        concepto = self.terminos.get(palabra_buscar) 
        if concepto:
            return f'{palabra}:{concepto}'
        else:
            return f"No existe el concepto de {palabra_buscar}" 
        
    def mostrar_todos (self) -> None:
        if not self.terminos:
            print("No hay glosario")
            return
        for palabra,concepto in self.terminos.items():
            print(f'{palabra}:{concepto}')

if __name__=="__main__":
    glosario=Glosario()
    glosario.agregar_termino("Sensor","es un dispositivo que detecta un cambio o estimulo fisico o quimico en su entorno")
    glosario.agregar_termino("Horno","es un aparato cerrado que genera y conserva calor en su interior")
    glosario.agregar_termino("Muestra","Subconjunto o una parte representativa de un conjunto")
    glosario.agregar_termino("Control","conjunto de dispositivos, para gobernar el comportamiento de un sistema")

    buscar=glosario.buscar_termino("condicional")
    print(buscar)
    glosario.mostrar_todos()

    # Examen 10 preguntas teoricas de 7 a 9 + Practica como sensor de temperatura 