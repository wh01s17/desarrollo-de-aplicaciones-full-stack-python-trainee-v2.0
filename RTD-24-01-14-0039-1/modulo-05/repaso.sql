-- Create
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    fecha_pedido DATE,
    total DECIMAL(10, 2)
);

INSERT INTO clientes (nombre, ciudad)
VALUES ('Juan Perez', 'Valparaíso');

-- Read
SELECT * FROM clientes 
WHERE ciudad = 'Valparaíso';

-- Update
UPDATE clientes SET ciudad = 'Santiago'
WHERE nombre = 'Juan Perez';

-- Delete (Borra datos)
DELETE FROM clientes
WHERE nombre = 'Juan Perez';

-- Borra todos los datos de la tabla clientes
DELETE FROM clientes;

-- DROP TABLES (Borra tablas)
-- CASCADE elimina tablas relacionadas
DROP TABLE pedidos CASCADE;
DROP TABLE clientes CASCADE;
