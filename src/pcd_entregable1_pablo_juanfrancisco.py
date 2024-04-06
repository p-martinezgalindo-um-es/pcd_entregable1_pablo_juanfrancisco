from abc import ABCMeta, abstractmethod
from enum import Enum

class Sexo(Enum): # Se relaciona con persona mediante una composición ya que no existe una sin la otra.
    V = 0
    M = 1

class Departamento(Enum): # Se trata de una agragación porque puede existir un departamento sin miembro.
    DIIC = 0
    DITEC = 1
    DIS = 2

class Asignaturas(Enum): # Es una agregación porque puede existir un profesor y estudiante que no tengan asignada ninguna asignatura y viceversa
    ESTADISTICA = 0
    PROGRAMACION = 1
    OPTIMIZACION = 2
    ALGEBRA = 3
    CALCULO = 4

class tipoProfesor(Enum): # Ocurre lo mismo que en la enumeración Sexo ya que solo pueden existir esos dos tipos de profesores
    ASOCIADO = 0
    TITULAR = 1

class Persona(metaclass=ABCMeta): # Creamos clase persona con atributos nombre, dni, dirección y sexo.
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    
    @abstractmethod
    def mostrarDatos(self): # Establecemos la función mostrarDatos como obligatoria en las clases que heredan de persona
            pass

class MiembroDepartamento(Persona): # Creamos la clase MiembroDepartamento que hereda de persona para añadirle el atributo de departamento
    def __init__(self, nombre, dni, direccion, sexo, departamento=None):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def mostrarDatos(self):  
        print('---- DATOS MIEMBRO DEPARTAMENTO ----')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento}\n')
    
    def asignarDepartamento(self, departamento):
        try:
            if self.departamento is None:
                self.departamento = departamento
            else:
                raise ValueError(f'{self.nombre} ya tiene departamento asignado')
        except ValueError as e:
            print(e)

    def quitarDepartamento(self):
        try:
            if self.departamento is not None:
                self.departamento = None
            else:
                raise ValueError(f'{self.nombre} no tiene ningún departamento asignado') 
        except ValueError as e:
            print(e)

    def cambiarDepartamento(self, departamento):
        try:
            if self.departamento is not None:
                self.departamento = departamento
            else:
                raise ValueError(f'{self.nombre} no tiene ningún departamento asignado') 
        except ValueError as e:
            print(e)

class Estudiante(Persona): # Creamos la clase Estudiante que también hereda de Persona y que tendrá otro atributo que será asignaturas 
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self._asignaturas = [] # Creamos el atributo asignaturas que será una lista de las asignaturas añadidas del estudiante.

    def mostrarDatos(self):
        print('---- DATOS ESTUDIANTE ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo}\n')

    def mostrarAsignaturas(self):
        print('---- ASIGNATURAS ----\n')
        for asignatura in self._asignaturas:
            print(asignatura)
        print()

    def añadirAsignatura(self, asignatura):
        try:
            if asignatura not in self._asignaturas:
                self._asignaturas.append(asignatura)
            else: 
                raise ValueError(f'ERROR. {asignatura} ya ha sido añadida anteriormente')
        except ValueError as e:
            print(e)

    def quitarAsignatura(self, asignatura):
        try:
            if asignatura in self._asignaturas:
                self._asignaturas.remove(asignatura)
            else: 
                raise ValueError(f'ERROR. La asignatura propuesta para ser eliminada no se encuentra entre las disponibles del estudiante')
        except ValueError as e:
            print(e)

class Investigador(MiembroDepartamento): # Creamos la clase Investigador que hereda de MiembroDepartamento y añadimos el atributo areaInvestigacion
    def __init__(self, nombre, dni, direccion, sexo, departamento, areaInvestigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.areaInvestigacion = areaInvestigacion

    def mostrarDatos(self):
        print('---- DATOS INVESTIGADOR ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nArea: {self.areaInvestigacion}\n')

class Profesor(MiembroDepartamento): # Creamos la clase Profesor que hereda de MiembroDepartamento y añadimos los atributos asignaturas, tipo y areaInvestigacion
    def __init__(self, nombre, dni, direccion, sexo, departamento, tipo):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self._asignaturas = []  # Creamos el atributo asignaturas que será una lista de las asignaturas añadidas del profesor.
        self.tipo = tipo 
        self._areaInvestigacion = None # Creamos el atributo de areaInvestigacion para poder añadirle un area de investigación a los profesores titulares.

    def mostrarDatos(self):
        print('---- DATOS PROFESOR ----\n')
        print(f'Nombre: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo} \nDepartamento: {self.departamento} \nArea: {self._areaInvestigacion} \nTipo de profesor: {self.tipo}\n')        

    def añadirAsignatura(self, asignatura):
        try:
            if asignatura not in self._asignaturas:
                self._asignaturas.append(asignatura)
            else: 
                raise ValueError(f'ERROR. {asignatura} ya ha sido añadida anteriormente')
        except ValueError as e:
            print(e)

    def cambiarTipo(self):
        if self.tipo is tipoProfesor.TITULAR:
                self._areaInvestigacion = None
                self.tipo = tipoProfesor.ASOCIADO
        else: self.tipo = tipoProfesor.TITULAR
        
    def añadirArea(self, area):
        try:
            if self.tipo is tipoProfesor.TITULAR:
                self._areaInvestigacion = area
            else: 
                raise ValueError(f'ERROR. El profesor al que se le está intentando añadir un área de investigación es de tipo ASOCIADO.')
        except ValueError as e:
            print(e)

    def quitarAsignatura(self, asignatura):
        try:
            if asignatura in self._asignaturas:
                self._asignaturas.remove(asignatura)
            else: 
                raise ValueError(f'ERROR. La asignatura propuesta para ser eliminada no se encuentra entre las disponibles del estudiante')
        except ValueError as e:
            print(e)

    def mostrarAsignaturas(self):
        print('---- ASIGNATURAS ----\n')
        for asignatura in self._asignaturas:
            print(asignatura)
        print()

class Universidad: # Creamos la clase Universidad para gestionar todos los estudiantes, profesores e investigadores registrados
    def __init__(self, nombre):
        self.nombre = nombre
        self._estudiantes = [] # Establecemos como privados las listas de estudiantes, profesores e investigadores, lo cual concuerda con
        self._profesores = []  # las cardinalidades del esquema UML, existiendo la posibilidad de haber una universidad sin estudiantes, profesores ni investigadores.
        self._investigadores = []

    def añadirEstudiante(self, estudiante):
        
        try:
            if estudiante not in self._estudiantes:
                self._estudiantes.append(estudiante)
            
            else: 
                raise ValueError(f'ERROR. Estudiante ya añadido')
        
        except ValueError as e:
            print(e)

    def añadirProfesor(self, profesor):
        try:
            if profesor not in self._profesores:
                self._profesores.append(profesor)
            else: 
                raise ValueError(f'ERROR. Profesor ya añadido')
        except ValueError as e:
            print(e)

    def añadirInvestigador(self, investigador):
        try:
            if investigador not in self._investigadores:
                self._investigadores.append(investigador)
            else: 
                raise ValueError(f'ERROR. Ivestigador ya añadido')
            
        except ValueError as e:
            print(e)

    def quitarEstudiante(self, estudiante):
        try:
            if estudiante in self._estudiantes:
                self._estudiantes.remove(estudiante)
            else:
                raise ValueError(f'ERROR. Estudiante no añadido')
            
        except ValueError as e:
            print(e)
        

    def quitarProfesor(self, profesor):
        try:
            if profesor in self._profesores:
                self._profesores.remove(profesor)
            else:
                raise ValueError(f'ERROR. Profesor no añadido')
            
        except ValueError as e:
            print(e)

    def quitarInvestigador(self, investigador):
        try:
            if investigador in self._investigadores:
                self._investigadores.remove(investigador)
            else:
                raise ValueError(f'ERROR. Investigadores no añadido')
            
        except ValueError as e:
            print(e)

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

profesor1 = Profesor("Humberto", "45869571G", "Calle Fuente Álamo", Sexo.V, Departamento.DIIC, tipoProfesor.TITULAR)
profesor2 = Profesor("Félix", "45896235H", "Calle Traperia", Sexo.V, Departamento.DIS, tipoProfesor.ASOCIADO)
profesor3 = Profesor("Concepción", "26895741Y", "Calle Plateria", Sexo.M, Departamento.DITEC, tipoProfesor.TITULAR)

profesor1.añadirArea('Programación orientada a objetos')
profesor3.añadirArea('Optimización')
profesor2.cambiarTipo()


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

profesor1.mostrarDatos()
