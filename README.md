# ae1bim-oct26-feb27

Actividad APEB1: uso de ORM con SQLAlchemy (Python + SQLite) sobre una red de clínicas veterinarias.

## Modelo

- **Clinica**: id, nombre, direccion, medico_responsable
- **Consultorio**: id, nombre, especialidad, clinica_id (obligatorio, una sola clínica)
- **Veterinario**: id, nombres, apellidos, correo, numero_licencia, consultorio_id (obligatorio)
- **HistoriaClinica**: id, fecha_atencion, diagnostico, tratamiento, nombre_mascota, veterinario_id (obligatorio)

Relaciones: Clínica 1—N Consultorio 1—N Veterinario 1—N HistoriaClinica.

## Archivos

| Archivo | Descripción |
|---|---|
| `configuracion.py` | Cadena de conexión a la base de datos SQLite |
| `crear_base_entidades.py` | Definición de las entidades y creación de las tablas |
| `poblar_base.py` | Ingreso de datos a las entidades |
| `consulta_all.py` | Consultas con `all` y número de historias clínicas por clínica |
| `consulta_filter.py` | Consultas con `filter` |
| `consulta_order_by.py` | Consultas con `order_by` |
| `consulta_or.py` | Consultas con `or_` |
| `consulta_and.py` | Consultas con `and_` |

## Ejecución

```bash
pip install sqlalchemy
python crear_base_entidades.py
python poblar_base.py
python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py
```
