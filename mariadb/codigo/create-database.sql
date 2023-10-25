CREATE DATABASE invernadero; --crear la base de dATOS
SHOW DATABASES; --MOSTRAR LAS BASES DE DATOS QUE EXISTEN
CREATE USER 'cmlavaut'@'localhost' IDENTIFIED BY  'cmlavaut96*';
--Crear las tablas
USE invernadero;
CREATE TABLE 'CLIENTES' (
    'id' INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    'nombre' VARCHAR(50) NOT NULL,
    'curp' VARCHAR(100) NOT NULL UNIQUE,
    'user' VARCHAR(50) NOT NULL UNIQUE,
    'password' VARCHAR(50) NOT NULL,
    
    PRIMARY KEY(id)

)

DEFAULT CHARSET=utf8mb4
COLLATE= utf8mb4_unicode_ci; 