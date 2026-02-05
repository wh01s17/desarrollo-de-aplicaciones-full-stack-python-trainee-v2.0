SELECT * FROM peliculas;


-- cuantas peliculas se estrenaron despues del 2000 
SELECT count(*) FROM peliculas
WHERE anio_estreno >= 2000;


-- peliculas que el titulo empiece con la letra A
SELECT * FROM peliculas
WHERE titulo LIKE "A%";

-- cuantas peliculas hay por genero y duracion promedio de peliculas por genero
SELECT
    genero,
    count(*) AS cuenta_peliculas,
    avg(duracion_min) AS duracion_prom
FROM peliculas
GROUP BY genero
ORDER BY cuenta_peliculas DESC;

-- el genero con la duracion promedio de pelicula mas largo
SELECT
    genero,
    avg(duracion_min) AS duracion_prom
FROM peliculas
GROUP BY genero
ORDER BY duracion_prom DESC
LIMIT 1;

-- la pelicula mas larga de cara director
SELECT
    titulo,
    director,
    max(duracion_min) AS duracion_max
FROM peliculas
GROUP BY director;

--cantidad de peliculas por director
SELECT
    director,
    count(director) AS cant_peliculas
FROM peliculas
GROUP BY director
ORDER BY cant_peliculas DESC;
