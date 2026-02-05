CREATE TABLE paciente (
    rut VARCHAR(10) PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE profesional (
    rut VARCHAR(10) PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL
);

CREATE TABLE atencion (
    id_cita SERIAL PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    tipo_atencion VARCHAR(255) NOT NULL,
    rut_paciente VARCHAR(10) NOT NULL,
    rut_profesional VARCHAR(10) NOT NULL,

    -- CONSTRAINT: permite definir una restricción con nombre propio
    -- Esto facilita la lectura del modelo y la identificación de errores
    -- fk_atencion_paciente es el nombre de la restricción
    CONSTRAINT fk_atencion_paciente

    -- FOREIGN KEY: indica que la columna rut_paciente
    -- es una clave foránea que depende de otra tabla
    FOREIGN KEY (rut_paciente)

    -- REFERENCES: especifica la tabla y columna
    -- donde debe existir previamente el valor
    -- En este caso, rut_paciente debe existir en paciente(rut)
    REFERENCES paciente (rut),

    CONSTRAINT fk_atencion_profesional
    FOREIGN KEY (rut_profesional)
    REFERENCES profesional (rut)
);
