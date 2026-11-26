from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera el enlace al gestor de base de datos
# para la actividad se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Clinica(Base):
    """
    Unidad de atención de la red de clínicas veterinarias.
    """
    __tablename__ = 'clinica'
    id = Column(Integer, primary_key=True)        # identificador único
    nombre = Column(String(100), nullable=False)  # nombre comercial
    direccion = Column(String(200), nullable=False)
    medico_responsable = Column(String(150), nullable=False)

    # una clínica tiene uno o varios consultorios
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return "Clínica: id=%d nombre=%s dirección=%s médico responsable=%s" % (
            self.id, self.nombre, self.direccion, self.medico_responsable)


class Consultorio(Base):
    """
    Consultorio que pertenece obligatoriamente a una sola clínica.
    """
    __tablename__ = 'consultorio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)        # nombre o número
    especialidad = Column(String(100), nullable=False)  # medicina general, cirugía, ...

    clinica_id = Column(Integer, ForeignKey('clinica.id'), nullable=False)
    clinica = relationship("Clinica", back_populates="consultorios")

    # un consultorio cuenta con uno o varios veterinarios
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return "Consultorio: id=%d nombre=%s especialidad=%s clínica=%s" % (
            self.id, self.nombre, self.especialidad, self.clinica.nombre)


class Veterinario(Base):
    """
    Veterinario que pertenece únicamente a un consultorio.
    """
    __tablename__ = 'veterinario'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    numero_licencia = Column(String(50), nullable=False, unique=True)

    consultorio_id = Column(Integer, ForeignKey('consultorio.id'), nullable=False)
    consultorio = relationship("Consultorio", back_populates="veterinarios")

    # un veterinario elabora varias historias clínicas
    historias = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return "Veterinario: id=%d %s %s correo=%s licencia=%s consultorio=%s" % (
            self.id, self.nombres, self.apellidos, self.correo,
            self.numero_licencia, self.consultorio.nombre)


class HistoriaClinica(Base):
    """
    Registro de la atención brindada a una mascota.
    Asociada obligatoriamente al veterinario que la elaboró.
    """
    __tablename__ = 'historia_clinica'
    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(250), nullable=False)
    tratamiento = Column(String(250), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)

    veterinario_id = Column(Integer, ForeignKey('veterinario.id'), nullable=False)
    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return "Historia Clínica: id=%d fecha=%s mascota=%s diagnóstico=%s tratamiento=%s veterinario=%s %s" % (
            self.id, self.fecha_atencion, self.nombre_mascota, self.diagnostico,
            self.tratamiento, self.veterinario.nombres, self.veterinario.apellidos)


# se crean las tablas en la base de datos
Base.metadata.create_all(engine)
