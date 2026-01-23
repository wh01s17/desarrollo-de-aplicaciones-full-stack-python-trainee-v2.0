# Diccionario de datos - Universidad

## 1) Entidad: estudiante

| Campo  | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones                                  |
| ------ | ------------ | ------------: | -------------: | ------------: | ---------------------------------------------- |
| rut    | VARCHAR(10)  |            No |             Sí |            No | Identificador único del estudiante (RUT).      |
| nombre | VARCHAR(120) |            No |             No |            No | Nombre del estudiante.                         |
| correo | VARCHAR(120) |            No |             No |            No | Correo del estudiante. Se recomienda `UNIQUE`. |

## 2) Entidad: curso

| Campo               | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones                                                                        |
| ------------------- | ------------ | ------------: | -------------: | ------------: | ------------------------------------------------------------------------------------ |
| codigo              | VARCHAR(20)  |            No |             Sí |            No | Identificador único del curso.                                                       |
| nombre              | VARCHAR(160) |            No |             No |            No | Nombre del curso.                                                                    |
| docente_responsable | VARCHAR(120) |            No |             No |            No | Nombre del docente responsable (no se modela como entidad aparte en este enunciado). |

## 3) Relación/Entidad asociativa: matricula

> Resuelve la relación **N:M** entre **estudiante** y **curso**, y además almacena atributos propios de la inscripción.

| Campo             | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones                                                        |
| ----------------- | ------------ | ------------: | -------------: | ------------: | -------------------------------------------------------------------- |
| rut_estudiante    | VARCHAR(10)  |            No | Sí (compuesta) |            Sí | FK a `estudiante(rut)`.                                              |
| codigo_curso      | VARCHAR(20)  |            No | Sí (compuesta) |            Sí | FK a `curso(codigo)`.                                                |
| anio              | SMALLINT     |            No | Sí (compuesta) |            No | Año en que se inscribe el estudiante. Permite reinscripción por año. |
| fecha_inscripcion | DATE         |            No |             No |            No | Fecha exacta de la matrícula (día/mes/año).                          |

---

# Reflexión

## ¿Cuál fue la mayor dificultad al transformar el modelo conceptual al relacional?

La mayor dificultad suele ser **elegir la clave primaria adecuada** para la entidad asociativa (en este caso, _matricula_).  
Conceptualmente, _matricula_ representa el acto de inscribir a un estudiante en un curso y tiene atributos propios (fecha y año).  
En el modelo relacional, hay que decidir si:

- crear un **ID artificial** (por ejemplo, `id_matricula`), o
- usar una **clave compuesta** con las claves de las entidades relacionadas y un atributo que distinga eventos (por ejemplo, `rut_estudiante + codigo_curso + anio`).

En esta solución se eligió **clave compuesta** para permitir que el mismo estudiante se matricule en el mismo curso en distintos años.

## ¿Qué ventajas tiene normalizar una base de datos? ¿Y cuándo conviene desnormalizarla?

**Ventajas de normalizar:**

- Reduce redundancia (menos datos repetidos).
- Evita anomalías de inserción/actualización/eliminación.
- Mejora la consistencia e integridad de los datos.
- Facilita mantenimiento y evolución del modelo.

**Cuándo conviene desnormalizar:**

- Cuando el sistema es muy consultado (muchas lecturas) y necesitas **mejorar performance** evitando demasiados JOIN.
- En reportes/BI (data marts) donde prima velocidad de consulta.
- Cuando el costo de recomponer datos normalizados es alto y los datos cambian poco.

La desnormalización debe hacerse con cuidado, porque aumenta duplicación y puede afectar la consistencia si no se controla bien.
