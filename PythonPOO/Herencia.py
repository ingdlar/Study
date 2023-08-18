class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")
    
"""Empleado hereda de persona, entre parentesis se pone la clase de la cual vamos a heredar"""
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo, salario):
        """Con super elegimos cuales propiedades de la clase padre vamos a heredar"""
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    
    """El metodo sobre escribe el metodo de la clase padre o de la super clase"""
    def hablar(self):
        print("NO")

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,universidad,notas):
        """Con super elegimos cuales propiedades de la clase padre vamos a heredar"""
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad
    
    """El metodo sobre escribe el metodo de la clase padre o de la super clase"""
    def hablar(self):
        print("NO")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

"""Herencia multiple. En el constructor __init_ debe llamar a la clase directamente"""
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init_(self,nombre,edad,nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

roberto = Empleado("Roberto",43,"Argentino","Programador",100000)

roberto.hablar()