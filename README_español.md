# analisis-divvy

# Análisis de datos empresa cyclist
Información básica:
Esta es la documentación del análisis de datos de la empresa cyclist, una empresa ficticia localizada en chicago la cual ofrece un sistema de bicicletas compartidas con un total de 5824 bicicletas y 692 estaciones repartidas por todo Chicago.
La empresa tiene tres principales planes de precios:
•	Pase para una bici
•	Pase para un día completo
•	Membresía anual
El departamento financiero de la empresa ha determinado que su plan de precio más rentable es la membresía anual. Los clientes que compran esta mercancía se les llaman Cyclist Members por la compañía mientras lo que usan los otros dos planes de precios son llamados usuarios casuales.

La flexibilidad en los planes ha sido una de las razones del éxito de la empresa, pero igual desean maximizar la cantidad de membresías anuales vendidas.
El departamento de marketing se da cuenta de que la mayoría de los usuarios casuales ya conocen de la membresia anual, por lo que se da a la tarea de convertir estos usuarios casuales a Cyclist Members.
Para esto marketing necesita saber la respuesta a 3 preguntas claves:
1.	En qué se diferencia el uso que le dan a las bicicletas de Cyclist los usuarios casuales y los Cyclist member.
2.	Porque los usuarios casuales comprarían una membresía anual.
3.	Como puede Cyclist usar los medios digitales para influenciar a los usuarios casuales en convertirse en miembros anuales.
Se me dio la tarea de resolver la primera pregunta de la empresa usando los datos de los viajes de los usuarios de los 12 últimos meses.
La data que se va usar esta publicada en el siguiente link https://divvy-tripdata.s3.amazonaws.com/index.html, (el nombre de la empresa en la data es diferente a el nombre de la empresa del caso ya que esta data es sacada de una empresa real bajo esta licencia https://www.divvybikes.com/data-license-agreement.
Con esta data esta prohibido correlacionar data con nombres reales, direcciones entre otros datos personales.

Manipulación de datos:
Tomando en cuenta de que es una data grande con millones de filas o registros podemos usar varias herramientas como Excel con Power Pivot y Acess, SQL, Python o R.
Para este caso vamos a usar el lenguaje de programación Python para la manipulación de los datos ya que es capaz de manejar grandes cantidades de datos y también usaremos PowerBi para hacer gráficos.
Para ver la manipulación de datos con detalle le recomiendo revisar el script en Python en main.py.
Análisis Final:
El objetivo de nuestro análisis es saber en qué se diferencia el uso de las bicicletas entre los usuarios casuales y los miembros. Para responder esta pregunta tenemos la data de viajes de la empresa.
Lo primero que queremos saber es que tipo de usuarios hace más viajes en total.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen2.png)

 En el anterior grafico podemos observar que 55% de los viajes son hechos por miembros mientras que 44% son hechos por usuarios casuales, esto por si solo no es suficiente para saber que usuarios son mas activos.

La segunda pregunta nos hacemos al ver esto es ¿qué tipo de bicicletas usan los usuarios para sus viajes?

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen1.png)

Con este grafico podemos observar que los usuarios casuales tienen un uso similar en los tipos de bicicletas, pero su bicicleta preferida es la docked bike mientras que para los miembros hay una preferencia clara por las bicicletas clásicas.

Sabiendo esto ahora debemos conocer en qué día de la semana los usuarios están mas activos.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen3.png)

Con este grafico podemos ver que el número de viajes al día es constante para los miembros mientras que los usuarios casuales tienen un número de viajes bajo en los días entre semana y muy alto para los fines semana, especialmente el sábado. 
Ahora queremos saber el promedio de minutos por viaje por cada tipo de usuario y por cada día de la semana.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/image.png)

En este grafico podemos observar que la duración promedio por viaje de los usuarios casuales son mucho más largos que la duración promedio por viaje de los miembros, llegando a su máximo en el fin de semana con una duración promedio de alrededor de 45 minutos por viaje, mientras que para la máxima duración promedio por viaje de los miembros nada mas toma entre 15 y 20 minutos.
Es importante saber que las desviaciones estándar del promedio de los viajes son altas tanto para los usuarios casuales como para los miembros, para usuarios casuales hay una desviación estándar de 5 horas mientras que para los miembros hay una desviación estándar de 50 minutos.
Conclusiones y recomendaciones:
En base al análisis hecho no pudimos sacar ninguna conclusión importante debido a que no podemos relacionar la data con los usuarios, pero si pudimos aprender los siguientes puntos:
-	Los usuarios casuales frecuentan hacer viajes los fines de semana por lo que un intento de marketing en los fines de semana en los puestos de bicicletas sería interesante, así como aumentar el precio de las tarifas los fines de semana para usuarios casuales.

-	Los miembros presentan una gran preferencia sobre las bicicletas clásicas mientras que los miembros casuales hacen más viajes en docked bikes pero no hay una preferencia tan marcada.

-	El promedio de los viajes de los usuarios casuales es mayor que el de los miembros, pero estos también tienen una desviación estándar mas alta que el de los miembros por lo que la duración de los viajes de los usuarios casuales es más impredecibles y más largos podrían tomar 5 horas estos viajes.








