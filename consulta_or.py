from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

# se importan las clases del archivo crear_base_entidades
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------------------------------------
# Uso de or_
# --------------------------------------------------------------
print("========== Clínicas ubicadas en Quito o en Cuenca ==========")
clinicas = session.query(Clinica).filter(
    or_(Clinica.direccion.like("%Quito%"),
        Clinica.direccion.like("%Cuenca%"))).all()
for c in clinicas:
    print(c)

print("========== Consultorios de Cirugía o Dermatología ==========")
consultorios = session.query(Consultorio).filter(
    or_(Consultorio.especialidad == "Cirugía",
        Consultorio.especialidad == "Dermatología")).all()
for c in consultorios:
    print(c)

print("========== Veterinarios con nombre 'Lucía' o correo del dominio 'huellitas.ec' ==========")
veterinarios = session.query(Veterinario).filter(
    or_(Veterinario.nombres == "Lucía",
        Veterinario.correo.like("%@huellitas.ec"))).all()
for v in veterinarios:
    print(v)

print("========== Historias clínicas de la mascota 'Luna' o con diagnóstico 'Parvovirus' ==========")
historias = session.query(HistoriaClinica).filter(
    or_(HistoriaClinica.nombre_mascota == "Luna",
        HistoriaClinica.diagnostico == "Parvovirus")).all()
for h in historias:
    print(h)

session.close()
