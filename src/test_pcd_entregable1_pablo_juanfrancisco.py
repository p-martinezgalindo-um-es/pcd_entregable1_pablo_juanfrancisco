# archivo: test_mi_codigo.py
from pcd_entregable1_pablo_juanfrancisco import (
    Sexo,
    Departamento,
    Asignaturas,
    tipoProfesor,
    Persona,
    MiembroDepartamento,
    Estudiante,
    Investigador,
    Profesor,
    Universidad
)

def test_miembro_departamento():
    # Creamos una instancia de MiembroDepartamento
    miembro = MiembroDepartamento("Juan", "12345678A", "Calle Falsa 123", Sexo.M)
    
    # Probamos el método asignarDepartamento()
    miembro.asignarDepartamento(Departamento.DITEC)
    assert miembro.departamento == Departamento.DITEC

    # Probamos el método cambiarDepartamento()
    miembro.cambiarDepartamento(Departamento.DIIC)
    assert miembro.departamento == Departamento.DIIC

    # Probamos el método quitarDepartamento()
    miembro.quitarDepartamento()
    assert miembro.departamento == None
    

def test_estudiante():
    # Creamos una instancia de Estudiante
    estudiante = Estudiante("Maria", "87654321B", "Calle Real 456", Sexo.V)

    # Probamos el método añadirAsignatura()
    estudiante.añadirAsignatura(Asignaturas.ESTADISTICA)
    assert Asignaturas.ESTADISTICA in estudiante._asignaturas

    # Probamos el método quitarAsignatura()
    estudiante.quitarAsignatura(Asignaturas.ESTADISTICA)
    assert Asignaturas.ESTADISTICA not in estudiante._asignaturas


def test_profesor():
    # Creamos una instancia de Profesor
    profesor = Profesor("Ana", "34567890D", "Calle Mayor 012", Sexo.V, Departamento.DIIC, tipoProfesor.TITULAR)

    # Probamos el método añadirArea()
    profesor.añadirArea("Machine Learning")
    assert profesor._areaInvestigacion == "Machine Learning"

    # Probamos el método cambiarTipo()
    profesor.cambiarTipo()
    assert profesor.tipo == tipoProfesor.ASOCIADO

    # Probamos el método añadirAsignatura()
    profesor.añadirAsignatura(Asignaturas.PROGRAMACION)
    assert Asignaturas.PROGRAMACION in profesor._asignaturas

    # Probamos el método quitarAsignatura()
    profesor.quitarAsignatura(Asignaturas.PROGRAMACION)
    assert Asignaturas.PROGRAMACION not in profesor._asignaturas

def test_universidad():
    # Creamos una instancia de Universidad
    universidad = Universidad("Universidad X")

    # Probamos los métodos añadirEstudiante(), añadirProfesor(), añadirInvestigador()
    estudiante = Estudiante("Laura", "45678901E", "Calle Estudiantil 345", Sexo.V)
    profesor = Profesor("Daniel", "56789012F", "Calle Profesorado 678", Sexo.M, Departamento.DIIC, tipoProfesor.ASOCIADO)
    investigador = Investigador("Sofia", "67890123G", "Calle Investigacion 901", Sexo.V, Departamento.DITEC, "Big Data")
    universidad.añadirEstudiante(estudiante)
    universidad.añadirProfesor(profesor)
    universidad.añadirInvestigador(investigador)

    assert estudiante in universidad._estudiantes
    assert profesor in universidad._profesores
    assert investigador in universidad._investigadores

    # Probamos los métodos quitarEstudiante(), quitarProfesor(), quitarInvestigador()
    universidad.quitarEstudiante(estudiante)
    universidad.quitarProfesor(profesor)
    universidad.quitarInvestigador(investigador)

    assert estudiante not in universidad._estudiantes
    assert profesor not in universidad._profesores
    assert investigador not in universidad._investigadores


if __name__ == "__main__":
    import pytest
    pytest.main()
