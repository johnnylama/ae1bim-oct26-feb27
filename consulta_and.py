from datetime import date

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

# se importan las clases del archivo crear_base_entidades
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------------------------------------
# Uso de and_
# --------------------------------------------------------------
print("========== Clínicas en Loja cuyo responsable es 'Dr. Andrés Jaramillo' ==========")
clinicas = session.query(Clinica).filter(
    and_(Clinica.direccion.like("%Loja%"),
         Clinica.medico_responsable == "Dr. Andrés Jaramillo")).all()
for c in clinicas:
    print(c)

print("========== Consultorios de 'Medicina general' en la clínica 'PetSalud Loja' ==========")
consultorios = session.query(Consultorio).join(Clinica).filter(
    and_(Consultorio.especialidad == "Medicina general",
         Clinica.nombre == "PetSalud Loja")).all()
for c in consultorios:
    print(c)

print("========== Veterinarios del dominio 'petsalud.ec' en consultorios de 'Medicina general' ==========")
veterinarios = session.query(Veterinario).join(Consultorio).filter(
    and_(Veterinario.correo.like("%@petsalud.ec"),
         Consultorio.especialidad == "Medicina general")).all()
for v in veterinarios:
    print(v)

print("========== Historias clínicas de 'Gastroenteritis' atendidas en noviembre de 2026 ==========")
historias = session.query(HistoriaClinica).filter(
    and_(HistoriaClinica.diagnostico == "Gastroenteritis",
         HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
         HistoriaClinica.fecha_atencion <= date(2026, 11, 30))).all()
for h in historias:
    print(h)

session.close()
