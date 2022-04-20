#definición de clase
import enum

class Persona():
    def __init__(self,nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

class Estudiante(Persona):
    def __init(self, codigoEstudiante, semestre):
        self.codigoEstudiante =  codigoEstudiante
        self.semestre = semestre

class MallaCurricular:
    pass

class Materia:
    def __init__(self, codigoM, tipoM, semestre, nombreMat, numeroCred, preferencia):
        self.codigoM = codigoM
        self.tipoM =  tipoM
        self.semestre =  semestre
        self.nombreMat =  nombreMat
        self.numeroCred =  numeroCred
        self.preferencia = preferencia


class Electiva(Materia):
    def __init__(self,nombreElect, tipoM, preferencia, semestre):
        super().__init__(tipoM, preferencia, semestre)
        self.nombreElect = nombreElect

class Obligatoria(Materia):
    def __init__(self, nombreA, tipoM, preferencia, semestre):
        super().__init__(tipoM, preferencia, semestre)
        self.nombreA = nombreA


#por implementar
class ActividadesExtra:
    pass

class Nelectiva(enum):
    pass

class Textra(enum): 
    Textra = ["Cedula",
    "Tarjeta_de_identidad",
    "Registro civil" ]

class TSemestre(enum):
    pass

class TDOc(enum):
    pass







