USE invernadero;

ALTER TABLE `sensores`
add `creado` DATETIME NOT NULL AFTER `id_endevice`,
add `actualizado` DATETIME NOT NULL AFTER `creado`;


