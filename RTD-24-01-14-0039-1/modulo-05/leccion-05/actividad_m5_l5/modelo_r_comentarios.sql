-- Tabla: ESTUDIANTE
CREATE TABLE estudiante (
    -- RUT del estudiante: identificador único
    rut VARCHAR(10) PRIMARY KEY,

    -- Nombre completo del estudiante
    nombre VARCHAR(120) NOT NULL,

    -- Correo electrónico del estudiante
    -- Se define como UNIQUE para evitar duplicados
    correo VARCHAR(120) NOT NULL UNIQUE
);

-- Tabla: CURSO
CREATE TABLE curso (
    -- Código único del curso
    codigo VARCHAR(20) PRIMARY KEY,

    -- Nombre del curso
    nombre VARCHAR(160) NOT NULL,

    -- Docente responsable del curso
    -- Se maneja como texto según el enunciado
    docente_responsable VARCHAR(120) NOT NULL
);

-- Tabla: MATRICULA
-- Entidad asociativa que resuelve la relación N:M entre ESTUDIANTE y CURSO
CREATE TABLE matricula (
    -- RUT del estudiante matriculado
    rut_estudiante VARCHAR(10) NOT NULL,

    -- Código del curso en el que se matricula
    codigo_curso VARCHAR(20) NOT NULL,

    -- Año académico de la matrícula
    -- Permite que un estudiante se matricule
    -- en el mismo curso en distintos años
    anio SMALLINT NOT NULL,

    -- Fecha exacta en que se realizó la matrícula
    fecha_inscripcion DATE NOT NULL,

    -- Clave primaria compuesta
    -- Garantiza unicidad por estudiante, curso y año
    CONSTRAINT pk_matricula 
        PRIMARY KEY (rut_estudiante, codigo_curso, anio),

    -- Clave foránea hacia la tabla ESTUDIANTE
    CONSTRAINT fk_matricula_estudiante 
        FOREIGN KEY (rut_estudiante)
        REFERENCES estudiante(rut)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Clave foránea hacia la tabla CURSO
    CONSTRAINT fk_matricula_curso 
        FOREIGN KEY (codigo_curso)
        REFERENCES curso(codigo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Restricción para asegurar años válidos
    CONSTRAINT chk_matricula_anio 
        CHECK (anio BETWEEN 1900 AND 2100)
);
