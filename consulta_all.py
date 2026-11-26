from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importan las clases del archivo crear_base_entidades
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------------------------------------
# Uso de all: se obtienen todos los registros de cada entidad
# --------------------------------------------------------------
print("========== Todas las clínicas ==========")
for c in session.query(Clinica).all():
    print(c)

print("========== Todos los consultorios ==========")
for c in session.query(Consultorio).all():
    print(c)

print("========== Todos los veterinarios ==========")
for v in session.query(Veterinario).all():
    print(v)

print("========== Todas las historias clínicas ==========")
for h in session.query(HistoriaClinica).all():
    print(h)

# --------------------------------------------------------------
# Clínicas y, por cada una, el número de Historias Clínicas
# asociadas (Clínica -> Consultorios -> Veterinarios -> Historias)
# --------------------------------------------------------------
print("========== Número de historias clínicas por clínica ==========")
clinicas = session.query(Clinica).all()
for clinica in clinicas:
    numero_historias = 0
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            numero_historias = numero_historias + len(veterinario.historias)
    print("Clínica: %s - Número de historias clínicas: %d" % (clinica.nombre, numero_historias))

session.close()
