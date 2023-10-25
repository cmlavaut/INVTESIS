USE invernadero;

CREATE TRIGGER update_field_clientes
BEFORE UPDATE
ON `clientes`
FOR EACH ROW
SET NEW.actualizado = NOW();


CREATE TRIGGER update_field_plantacion
BEFORE UPDATE 
ON `plantacion`
FOR EACH ROW
SET NEW.actualizado = NOW();

CREATE TRIGGER update_field_sensores
BEFORE UPDATE 
ON `sensores`
FOR EACH ROW
SET NEW.actualizado = NOW();