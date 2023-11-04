USE invernadero;

/* CREATE TABLE `ubicacion` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `id_plantacion` int NOT NULL,
    `ubicacion` POINT NOT NULL,
    `creado` datetime NOT NULL,
    `actualizado` DATETIME NOT NULL,

    PRIMARY KEY(id)
); */

/
INSERT INTO `ubicacion` (id_plantacion, ubicacion) VALUES
(1, POINT(-99.209770, 19.444514)), --COORDENADAS GEOGRAFICAS DEL CICATA
(2, POINT(-99.213093, 19.457314)),-- coordenadas geograficas de demet toreo edificio managua
(3, POINT(-99.213797, 19.446817)); --coordenadas ksa loma hermosa 