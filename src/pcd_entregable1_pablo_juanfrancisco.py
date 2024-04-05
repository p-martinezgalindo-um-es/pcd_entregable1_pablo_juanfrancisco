class Sexo:  
    V = 1
    M = 2

class Departamento:
    DIIC = 1
    DITEC = 2
    DIS = 3

class Asignaturas:
    MATEMATICAS = 1
    LENGUA = 2
    BIOLOGIA = 3
    HISTORIA = 4
    INGLES = 5

from abc import ABCMeta, abstractmethod

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    @abstractmethod
    def mostraDatos(self):
        pass

class Miembro_departamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def mostraDatos(self):
        datos_persona = super().mostraDatos()
        return f"{datos_persona}, Departamento: {self.departamento}"
    
    def cambiarDepartamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
    
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = []

    def mostrarDatos(self):
        datos_persona = super().mostrarDatos()
        asignaturas_str = ", ".join(str(a) for a in self.asignaturas)
        return f"{datos_persona}, Asignaturas: {asignaturas_str}"

    def mostrarAsignaturas(self, asignaturas):
        for i in asignaturas:
            print(i)

    def añadirAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def quitarAsignatura(self, asignatura):
        for i in range(len(self.asignaturas)-1):
            if self.asignaturas[i] == asignatura:
                self.asignaturas.remove(i)

        
class Investigador(Miembro_departamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion #OCULTO???
        
    def mostraDatos(self):
        datos_persona = super().mostraDatos()
        return f"{datos_persona}, Area: {self.area_investigacion}"
    
class Profesor(Miembro_departamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion=None):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas = []
        self.area_investigacion = area_investigacion

    def mostraDatos(self):
        if self.area_investigacion is not None:
            datos_persona = super().mostraDatos()
            return f"{datos_persona}, Area: {self.area_investigacion}, Tipo de profesor: Titular"
        else:
            datos_persona = super().mostraDatos()
            return f"{datos_persona}, Tipo de profesor: Asociado"

    def añadirAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def quitarAsignatura(self, asignatura):
        for i in range(len(self.asignaturas)-1):
            if self.asignaturas[i] == asignatura:
                self.asignaturas.remove(i)
 
    

class Universidad:
    def __init__(self, nombre, estudiantes, profesores, investigadores):
        self._nombre = nombre
        self._estudiantes = estudiantes
        self._profesores = profesores
        self.investigadores = investigadores

    def añadirEstudiante(self, estudiante): #comprobar q no existe el mismo estudiante
        self._estudiantes.append(estudiante)

    def añadirProfesor(self, profesor):
        self._estudiantes.append(profesor)

    def añadirInvestigador(self, investigador):
        self._estudiantes.append(investigador)

    def añadirMiembroDepartamento(self, persona, departamento):
        Miembro_departamento(persona.nombre, persona.dni,persona.direccion, persona.sexo, departamento)
        
    def quitarEstudiante(self, estudiante):
        for i in range(len(self._estudiantes)-1):
            if self._estudiantes[i] == estudiante:
                self._estudiantes.remove(i)

    def quitarProfesor(self, profesor):
        for i in range(len(self._estudiantes)-1):
            if self._profesores[i] == profesor:
                self._profesores.remove(i)

    def quitarProfesor(self, profesor):
        for i in range(len(self._estudiantes)-1):
            if self._profesores[i] == profesor:
                self._profesores.remove(i)

    def quitarMiembroDepartamento(self, miembro):
        for i in range(len(self._estudiantes)-1):
            if self._profesores[i] == profesor:
                self._profesores.remove(i)
        
    

#EJEMPLO DE EJECUCIÓN


