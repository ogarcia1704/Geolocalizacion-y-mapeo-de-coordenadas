# Geolocalizacion-y-mapeo-de-coordenadas
Muestra el mapa y las coordenadas con tan solo el nombre de la entidad.

Programa para localizar algun punto con el nombre del lugar.

Oswaldo Missael Garcia Orozco 

PE Ingeniero Topografo Geomatico, Facultad de Ingeniería Civil, carretera Coquimatlán kilometro 9, Coquimatlán 28 400, Coquimatlán, Coli-ma, Oswaldo Missael Garcia Orozco, ogarcia17@ucol.mx

Resumen

Se determinará con exactitud la ubicación de dicho lugar proporcionado por el usuario, respetando el acomodo correcto del lugar (municipio, estado, país) para que el procesamiento sea exitoso. De igual manera se obtendrá un archivo CSV donde se guar-de la ubicación del lugar, las coordenadas, así como la hora y la fecha en que se realizó la consulta. La determinación de las coordenadas geográficas del área proporcionada y el mapa se obtendrá mediante el uso de lenguaje de programación Python, auxilia-do por las librerías GEOPY, FOLIUM, BRANCA, entre otras. Se planea que el mapa obtenido en HTML arroje la ubicación exacta de dicho lugar.

Palabras clave: Geolocalización, Python, Geopy, Folium, Branca, Html, Csv, mapa.

Abstract

The location of said place provided by the user will be accurately determined, respecting the correct arrangement of the place (municipality, state, coun-try) for the processing to be successful. In the same way, a CSV file will be obtained where the location of the place, the coordinates, as well as the time and date when the query was made are saved. The de-termination of the geographic coordinates of the provided area and the map will be obtained through the use of the Python programming language, as-sisted by the GEOPY, FOLIUM, BRANCA libraries, among others. The map obtained in HTML is planned to show the exact location of that place.

Keywords: Geolocation, Python, Geopy, Folium, Branca, Html, Csv, map.

Introducción 

La geolocalización es una tecnología que utiliza datos obtenidos de la computadora o dispositi-vo móvil de un individuo para identificar o des-cribir su ubicación física real. Es una de las manifestaciones más populares del desarrollo actual de tecnologías de la información y recien-temente está experimentando un aumento signi-ficativo de popularidad.
Un sistema de geolocalización es una solución de la tecnología de la información que determi-na la ubicación de un objeto en un entorno físi-co (geoespacial) o virtual (Internet). A menudo, el objeto es una persona que quiere utilizar un servicio basado en la ubicación, mientras man-tiene su privacidad.
Los servicios de software de geolocalización se utilizan para apoyar los objetivos del negocio de las empresas públicas y privadas.
Para obtener la ubicación geográfica aproxima-da de un smartphone se utiliza un sistema de posicionamiento global. El sistema está forma-do por una red de satélites geoestacionarios que dan cobertura a toda la Tierra. Para obtener la ubicación el dispositivo se conecta como mínimo con 3 satélites, de estos satélites recibe un identificador y la hora de cada uno ellos. El dispositivo calcula el tiempo que tarda en llegar la señal desde los satélites y gracias al retardo o delay resultante se obtiene la ubicación por medio de la triangulación.




Ventajas de la Geolocalización

La geolocalización es una tecnología que nos ayuda a mejorar la eficiencia en muchos aspec-tos de nuestra vida cotidiana. Esta tecnología ofrece información en un doble sentido, noso-tros como usuarios nos beneficiamos de la información que nos facilita. Muchas tareas sin esta tecnología serían más complicadas de realizar como obtener la ruta más corta a nues-tro destino, o directamente imposibles como conocer el punto exacto dónde está el último paquete que hemos comprado por Internet, etc.
Pero este flujo de información también viaja en sentido contrario, nosotros facilitamos informa-ción de manera constante sobre nuestra ubica-ción. Cuando publicamos en redes sociales utilizando la funcionalidad de geoposiciona-miento o cuando damos permisos a una app de nuestro smartphone para acceder a nuestra ubicación estamos facilitando información per-sonal sobre nuestros hábitos diarios relativos a rutas, lugares que visitamos o similar.

1.2. 	Riesgos de la Geolocalización

Las ventajas también pueden tener consecuen-cias negativas. Cualquier información de carác-ter personal puede comprometer nuestra priva-cidad y los datos de geolocalización son de este tipo.
La geolocalización y las aplicaciones de mapas son usados más comúnmente de los que pen-samos para realizar acciones delictivas. Los delincuentes utilizan estas herramientas para encontrar objetivos potenciales basándose por ejemplo en las publicaciones que hacemos en redes sociales o la información facilitada por mapas virtuales como Google Maps.
Añadir la ubicación a una publicación puede poner en riesgo a personas, animales o recur-sos que se quiere mantener en el anonimato como bien indica este tweet en el que se avisa a los excursionistas que no indiquen la posición geográfica de los animales que verán ya que los cazadores furtivos pueden utilizar esa infor-mación.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Geolocalizacion-y-mapeo-de-coordenadas/blob/master/Imagenes/2.jpg)
Figura 2.- Ejemplo de los riesgos de la geolocalizacion.

1.3. 	Usos de la Geolocalización.

Utilizando un dispositivo conectado a Internet, con la geolocalización es posible obtener distin-tos tipos de información en tiempo real y locali-zarlos en el mapa con una gran precisión en un momento determinado en el tiempo. Los datos de geolocalización se pueden recopilar de mu-chas formas:
•	Mediante la navegación web a través de direcciones IP.
•	Teléfonos móviles.
•	Dispositivos GPS.
•	Identificación de radiofrecuencia (RFID).
•	Transacciones con tarjeta de crédito o débito.
•	Etiquetas en fotografías y mensajes (ta-les como la geo etiquetas o verificacio-nes mediante aplicaciones como Foursquare) en sitios de redes sociales como Facebook y Twitter.

1.4. 	Impactos de la Geolocalización

La capacidad para proporcionar datos de geo-rreferenciación precisos y oportunos, elementos de etiquetas de interés con metadatos de ubi-cación y para usar las coordenadas de ubica-ción como clave para las bases de datos de búsqueda, se ha convertido en la base de un mercado de software creciente para aplicacio-nes que se ejecutan en plataformas móviles.
La capacidad para proporcionar datos de geo-rreferenciación precisos y oportunos, elementos de etiquetas de interés con metadatos de ubi-cación y para usar las coordenadas de ubica-ción como clave para las bases de datos de búsqueda, se ha convertido en la base de un mercado de software creciente para aplicacio-nes que se ejecutan en plataformas móviles.

1.5. 	Programa por utilizar.

Se utilizará Python, en el cual una vez corrido el código presentara la ubicación exacta y las coordenadas de dicho lugar tecleado por el usuario, así mismo presentara la hora y el día en el que el usuario realizo la búsqueda para poste-riormente toda esta información ser guardada en un archivo CSV el cual lo va a generar auto-máticamente el código.
Finalmente mostrara el mapa con la ubicación exacta la cual es la que el usuario propuso.

1.6. 	Folium

Folium es una librería que requiere la instalación de un par de herramientas, por lo tanto, el pri-mer paso será hacer la instalación de todos los elementos que forman su arquitectura:
•	Necesitamos, en primer lugar, Python y su manejador de paquetes PIP.
•	También necesitamos instalar Jupyter, que es un entorno o una shell que nos permite escribir las instrucciones en Python y ver los resultados en Leaflet. 



