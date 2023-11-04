USE invernadero;
-- DISTANCIA ENTRE EL CICATA Y LOMA HERMOSA en metros
SELECT 
ST_Distance_Sphere(
    POINT(-99.209770, 19.444514),
    POINT(-99.213797, 19.446817)
) AS distance;



-- DISTANCIA ENTRE EL CICATA Y LOMA HERMOSA en km
SELECT 
ST_Distance_Sphere(
    POINT(-99.209770, 19.444514),
    POINT(-99.213797, 19.446817)
) / 1000 AS distance;


---- DISTANCIA ENTRE EL CICATA (plantacion cafe) Y LOMA HERMOSA (plantacion cempasuchil) en km
SELECT 
ST_Distance_Sphere(
    (
        SELECT `ubicacion`.`ubicacion`
        FROM `ubicacion`
        INNER JOIN `plantacion`
        ON `plantacion`.`id` = `ubicacion`.`id_plantacion`
        WHERE `plantacion`.`nombre` = "Cafe"
    ),
    (
         SELECT `ubicacion`.`ubicacion`
        FROM `ubicacion`
        INNER JOIN `plantacion`
        ON `plantacion`.`id` = `ubicacion`.`id_plantacion`
        WHERE `plantacion`.`nombre` = "Cempasuchil"
    )
) / 1000 AS distancia;