--DELETE FROM `TABLE_NAME`; --ELIMINA TODOS LOS REGISTROS DE LA TABLA pero no reinicia los ids

USE invernadero;
DELETE FROM `clientes` 
WHERE id = 6; --elimina un regstro solamente

TRUNCATE TABLE `clientes`; -- elimina todos los registros  de la tabla y reinicia los ids en la tabla