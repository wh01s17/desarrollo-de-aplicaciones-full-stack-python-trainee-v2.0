CREATE TABLE peliculas (
    id_pelicula SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    director VARCHAR(100),
    anio_estreno INT,
    duracion_min INT
);

INSERT INTO peliculas (
    titulo, genero, director, anio_estreno, duracion_min
) VALUES
('El Padrino', 'Drama', 'Francis Ford Coppola', 1972, 175),
('El Padrino II', 'Drama', 'Francis Ford Coppola', 1974, 202),
('Pulp Fiction', 'Crimen', 'Quentin Tarantino', 1994, 154),
('Forrest Gump', 'Drama', 'Robert Zemeckis', 1994, 142),
('Matrix', 'Ciencia Ficción', 'Lana Wachowski', 1999, 136),
('Inception', 'Ciencia Ficción', 'Christopher Nolan', 2010, 148),
('Interstellar', 'Ciencia Ficción', 'Christopher Nolan', 2014, 169),
('El Caballero Oscuro', 'Acción', 'Christopher Nolan', 2008, 152),
('Fight Club', 'Drama', 'David Fincher', 1999, 139),
('Gladiador', 'Acción', 'Ridley Scott', 2000, 155),
('Titanic', 'Romance', 'James Cameron', 1997, 195),
('Avatar', 'Ciencia Ficción', 'James Cameron', 2009, 162),
('Jurassic Park', 'Aventura', 'Steven Spielberg', 1993, 127),
('La Lista de Schindler', 'Drama', 'Steven Spielberg', 1993, 195),
(
    'Star Wars: Una Nueva Esperanza',
    'Ciencia Ficción',
    'George Lucas',
    1977,
    121
),
(
    'El Señor de los Anillos: La Comunidad del Anillo',
    'Fantasía',
    'Peter Jackson',
    2001,
    178
),
(
    'El Señor de los Anillos: Las Dos Torres',
    'Fantasía',
    'Peter Jackson',
    2002,
    179
),
(
    'El Señor de los Anillos: El Retorno del Rey',
    'Fantasía',
    'Peter Jackson',
    2003,
    201
),
('Toy Story', 'Animación', 'John Lasseter', 1995, 81),
('Coco', 'Animación', 'Lee Unkrich', 2017, 105);
