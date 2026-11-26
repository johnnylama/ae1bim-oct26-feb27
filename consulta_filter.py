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
# Uso de filter
# --------------------------------------------------------------
print("========== Clínicas cuya dirección contiene 'Loja' ==========")
clinicas = session.query(Clinica).filter(Clinica.direccion.like("%Loja%")).all()
for c in clinicas:
    print(c)

print("========== Consultorios con especialidad 'Medicina general' ==========")
consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina general").all()
for c in consultorios:
    print(c)

print("========== Veterinarios que trabajan en la clínica 'VetCare Quito' ==========")
veterinarios = session.query(Veterinario).join(Consultorio).join(Clinica).filter(
    Clinica.nombre == "VetCare Quito").all()
for v in veterinarios:
    print(v)

print("========== Historias clínicas con diagnóstico 'Gastroenteritis' ==========")
historias = session.query(HistoriaClinica).filter(
    HistoriaClinica.diagnostico == "Gastroenteritis").all()
for h in historias:
    print(h)

session.close()
