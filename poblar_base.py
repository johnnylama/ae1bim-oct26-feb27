from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importan las clases del archivo crear_base_entidades
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se evita duplicar la información si el script se ejecuta más de una vez
if session.query(Clinica).count() > 0:
    print("La base de datos ya tiene información registrada.")
    session.close()
    raise SystemExit

# --------------------------------------------------------------
# Clínicas
# --------------------------------------------------------------
clinica1 = Clinica(nombre="PetSalud Loja", direccion="Av. Universitaria y 10 de Agosto, Loja",
                   medico_responsable="Dr. Andrés Jaramillo")
clinica2 = Clinica(nombre="VetCare Quito", direccion="Av. Amazonas N34-120, Quito",
                   medico_responsable="Dra. Gabriela Torres")
clinica3 = Clinica(nombre="Huellitas Cuenca", direccion="Calle Larga 7-45, Cuenca",
                   medico_responsable="Dr. Santiago Vintimilla")

session.add_all([clinica1, clinica2, clinica3])

# --------------------------------------------------------------
# Consultorios (cada uno pertenece a una sola clínica)
# --------------------------------------------------------------
consultorio1 = Consultorio(nombre="Consultorio 101", especialidad="Medicina general", clinica=clinica1)
consultorio2 = Consultorio(nombre="Consultorio 102", especialidad="Cirugía", clinica=clinica1)
consultorio3 = Consultorio(nombre="Consultorio A", especialidad="Dermatología", clinica=clinica2)
consultorio4 = Consultorio(nombre="Consultorio B", especialidad="Medicina general", clinica=clinica2)
consultorio5 = Consultorio(nombre="Consultorio 1", especialidad="Cardiología", clinica=clinica3)

session.add_all([consultorio1, consultorio2, consultorio3, consultorio4, consultorio5])

# --------------------------------------------------------------
# Veterinarios (cada uno pertenece a un solo consultorio)
# --------------------------------------------------------------
veterinario1 = Veterinario(nombres="María José", apellidos="Castillo Ruiz",
                           correo="mjcastillo@petsalud.ec", numero_licencia="LIC-VET-1001",
                           consultorio=consultorio1)
veterinario2 = Veterinario(nombres="Carlos", apellidos="Ordóñez Paz",
                           correo="cordonez@petsalud.ec", numero_licencia="LIC-VET-1002",
                           consultorio=consultorio2)
veterinario3 = Veterinario(nombres="Lucía", apellidos="Mendoza Vera",
                           correo="lmendoza@vetcare.ec", numero_licencia="LIC-VET-2001",
                           consultorio=consultorio3)
veterinario4 = Veterinario(nombres="Diego", apellidos="Salazar León",
                           correo="dsalazar@vetcare.ec", numero_licencia="LIC-VET-2002",
                           consultorio=consultorio4)
veterinario5 = Veterinario(nombres="Paola", apellidos="Cabrera Ochoa",
                           correo="pcabrera@huellitas.ec", numero_licencia="LIC-VET-3001",
                           consultorio=consultorio5)
veterinario6 = Veterinario(nombres="Javier", apellidos="Aguilar Romero",
                           correo="jaguilar@petsalud.ec", numero_licencia="LIC-VET-1003",
                           consultorio=consultorio1)

session.add_all([veterinario1, veterinario2, veterinario3,
                 veterinario4, veterinario5, veterinario6])

# --------------------------------------------------------------
# Historias Clínicas (cada una asociada al veterinario que la elaboró)
# --------------------------------------------------------------
historias = [
    HistoriaClinica(fecha_atencion=date(2026, 10, 2), nombre_mascota="Firulais",
                    diagnostico="Gastroenteritis", tratamiento="Dieta blanda y metronidazol",
                    veterinario=veterinario1),
    HistoriaClinica(fecha_atencion=date(2026, 10, 5), nombre_mascota="Michi",
                    diagnostico="Otitis externa", tratamiento="Gotas óticas por 7 días",
                    veterinario=veterinario1),
    HistoriaClinica(fecha_atencion=date(2026, 10, 9), nombre_mascota="Rocky",
                    diagnostico="Fractura de fémur", tratamiento="Cirugía de osteosíntesis",
                    veterinario=veterinario2),
    HistoriaClinica(fecha_atencion=date(2026, 10, 12), nombre_mascota="Luna",
                    diagnostico="Dermatitis alérgica", tratamiento="Antihistamínico y champú medicado",
                    veterinario=veterinario3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 15), nombre_mascota="Max",
                    diagnostico="Sarna demodécica", tratamiento="Ivermectina y baños semanales",
                    veterinario=veterinario3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 20), nombre_mascota="Toby",
                    diagnostico="Parvovirus", tratamiento="Hospitalización y fluidoterapia",
                    veterinario=veterinario4),
    HistoriaClinica(fecha_atencion=date(2026, 10, 28), nombre_mascota="Nala",
                    diagnostico="Soplo cardíaco", tratamiento="Enalapril y control mensual",
                    veterinario=veterinario5),
    HistoriaClinica(fecha_atencion=date(2026, 11, 3), nombre_mascota="Simba",
                    diagnostico="Gastroenteritis", tratamiento="Probióticos y suero oral",
                    veterinario=veterinario6),
    HistoriaClinica(fecha_atencion=date(2026, 11, 10), nombre_mascota="Coco",
                    diagnostico="Vacunación anual", tratamiento="Vacuna séxtuple y desparasitación",
                    veterinario=veterinario6),
    HistoriaClinica(fecha_atencion=date(2026, 11, 18), nombre_mascota="Bruno",
                    diagnostico="Cálculos renales", tratamiento="Dieta renal y analgésicos",
                    veterinario=veterinario4),
]

session.add_all(historias)

# se confirman los cambios en la base de datos
session.commit()
print("Información registrada correctamente.")
session.close()
