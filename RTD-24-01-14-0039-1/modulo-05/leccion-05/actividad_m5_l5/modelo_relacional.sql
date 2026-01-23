CREATE TABLE estudiante (
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE curso (
    codigo VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(160) NOT NULL,
    docente_responsable VARCHAR(120) NOT NULL
);

CREATE TABLE matricula (
    rut_estudiante VARCHAR(10) NOT NULL,
    codigo_curso VARCHAR(20) NOT NULL,
    anio SMALLINT NOT NULL,
    fecha_inscripcion DATE NOT NULL,

    CONSTRAINT pk_matricula
        PRIMARY KEY (rut_estudiante, codigo_curso, anio),

    CONSTRAINT fk_matricula_estudiante
        FOREIGN KEY (rut_estudiante)
        REFERENCES estudiante(rut)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_matricula_curso
        FOREIGN KEY (codigo_curso)
        REFERENCES curso(codigo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_matricula_anio
        CHECK (anio BETWEEN 1900 AND 2100)
);
