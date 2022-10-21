# TP_Prog2__Grupo9
Trabajo practico final para la materia Programación 2 de la Tecnicatura Universitaria en Programación - UTN Sede Rosario. Comisión 2 TT - Entrega limite: 24/10/22  - Alumnos: Luciano Fernandez - Julian Vazquez - Ariel Salinas

Se utilizan tecnologias: Python y SQL. IDE Utilizado: Visual Studio Code.

Trabajo realizado en base a la consigna dada por los profesores para el TP Final:

*Desarrollar un sistema que integre una base de datos con SQLite para un sistema de ventas de 
Monopatines Eléctricos. Mediante un menú de opciones llevar a cabo las siguientes 
posibilidades.

*REGULARIDAD
1- Cargar Monopatines.
De cada monopatín almacenar marca, precio, cantidad, disponibles. La marca declararla como 
única e irrepetible. Llevar también a cabo un id como primary key autoincremental.
2- Modificar datos de un monopatín. Dado el código del monopatín, permitir modificar su 
precio.
3- Borrar un monopatín
Dado el código, permitir eliminarlo de la base datos
4- Cargar disponibilidad.
Cada vez que ingresa un nuevo monopatín, incrementar la cantidad disponible. Solicitar al 
usuario la marca e incrementar la cantidad disponible en 1.
5- Listado de productos.
Mostrar ordenadamente todos los productos cargados.
0- Salir del menú.

*PROMOCIÓN
6- Crear una tabla llamada monopatín que contenga los siguientes atributos:
modelo (Varchar (30)), marca (Varchar (30)), potencia (Varchar (30)), precio (Integer), color 
(Varchar(30)), fechaUltimoPrecio (datetime). Llevar a cabo un id auto incremental denominado 
id_mono.
Para esta tabla los atributos marca y modelo NO son únicos e irrepetibles.
7- Por el aumento del dólar se decidió actualizar los precios de todos los monopatines en un 
23%. Se desea mantener el historial de registros de precios actuales. Insertar los registros 
viejos en una tabla llamada “historicoprecios” y actualizar el precio y fecha en la tabla 
monopatin. Para este punto se debe de crear la tabla historico_mono que tendrá exactamente 
las mismas características que la tabla monopatin. Previo a actualizar los precios en la tabla 
monopatin, se deberá de insertar los datos actuales en la tabla historico_mono
8- Mostrar todos los registros anteriores a una fecha en específico de la tabla monopatin.
0- Salir del menú.
CONSIDERACIONES A LA HORA DE CORRECCIÓN:
-Utilización de Programación Orientada a objetos
-Uso de estructuras de manejo de errores (try, except, finally)
-Claridad a la hora de mostrar los mensajes
-Simplicidad del código.
-Optimización del código

