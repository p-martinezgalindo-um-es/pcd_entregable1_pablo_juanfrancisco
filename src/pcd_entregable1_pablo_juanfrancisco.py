from abc import ABCMeta, abstractmethod
from enum import Enum

class Sexo(Enum):
    V = 0
    M = 1

class Departamento(Enum):
    DIIC = 0
    DITEC = 1
    DIS = 2

class Asignaturas(Enum):
    ESTADISTICA = 0
    PROGRAMACION = 1
    OPTIMIZACION = 2
    ALGEBRA = 3
    CALCULO = 4

class tipoProfesor(Enum):
    ASOCIADO = 0
    TITULAR = 1

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    @abstractmethod
    def mostrarDatos(self):
        pass

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento=None):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def mostrarDatos(self):  # SE PUEDE QUITAR
        print('---- DATOS MIEMBRO DEPARTAMENTO ----')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento}\n')
    
    def asignarDepartamento(self, departamento):
        if self.departamento is None:
            self.departamento = departamento
        else: print('Ya tiene departamento asignado\n')

    def quitarDepartamento(self):
        self.departamento = None

    def cambiarDepartamento(self, departamento):
        self.departamento = departamento

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = []

    def mostrarDatos(self):
        print('---- DATOS ESTUDIANTE ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nAsignaturas: {self.asignaturas}\n')


    def mostrarAsignaturas(self):
        print('---- ASIGNATURAS ----\n')
        for asignatura in self.asignaturas:
            print(asignatura)
        print()

    
    def añadirAsignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
        else: print('Ya está añadida')

    def quitarAsignatura(self, asignatura):
        for i in range(len(self.asignaturas)):
            if self.asignaturas[i] == asignatura:
                self.asignaturas.remove(self.asignaturas[i])
                return

class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, areaInvestigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.areaInvestigacion = areaInvestigacion

    def mostrarDatos(self):
        print('---- DATOS INVESTIGADOR ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nArea: {self.areaInvestigacion}\n')

class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, tipo, areaInvestigacion=None):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas = []
        self.tipo = tipo
        self.areaInvestigacion = areaInvestigacion

    def mostrarDatos(self):
        print('---- DATOS PROFESOR ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nArea: {self.areaInvestigacion} \nTipo de profesor: {self.tipo}\n')        

    def añadirAsignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
        else: print('Ya está añadida')

    def quitarAsignatura(self, asignatura):
        if asignatura in self.asignaturas:
            for i in range(len(self.asignaturas)):
                if self.asignaturas[i] == asignatura:
                    self.asignaturas.remove(self.asignaturas[i])
                    return

    def mostrarAsignaturas(self):
        print('---- ASIGNATURAS ----\n')
        for asignatura in self.asignaturas:
            print(asignatura)
        print()

class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._estudiantes = []
        self._profesores = []
        self._investigadores = []

    def añadirEstudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
        else: print('Ya existe este estudiante')

    def añadirProfesor(self, profesor):
        if profesor not in self._profesores:
            self._profesores.append(profesor)
        else: print('Ya existe este profesor')

    def añadirInvestigador(self, investigador):
        if investigador not in self._investigadores:
            self._investigadores.append(investigador)
        else: print('Ya existe este investigador')

    def quitarEstudiante(self, estudiante):
        for i in range(len(self._estudiantes)):
            if self._estudiantes[i] == estudiante:
                self._estudiantes.remove(self._estudiantes[i])
                return

    def quitarProfesor(self, profesor):
        for i in range(len(self._profesores)):
            if self._profesores[i] == profesor:
                self._profesores.remove(self._profesores[i])
                return

    def quitarInvestigador(self, investigador):
        for i in range(len(self._investigadores)):
            if self._investigadores[i] == investigador:
                self._investigadores.remove(self._investigadores[i])
                return

    def listarEstudiantes(self):
        print('---- LISTADO DE ESTUDIANTES ----\n')
        for estudiante in self._estudiantes:
            print(estudiante.mostrarDatos(), '\n')

    def listarProfesores(self):
        print('---- LISTADO DE PROFESORES ----\n')
        for profesor in self._profesores:
            print(profesor.mostrarDatos(), '\n')
    
    def listarInvestigadores(self):
        print('---- LISTADO DE INVESTGADORES ----\n')
        for investigador in self._investigadores:
            print(investigador.mostrarDatos(), '\n')
    

# EJEMPLO DE USO
                
universidad = Universidad('Universidad de Murcia')

estudiante1 = Estudiante("Pablo", "23347636T", "Calle Rambla", Sexo.V)
estudiante2 = Estudiante("Juan Francisco", "23306585F", "Calle Gran Via", Sexo.V)
estudiante3 = Estudiante("Carmen", "23528569D", "Calle la Merced", Sexo.M)

universidad.añadirEstudiante(estudiante1)
universidad.añadirEstudiante(estudiante2)
universidad.añadirEstudiante(estudiante3)

profesor1 = Profesor("Humberto", "45869571G", "Calle Fuente Álamo", Sexo.V, Departamento.DIIC, tipoProfesor.TITULAR, 'Programación orientada a objetos')
profesor2 = Profesor("Félix", "45896235H", "Calle Traperia", Sexo.V, Departamento.DIS, tipoProfesor.ASOCIADO)
profesor3 = Profesor("Concepción", "26895741Y", "Calle Plateria", Sexo.M, Departamento.DITEC, tipoProfesor.TITULAR, 'Optimización')

universidad.añadirProfesor(profesor1)
universidad.añadirProfesor(profesor2)
universidad.añadirProfesor(profesor3)

investigador1 = Investigador("Claudi", "486957P", "Calle JC1", Sexo.V, Departamento.DIIC, 'Álgebra')
investigador2 = Investigador("María", "48575214K", "Calle Murcia", Sexo.M, Departamento.DITEC, 'Algorítmia')
investigador3 = Investigador("Carlos", "63325896G", "Calle Rectores", Sexo.V, Departamento.DIS, 'Cálculo')

universidad.añadirInvestigador(investigador1)
universidad.añadirInvestigador(investigador2)
universidad.añadirInvestigador(investigador3)

# universidad.listarEstudiantes()
# universidad.listarProfesores()
# universidad.listarInvestigadores()

estudiante1.añadirAsignatura(Asignaturas.ALGEBRA)
estudiante1.añadirAsignatura(Asignaturas.ESTADISTICA)
estudiante1.añadirAsignatura(Asignaturas.OPTIMIZACION)
estudiante1.añadirAsignatura(Asignaturas.PROGRAMACION)
# estudiante1.añadirAsignatura(Asignaturas.PROGRAMACION)
estudiante1.añadirAsignatura(Asignaturas.CALCULO)
estudiante1.quitarAsignatura(Asignaturas.OPTIMIZACION)

# estudiante1.mostrarAsignaturas()

estudiante2.añadirAsignatura(Asignaturas.ALGEBRA)
estudiante2.añadirAsignatura(Asignaturas.ESTADISTICA)
estudiante2.añadirAsignatura(Asignaturas.OPTIMIZACION)
estudiante2.añadirAsignatura(Asignaturas.PROGRAMACION)
estudiante2.añadirAsignatura(Asignaturas.CALCULO)

estudiante3.añadirAsignatura(Asignaturas.ALGEBRA)
estudiante3.añadirAsignatura(Asignaturas.ESTADISTICA)
estudiante3.añadirAsignatura(Asignaturas.OPTIMIZACION)
estudiante3.añadirAsignatura(Asignaturas.PROGRAMACION)
estudiante3.añadirAsignatura(Asignaturas.CALCULO)

# investigador1.mostrarDatos()

profesor1.añadirAsignatura(Asignaturas.PROGRAMACION)
profesor1.añadirAsignatura(Asignaturas.CALCULO)
profesor1.quitarAsignatura(Asignaturas.CALCULO)

profesor2.añadirAsignatura(Asignaturas.ESTADISTICA)
profesor2.añadirAsignatura(Asignaturas.ALGEBRA)

profesor3.añadirAsignatura(Asignaturas.OPTIMIZACION)
profesor3.añadirAsignatura(Asignaturas.CALCULO)


# profesor1.asignarDepartamento(Departamento.DIS)
# profesor1.cambiarDepartamento(Departamento.DITEC)
# profesor1.mostrarDatos()
# profesor1.mostrarAsignaturas()


universidad.quitarEstudiante(estudiante3)
universidad.quitarProfesor(profesor3)
universidad.quitarInvestigador(investigador3)

# universidad.listarEstudiantes()
# universidad.listarProfesores()
# universidad.listarInvestigadores()