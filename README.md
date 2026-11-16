Contribución del equipo:

Para comenzar, nos hemos dividido las tareas por bloques, por ejemplo:
Funciones principales del juego
Erik: Me he encargado de crear las dos funciones de movimiento, tanto de las palas como de la bola (move_paddle(), move_ball()).
Oscar: Por mi parte, me encargué de realizar las funciones de colisión de la bola con los límites de la pantalla y el reseteo de la bola al tocar el borde (collide_ball_walls(), collide_ball_paddle(), reset_ball()).

Funciones de configuración
Erik: Me encargaba de crear la función del bucle `ask_yes_no()` para las preguntas de sí y no, el otro bucle que, si no ponías un número entero, no paraba de preguntarte hasta que ponías un input válido read_int_in_range() y, por último, el menú principal de configuración para modificar los tamaños de las palas, bolas… (get_config()) 
Oscar: Yo creé las dos funciones que permitían modificar los colores del juego en general, modificando los valores de las luces rojas, verdes y azules (change_colors(), read_color()).

Funciones adicionales
Solo creamos la función de compute_ai_direction() entre los dos




Visión general del diseño: 

El programa se divide en tres partes, lideradas por main(), añadiendo así la configuración previa, la inicialización y el bucle del juego. Antes de abrir el juego, se realizan en la terminal varias preguntas generadas mediante get_config() y change_colors() para personalizar la partida.  Primero consultan al usuario mediante ask_yes_no() y, si responde con un sí, se utiliza read_int_in_range() para leer y verificar cada número. Luego pasamos a la parte visual, donde se utilizan change_colors(), read_color() y read_int_in_range()  para construir las tuplas RGB. Si el jugador prefiere jugar con los valores predeterminados, se jugará con las variables definidas en un principio al inicio del programa.

Con los ajustes definidos, se inicia el pygame mediante main(), centra las palas y coloca la pelota en el centro mediante reset_ball(). Dentro del bucle principal se utilizan las funciones read_player_direction() para leer el teclado del jugador izquierdo y compute_ai_direction() para calcular automáticamente la dirección a seguir de la pala derecha controlada gracias a la constante PLAY_AGAINST_MACHINE. Siguiendo con move_paddle(), move_ball(), collide_ball_walls() y collide_ball_paddle(), los cuales actualizan las posiciones de las palas, de la bola y sus respectivas colisiones. Finalmente, main() hace una comprobación para saber si se ha anotado un punto o no y así actualizar el marcador y resetear la pelota con reset_ball(), además de mostrar el mensaje final con show_message() al alcanzar POINTS_END.



Decisiones clave:

La primera decisión clave que hay que comentar es la colisión entre la pelota y la pala. Esto fue un paso difícil, ya que la pelota es redonda y la pala rectangular; por lo tanto, funcionaba mal. Lo que hicimos fue colocar la pelota como si fuese un cuadrado, es decir, que su colisión sea un cuadrado para así poder detectar su choque mucho más fácil, ya que solo había que mirar si el borde del cuadrado de la pelota y el rectángulo de la pelota hacían contacto. Si esto pasaba, lo marcábamos como choque, pero aquí vino el siguiente problema: la pelota se quedaba todo el rato colisionando con la pala. Esto sucedía porque, al ir por fotogramas, a la pelota no le daba tiempo a alejarse de la pala antes de que se volviese a invertir la velocidad al notificar un choque; por tanto, se quedaba pasando de un lado a otro constantemente. Para resolverlos, forzamos una expulsión de la pelota hasta el borde de la pala, para que no pueda volver a colisionar.


Otra decisión importante fue la de la configuración del usuario, donde hicimos uso de read_int_in_range() para poder asignar límites en las medidas designadas. Para que Python no dé error si el usuario no pone nada o pone una medida errónea, utilizamos un bucle infinito con el while True y con un bloque de try-except. Por tanto, si se escribe algo que no sea un número entero, se avisa de que el texto introducido ha de ser un número entero y se repite la pregunta sin que el programa se cierre. En cambio, si se pone un número, se comprueba que esté dentro del rango permitido  y entonces se acepta. Aparte, hemos hecho uso del ask_yes_no y de .strip().lower() para borrar espacios sobrantes y pasar las respuestas a minúscula, ya que el bucle no deja avanzar si no se añade exactamente “y” o “n”. Finalmente, colocamos un if en el apartado de change_colors para detectar si el color del fondo de pantalla y el de las palas era el mismo; en caso de que sí, se pone el juego en los colores predeterminados (blanco y negro).

También sería importante destacar que hicimos algunas mejoras, las cuales no eran necesarias según las instrucciones. Primero de todo, a la hora de programar la colisión entre la bola y las palas, en vez de hacer uso de vx = -vx, usamos -abs(vx) y abs(vx) según el lado de la pala donde golpee para que así no se nos atasque. Otro cambio significativo aparece en el apartado de change_colors, ya que el poder determinar si el fondo y las palas son del mismo color y hacer una contramedida a ese problema no es algo que estuviera detallado en los comentarios, solo que al llevar a cabo pruebas, nos dimos cuenta de este error y decidimos solucionarlo.  

Existe una última mejora significativa situada en el sistema de control de la IA, ya que, siguiendo los pasos indicados, la pala derecha, cuando la bola está muy cerca, comienza a vibrar porque intenta alinear constantemente su centro con el centro de la bola. En cambio, nuestro código está diseñado para que, cuando se detecte la bola muy cerca, se detenga esta acción, lo que permite observar la pala completamente quieta en cierto momento, haciendo uso de la tolerancia.



Problemas y soluciones:

Nuestros problemas, la gran mayoría, se debieron a que empezamos a hacer el código sin revisar el orden de funciones que nos decía el pdf; por eso, muchas funciones pedían otras que estaban más abajo, hasta que miramos el pdf y nos dimos cuenta del orden.

Otro problema es que había alguna parte que no entendíamos bien, el código que teníamos que poner, ya que somos novatos. Entonces, decidimos buscar en las plataformas de YouTube y TikTok guías de Python; así también nuestros conocimientos de este lenguaje de programación aumentaban.

Otro de nuestros grandes problemas fue la colisión con los límites de la pantalla, ya que al principio no teníamos mucha idea de cómo poder hacerlo, hasta que nos pusimos a interpretar todo con figuras geométricas y esquemáticamente y decidimos asumir que de momento no había colisión. Y decidimos darle valores numéricos a los lados de la pala; también interpretamos con ángulos a dónde debía ser golpeada la bola y la redirección.

Para finalizar, nos tomó algo de tiempo como descubrir bajarle o subirle la dificultad a la IA rival hasta que interpretamos la velocidad como valor numérico y le restamos un valor para hacerlo más fácil/difícil el poder ganarle

Pruebas:

La fase de pruebas la hicimos en tres partes, primero cuando tuvimos las funciones de movimiento, al hacerlo en clase probamos y todo nos funcionaba correctamente, la parte de configuración de tamaños y colores, hicimos una reunión por Discord donde íbamos configurando con opciones que no se podían o dará error y comprobamos que read_int_in_range() funcionaba correctamente, para finalizar, hicimos la prueba del bot por el mismo medio de comunicación ajustando los valores de tolerancia y comprobamos el correcto funcionamiento de este mismo

Funcionalidades opcionales:

En nuestro caso decidimos hacer la función opcional de poder jugar contra una “ia” ya que lo encontramos una parte interesante y así haría nuestro juego más completo, esta función lee los límites de los eje x e y de su campo y le aplicamos una tolerancia para poder o subir la dificultad del bot, entonces hicimos dos if teniendo en cuenta la posición de la bola en ese momento y restandole la tolerancia para que si este valor es muy bajo, que se mueva más rápido y que si es más alto, que se mueva más lento




Uso de IA:

La labor de la IA ha sido hacer que la estructura del código sea más visual y ordenada, ya que al acabar el código había muchos espacios y alguna parte del código con más tabulación de la debida, y hemos hecho que nos corrija estos errores. Decidimos usar la herramienta Gemini por la accesibilidad que tenemos a ella
