import datetime

class Alumno:
    nombre: str
    apellido: str
    edad: int
    fechaNacimiento: datetime.date
    
    def __init__(self, nombre, apellido,fechaNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        
    def obtenerEdad(self):
       return (datetime.date.today() - self.fechaNacimiento) //365