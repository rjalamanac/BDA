class Partido:
    def __init__(self, name, estadio, golesVisitante,golesLocal, fechaInicioPartido,fechaFinalPartido):
        self.id = None,
        self.name = name
        self.estadio = estadio
        self.golesLocal = golesLocal
        self.golesVisitante = golesVisitante
        self.fechaInicioPartido = fechaInicioPartido
        self.fechaFinalPartido = fechaFinalPartido
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}, estadio: {self.estadio}, fechaInicioPartido: {self.fechaInicioPartido}'
    
