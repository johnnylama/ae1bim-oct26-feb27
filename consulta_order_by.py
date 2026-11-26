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
# Uso de order_by
# --------------------------------------------------------------
print("========== Clínicas ordenadas por nombre (ascendente) ==========")
for c in session.query(Clinica).order_by(Clinica.nombre).all():
    print(c)

print("========== Consultorios ordenados por especialidad y nombre ==========")
for c in session.query(Consultorio).order_by(Consultorio.especialidad, Consultorio.nombre).all():
    print(c)

print("========== Veterinarios ordenados por apellidos (descendente) ==========")
for v in session.query(Veterinario).order_by(Veterinario.apellidos.desc()).all():
    print(v)

print("========== Historias clínicas ordenadas por fecha (más reciente primero) ==========")
for h in session.query(HistoriaClinica).order_by(HistoriaClinica.fecha_atencion.desc()).all():
    print(h)

session.close()
