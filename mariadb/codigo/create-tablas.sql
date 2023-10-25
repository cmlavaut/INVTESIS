
USE invernadero;
CREATE TABLE `clientes` (
    `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `curp` VARCHAR(100) NOT NULL UNIQUE,
    `user` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(50) NOT NULL,
    `id_plantacion` INTEGER NOT NULL,
    
    PRIMARY KEY(id),
    FOREIGN KEY (`id_plantacion`) REFERENCES `plantacion`(`id`)

);
DEFAULT CHARSET=utf8mb4_general_ci

CREATE TABLE 'servidores' (
    'id' INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    'rasp_serial' VARCHAR(50) NOT NULL UNIQUE,
    'id_plantacion' INTEGER NOT NULL,
    
    PRIMARY KEY(id)
    FOREIGN KEY (id_plantacion) REFERENCES PLANTACION(id)
);
DEFAULT CHARSET=utf8mb4_general_ci

CREATE TABLE 'end_device' (
    'id' INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    'esp_serial' VARCHAR(50) NOT NULL UNIQUE,
    'ubicacion' VARCHAR(50) NOT NULL,
    'protocolo_cx' VARCHAR(50) NOT NULL,
    'id_servidor' INTEGER NOT NULL,

    PRIMARY KEY(id)
    FOREIGN KEY (id_servidor) REFERENCES SERVIDORES(id)
);
DEFAULT CHARSET=utf8mb4_general_ci

CREATE TABLE 'sensores' (
    'id' INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    'nombre' VARCHAR(50) NOT NULL,
    'valor' NUMERIC(5,2) NOT NULL,
    'hora_medicion' DATETIME NOT NULL,
    'id_endevice' INTEGER NOT NULL,

    PRIMARY KEY(id)
    FOREIGN KEY (id_endevice) REFERENCES END_DEVICE(id)
);

DEFAULT CHARSET=utf8mb4_general_ci
 */