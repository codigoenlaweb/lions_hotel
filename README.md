# Lions Hotels.
Aplicación web en Django, donde se podrá hacer una reservación en el hotel en un rango de fecha seleccionado con distintos tipos de cuartos, confirmar tu habitación a través de un código de verificación enviado por email de manera asíncrona para no afectar el rendimiento del servidor, además dicho cuenta con un tiempo de vencimiento de 10 minutos, por último, al confirmar tu habitación se le enviará un nuevo email al usuario con un código único alfanumérico donde podrá ver su reservación con todos sus datos de la misma. 

## URL de la aplicación.
**Montado en HEROKU**
[Servidor en vivo](https://lionshotel.herokuapp.com/ "servidor en vivo")

## Pre-requisitos.
1. Instalar Python.
2. Pip.
3. Entorno Virtual

## Instalación
> Esta guia de instalacion se basa en el sistema operativo Ubuntu

1. Comencemos por crear una carpeta nueva, en mi caso la llamare **project**.

2. Abrimos la terminal en la carpeta project para poder crear nuestro entorno virtual, en mi caso lo llamare **venv**.
`python3 -m venv venv`

3. procedemos a clonar el repositorio en **Github**.
`git clone https://github.com/codigoenlaweb/lions_hotel.git`

4. Entramos en el entorno virtual **venv**.
`source venv/bin/activate`

5. instalamos los requerimientos en el enotrno virtual **venv**.
`pip install -r lions_hotel/requirements/local.txt`

6. Este proyecto utiliza django-environ, dentro de la aplicación se encontrarán con el archivo **.env.example**, por razones de practicidad esta casi todo rellenado de manera que solo copien y peguen en el archivo **.env** que crearan en la raíz del archivo **lions_hotel** en el mismo nivel que el **manage.py** (esto no es una buena práctica ya que cada quien debe tener sus propias variables de entorno siguiendo el modelo **.env.example** es solo por fines de practicidad), solo faltaría agregar la **SECRET_KEY** que la pueden generar en esta página. 
[generador secret_key](https://djecrety.ir/ "generador secret_key") 

7. procedemos a verificar el resultado.
`python3 manage.py runserver`

##### Has montado tu proyecto en django y ya lo puedes probar todo lo que desees


------------

#### Quieres cambiarle los estilos a la pagina y agregar alguno nuevo?

Para ello debes saber que este proyecto trabaja con **tailwindcss** unos de los frameworks más populares de css y en lo particularmente mi favorito ya que no tiene límites a la hora de personalizarlo y dar tu toque especial.

##### A continuacion la guia de intalacion de tailwind.
este proyecto ya tiene todo configurado para poder trabajar con tailwind asi qued sera corto.

1. Dentro de la carpeta **lions_hotel** dirigirse a jstools.
`cd jstools/`

2. npm install.
`npm install`

3. npm run tailwind para trabajar entorno local y npm run build antes de subir a producción..
`npm run tailwind ` **Local**
`npm run build ` **Producción.**

##### Listo has completado toda la instalación felicidades :) 

## Diseño de base de datos.
[diagrama relacional](https://drive.google.com/file/d/1HpivqhYgemKfOTEcpf3FEgm9jLDR9sZW/view?usp=drivesdk "diagrama relacional")

## Construido con.

1. Python

2. Django

3. Tailwindcss

4. Javascript

## Autor
### Jesús Olmos - Programador en Django Full-stack

## Gracias

Gracias **CHAPP Solutions** por bridarme la oportunidad de hacer esta grandiosa prueba técnica, que como todo y cada una de las cosas que hago le pongo mi corazón, mi firma, mi toque personal y todo el esfuerzo para llegar al objetivo.

Espero que esta aplicación exprese una parte de mí y mi amor hacia mi carrera, he disfrutado hacerla, he aprendido y ha sido otro reto en mi camino como programador.


